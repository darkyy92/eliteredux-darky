<template>
  <div class="sidebar-enhancer">
    <!-- Multi-user activity indicator -->
    <div v-if="showActivityIndicator" class="activity-indicator">
      <div class="activity-pulse"></div>
      <span class="activity-text">{{ activityText }}</span>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted, onUnmounted, nextTick } from 'vue'
import { useAbilityStatus } from '../composables/useAbilityStatus'

const { 
  getAbilityStatus, 
  statusData, 
  hasPendingChanges, 
  isActiveEnvironment,
  multiUserActivity 
} = useAbilityStatus()

// Activity indicator state
const showActivityIndicator = computed(() => {
  return isActiveEnvironment.value || hasPendingChanges.value
})

const activityText = computed(() => {
  if (hasPendingChanges.value) {
    return 'Syncing changes...'
  } else if (multiUserActivity.value.activeUsers > 1) {
    return 'Other users active'
  } else if (multiUserActivity.value.lastActivity) {
    const ago = Date.now() - multiUserActivity.value.lastActivity
    if (ago < 60000) {
      return 'Recently updated'
    }
  }
  return 'Checking for updates...'
})

// Track sidebar mutations
let sidebarObserver = null
let updateTimer = null

// Update sidebar items with current status
async function updateSidebarItems() {
  await nextTick()
  
  // Find all sidebar links
  const sidebarLinks = document.querySelectorAll('.VPSidebarItem a')
  
  sidebarLinks.forEach(link => {
    const href = link.getAttribute('href')
    if (!href || !href.includes('/abilities/')) return
    
    // Extract ability ID from href (e.g., /abilities/123_ability_name)
    const match = href.match(/\/abilities\/(\d+)_/)
    if (!match) return
    
    const abilityId = match[1]
    const status = getAbilityStatus(abilityId)
    
    if (!status) return
    
    // Add data attribute for CSS targeting
    link.setAttribute('data-ability-id', abilityId)
    link.setAttribute('data-ability-status', status.status || 'pending')
    
    if (status.isPending) {
      link.setAttribute('data-pending', 'true')
    } else {
      link.removeAttribute('data-pending')
    }
    
    // Update the text content with new indicator
    const textNode = link.querySelector('.text') || link
    let text = textNode.textContent || ''
    
    // Only update if not already updated
    if (!link.hasAttribute('data-indicator-applied')) {
      // Remove any existing indicators first
      text = text.replace(/^[✅🟠⏳]\s*/, '')
      
      // Extract just the ability ID and name
      const cleanMatch = text.match(/^(\d+\s+.+)$/)
      if (cleanMatch) {
        const cleanText = cleanMatch[1]
        const indicator = status.indicator || '🟠'
        textNode.textContent = `${indicator} ${cleanText}`
        link.setAttribute('data-indicator-applied', 'true')
      }
    } else {
      // Just update the indicator if it changed
      const currentIndicator = text.match(/^([✅🟠⏳])/)
      const newIndicator = status.indicator || '🟠'
      if (currentIndicator && currentIndicator[1] !== newIndicator) {
        textNode.textContent = text.replace(/^[✅🟠⏳]/, newIndicator)
      }
    }
    
    // Add activity class if recently changed
    if (status.lastModified && Date.now() - status.lastModified < 3000) {
      link.classList.add('ability-just-updated')
      setTimeout(() => {
        link.classList.remove('ability-just-updated')
      }, 3000)
    }
  })
}

// Debounced update function
function scheduleUpdate() {
  if (updateTimer) {
    clearTimeout(updateTimer)
  }
  updateTimer = setTimeout(updateSidebarItems, 500) // Increased delay to prevent rapid updates
}

// Watch for status changes
watch(() => statusData.value, () => {
  scheduleUpdate()
}, { deep: true })

// Setup mutation observer to detect sidebar changes
function setupSidebarObserver() {
  // Find sidebar container
  const sidebar = document.querySelector('.VPSidebar')
  if (!sidebar) {
    // Retry after a short delay
    setTimeout(setupSidebarObserver, 500)
    return
  }
  
  // Create observer
  sidebarObserver = new MutationObserver((mutations) => {
    // Check if sidebar items were added/modified
    const hasSidebarChanges = mutations.some(mutation => {
      return mutation.addedNodes.length > 0 || 
             (mutation.type === 'childList' && mutation.target.classList.contains('VPSidebarItem'))
    })
    
    if (hasSidebarChanges) {
      scheduleUpdate()
    }
  })
  
  // Start observing
  sidebarObserver.observe(sidebar, {
    childList: true,
    subtree: true,
    attributes: false
  })
  
  // Initial update
  updateSidebarItems()
}

// Handle route changes
function handleRouteChange() {
  // Update sidebar after navigation
  nextTick(() => {
    scheduleUpdate()
  })
}

onMounted(() => {
  setupSidebarObserver()
  
  // Listen for route changes
  if (window) {
    window.addEventListener('popstate', handleRouteChange)
    
    // Also listen for Vue Router navigation
    const pushState = history.pushState
    history.pushState = function() {
      pushState.apply(history, arguments)
      handleRouteChange()
    }
  }
})

onUnmounted(() => {
  if (sidebarObserver) {
    sidebarObserver.disconnect()
  }
  
  if (updateTimer) {
    clearTimeout(updateTimer)
  }
  
  window.removeEventListener('popstate', handleRouteChange)
})
</script>

<style scoped>
.sidebar-enhancer {
  position: fixed;
  top: var(--vp-nav-height);
  left: 0;
  right: 0;
  z-index: 100;
  pointer-events: none;
}

.activity-indicator {
  position: absolute;
  top: 0.5rem;
  left: 1rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-border);
  border-radius: 20px;
  padding: 0.25rem 0.75rem;
  font-size: 0.75rem;
  color: var(--vp-c-text-2);
  pointer-events: auto;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  animation: slideIn 0.3s ease-out;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.activity-pulse {
  width: 8px;
  height: 8px;
  background: var(--vp-c-brand);
  border-radius: 50%;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0% {
    opacity: 1;
    transform: scale(1);
  }
  50% {
    opacity: 0.5;
    transform: scale(1.2);
  }
  100% {
    opacity: 1;
    transform: scale(1);
  }
}

/* Sidebar item states - using global styles to affect VitePress sidebar */
:global(.VPSidebarItem a[data-ability-status="reviewed"]) {
  position: relative;
}

:global(.VPSidebarItem a[data-pending="true"]) {
  position: relative;
  opacity: 0.8;
}

:global(.VPSidebarItem a[data-pending="true"]::after) {
  content: '';
  position: absolute;
  top: 50%;
  right: 1rem;
  transform: translateY(-50%);
  width: 6px;
  height: 6px;
  background: var(--vp-c-warning);
  border-radius: 50%;
  animation: pulse 1s infinite;
}

:global(.VPSidebarItem a.ability-just-updated) {
  animation: highlightUpdate 0.5s ease-out;
}

@keyframes highlightUpdate {
  0% {
    background: rgba(100, 108, 255, 0.2);
  }
  100% {
    background: transparent;
  }
}

/* Mobile adjustments */
@media (max-width: 768px) {
  .activity-indicator {
    font-size: 0.7rem;
    padding: 0.2rem 0.6rem;
  }
}
</style>