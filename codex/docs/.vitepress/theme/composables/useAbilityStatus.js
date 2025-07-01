import { ref, reactive, computed, watch, onMounted, onUnmounted } from 'vue'

// Constants for polling intervals
const POLL_INTERVAL_IDLE = 30000 // 30 seconds when idle
const POLL_INTERVAL_ACTIVE = 5000 // 5 seconds when activity detected
const POLL_INTERVAL_PENDING = 2000 // 2 seconds when user has pending changes
const ACTIVITY_THRESHOLD = 60000 // Consider activity within last 60 seconds as "active"
const STORAGE_KEY = 'codex-ability-status-local'
const ACTIVITY_KEY = 'codex-ability-activity'

// Global state (shared across all component instances)
const statusData = ref({})
const localOverrides = ref({})
const pendingChanges = ref(new Set())
const lastSync = ref(null)
const isPolling = ref(false)
const pollInterval = ref(POLL_INTERVAL_IDLE)
const pollTimer = ref(null)
const lastETag = ref(null)
const multiUserActivity = ref({
  lastActivity: null,
  activeUsers: 0,
  recentChanges: []
})

// Initialize from localStorage
if (typeof window !== 'undefined') {
  try {
    const stored = localStorage.getItem(STORAGE_KEY)
    if (stored) {
      const data = JSON.parse(stored)
      localOverrides.value = data.overrides || {}
      pendingChanges.value = new Set(data.pending || [])
    }
  } catch (e) {
    console.warn('Failed to load local ability status:', e)
  }
}

export function useAbilityStatus() {
  // Computed state
  const mergedStatus = computed(() => {
    // Merge server data with local overrides
    const merged = { ...statusData.value }
    
    // Apply local overrides
    for (const [id, status] of Object.entries(localOverrides.value)) {
      if (merged.abilities && merged.abilities[id]) {
        merged.abilities[id] = {
          ...merged.abilities[id],
          ...status,
          isPending: pendingChanges.value.has(id)
        }
      }
    }
    
    return merged
  })
  
  const hasPendingChanges = computed(() => pendingChanges.value.size > 0)
  
  const isActiveEnvironment = computed(() => {
    if (hasPendingChanges.value) return true
    if (!multiUserActivity.value.lastActivity) return false
    
    const timeSinceActivity = Date.now() - multiUserActivity.value.lastActivity
    return timeSinceActivity < ACTIVITY_THRESHOLD
  })
  
  // Get status for a specific ability
  function getAbilityStatus(abilityId) {
    const id = String(abilityId)
    const merged = mergedStatus.value
    
    if (merged.abilities && merged.abilities[id]) {
      return {
        ...merged.abilities[id],
        indicator: getStatusIndicator(merged.abilities[id]),
        isPending: pendingChanges.value.has(id)
      }
    }
    
    return null
  }
  
  // Get visual indicator for status
  function getStatusIndicator(status) {
    if (!status) return '🟠' // Default orange
    
    if (status.isPending) {
      return '⏳' // Pending sync
    } else if (status.reviewed || status.status === 'reviewed') {
      return '✅' // Reviewed
    } else if (status.written || status.status === 'written') {
      return '🟠' // Written but not reviewed
    } else {
      return '⏳' // Not written
    }
  }
  
  // Update ability status (optimistic update)
  async function updateAbilityStatus(abilityId, updates) {
    const id = String(abilityId)
    
    // Apply local override immediately
    localOverrides.value[id] = {
      ...localOverrides.value[id],
      ...updates,
      lastModified: Date.now()
    }
    
    // Mark as pending
    pendingChanges.value.add(id)
    
    // Update activity timestamp
    recordActivity(`Updated ability ${id}`)
    
    // Save to localStorage
    saveLocalState()
    
    // Force update the merged status to trigger reactivity
    statusData.value = { ...statusData.value }
    
    // Trigger faster polling
    adjustPollingInterval()
    
    if (import.meta.env.DEV) {
      console.log(`[useAbilityStatus] Updated ability ${id} locally:`, updates)
    }
    
    return true
  }
  
  // Record user activity
  function recordActivity(action) {
    multiUserActivity.value.lastActivity = Date.now()
    multiUserActivity.value.recentChanges.unshift({
      action,
      timestamp: Date.now()
    })
    
    // Keep only last 10 changes
    if (multiUserActivity.value.recentChanges.length > 10) {
      multiUserActivity.value.recentChanges.pop()
    }
    
    // Store activity in localStorage for other tabs
    try {
      localStorage.setItem(ACTIVITY_KEY, JSON.stringify({
        lastActivity: multiUserActivity.value.lastActivity,
        timestamp: Date.now()
      }))
    } catch (e) {
      console.warn('Failed to store activity:', e)
    }
  }
  
  // Check for activity from other users/tabs
  function checkMultiUserActivity() {
    try {
      const stored = localStorage.getItem(ACTIVITY_KEY)
      if (stored) {
        const activity = JSON.parse(stored)
        if (activity.timestamp > (multiUserActivity.value.lastActivity || 0)) {
          multiUserActivity.value.lastActivity = activity.timestamp
          multiUserActivity.value.activeUsers++
        }
      }
    } catch (e) {
      console.warn('Failed to check activity:', e)
    }
  }
  
  // Sync with server
  async function syncWithServer(force = false) {
    if (isPolling.value && !force) return
    
    isPolling.value = true
    
    try {
      // Check for multi-user activity first
      checkMultiUserActivity()
      
      // Fetch ability status with ETag support
      const headers = {}
      if (lastETag.value && !force) {
        headers['If-None-Match'] = lastETag.value
      }
      
      const response = await fetch('/ability-status.json', {
        method: 'GET',
        headers,
        cache: force ? 'no-cache' : 'default'
      })
      
      if (response.status === 304) {
        // Not modified - data hasn't changed
        if (import.meta.env.DEV) {
          console.log('Ability status unchanged (304)')
        }
      } else if (response.ok) {
        const data = await response.json()
        statusData.value = data
        lastSync.value = Date.now()
        
        // Log only in development
        if (import.meta.env.DEV) {
          console.log('[useAbilityStatus] Loaded status data:', {
            totalAbilities: data.metadata?.total_abilities,
            hasAbilities: !!data.abilities,
            abilitiesCount: Object.keys(data.abilities || {}).length
          })
        }
        
        // Store ETag for next request
        const etag = response.headers.get('ETag')
        if (etag) {
          lastETag.value = etag
        }
        
        // Reconcile pending changes
        reconcilePendingChanges(data)
        
        // Check if there's recent activity from other users
        detectMultiUserChanges(data)
      } else {
        console.error('Failed to fetch ability status:', response.status)
      }
    } catch (error) {
      console.error('Error syncing ability status:', error)
    } finally {
      isPolling.value = false
      
      // Adjust polling interval based on activity
      adjustPollingInterval()
    }
  }
  
  // Detect changes made by other users
  function detectMultiUserChanges(serverData) {
    if (!serverData.metadata || !serverData.metadata.generated_at) return
    
    const serverTimestamp = new Date(serverData.metadata.generated_at).getTime()
    const localTimestamp = lastSync.value || 0
    
    if (serverTimestamp > localTimestamp + 5000) {
      // Data was updated by another user
      multiUserActivity.value.lastActivity = serverTimestamp
      multiUserActivity.value.activeUsers++
      recordActivity('Detected changes from another user')
    }
  }
  
  // Reconcile local pending changes with server data
  function reconcilePendingChanges(serverData) {
    if (!serverData.abilities) return
    
    const reconciledIds = []
    
    for (const id of pendingChanges.value) {
      const localStatus = localOverrides.value[id]
      const serverStatus = serverData.abilities[id]
      
      if (serverStatus && localStatus) {
        // Check if server has the same status we were trying to set
        const localReviewed = localStatus.reviewed || localStatus.status === 'reviewed'
        const serverReviewed = serverStatus.reviewed || serverStatus.status === 'reviewed'
        
        if (localReviewed === serverReviewed) {
          // Change has been applied on server
          reconciledIds.push(id)
        }
      }
    }
    
    // Remove reconciled changes
    for (const id of reconciledIds) {
      pendingChanges.value.delete(id)
      delete localOverrides.value[id]
    }
    
    if (reconciledIds.length > 0) {
      saveLocalState()
      if (import.meta.env.DEV) {
        console.log(`Reconciled ${reconciledIds.length} pending changes`)
      }
    }
  }
  
  // Adjust polling interval based on activity
  function adjustPollingInterval() {
    let newInterval = POLL_INTERVAL_IDLE
    
    if (hasPendingChanges.value) {
      // User has pending changes - poll frequently
      newInterval = POLL_INTERVAL_PENDING
    } else if (isActiveEnvironment.value) {
      // Recent activity detected - poll more frequently
      newInterval = POLL_INTERVAL_ACTIVE
    }
    
    if (newInterval !== pollInterval.value) {
      pollInterval.value = newInterval
      restartPolling()
    }
  }
  
  // Start polling
  function startPolling() {
    if (pollTimer.value) return
    
    // Initial sync
    syncWithServer()
    
    // Set up polling
    pollTimer.value = setInterval(() => {
      syncWithServer()
    }, pollInterval.value)
  }
  
  // Stop polling
  function stopPolling() {
    if (pollTimer.value) {
      clearInterval(pollTimer.value)
      pollTimer.value = null
    }
  }
  
  // Restart polling with new interval
  function restartPolling() {
    stopPolling()
    startPolling()
  }
  
  // Save local state to localStorage
  function saveLocalState() {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify({
        overrides: localOverrides.value,
        pending: Array.from(pendingChanges.value),
        lastSave: Date.now()
      }))
    } catch (e) {
      console.warn('Failed to save local ability status:', e)
    }
  }
  
  // Clear all local overrides
  function clearLocalOverrides() {
    localOverrides.value = {}
    pendingChanges.value.clear()
    saveLocalState()
  }
  
  // Force refresh from server
  async function forceRefresh() {
    lastETag.value = null
    await syncWithServer(true)
  }
  
  // Listen for storage events (changes from other tabs)
  function handleStorageChange(event) {
    if (event.key === ACTIVITY_KEY) {
      checkMultiUserActivity()
      adjustPollingInterval()
    } else if (event.key === STORAGE_KEY) {
      // Another tab updated local overrides
      try {
        const data = JSON.parse(event.newValue)
        localOverrides.value = data.overrides || {}
        pendingChanges.value = new Set(data.pending || [])
      } catch (e) {
        console.warn('Failed to sync storage change:', e)
      }
    }
  }
  
  // Lifecycle management
  onMounted(() => {
    startPolling()
    
    // Listen for changes from other tabs
    window.addEventListener('storage', handleStorageChange)
    
    // Listen for visibility changes
    document.addEventListener('visibilitychange', () => {
      if (document.visibilityState === 'visible') {
        // Tab became visible - check for updates
        syncWithServer()
      }
    })
  })
  
  onUnmounted(() => {
    stopPolling()
    window.removeEventListener('storage', handleStorageChange)
  })
  
  return {
    // State
    statusData: computed(() => mergedStatus.value),
    hasPendingChanges,
    isPolling,
    lastSync,
    multiUserActivity: computed(() => multiUserActivity.value),
    isActiveEnvironment,
    
    // Methods
    getAbilityStatus,
    updateAbilityStatus,
    syncWithServer,
    forceRefresh,
    clearLocalOverrides,
    
    // Utility
    getStatusIndicator
  }
}