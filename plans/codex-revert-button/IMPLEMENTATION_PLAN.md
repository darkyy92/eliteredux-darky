# Implementation Plan: Red "Not Done Yet" Button for Codex

## Overview

Add a red "Not Done Yet" button to the Codex that allows users to revert ability approvals. This button will appear in place of the green "Approve This Ability" button when an ability is already approved.

## Context

The Codex recently implemented:
1. **Undo Feature** (commit f039a42): 5-second window to cancel actions
2. **Real-Time Updates** (commit 48cd1df): Hot-reloading with multi-user support

These features provide the perfect foundation for our revert button.

## Requirements

### Functional Requirements
- Red button appears only when ability is already approved
- Clicking button reverts status from "reviewed" to "written"
- Confirmation modal before executing revert
- 5-second undo window after confirming
- Real-time sync to all connected users

### Visual Requirements
- Red color scheme (#e53e3e) for danger action
- "Not Done Yet" text on button
- Smooth hover effects
- Clear modal messaging about consequences

## Implementation Details

### 1. InlineAbilityEditor.vue Changes

#### A. Add Revert Button (Line ~20)
```vue
<button 
  v-if="isReviewed"
  class="editor-button danger"
  @click="revertApproval"
  :disabled="reverting"
>
  {{ reverting ? 'Reverting...' : 'Not Done Yet' }}
</button>
```

This replaces the approve button when `isReviewed` is true.

#### B. Add State Variable (Line ~215)
```javascript
const reverting = ref(false)
const revertModalOpen = ref(false)
```

#### C. Add Modal Message (Line ~230)
```javascript
const revertModalMessage = computed(() => {
  return `Are you sure you want to revert the approval for "${abilityInfo.value.name}" (ID: ${abilityInfo.value.id})?

This will:
• Mark it as needing review again
• Remove it from approved abilities
• Update all connected users instantly

Current status: Approved ✅ → Needs Review 🟠`
})
```

#### D. Add Revert Methods (After line ~840)
```javascript
function revertApproval() {
  if (reverting.value || !isReviewed.value) return
  
  // Show revert modal
  revertModalOpen.value = true
}

async function handleRevertConfirm() {
  revertModalOpen.value = false
  
  // Optimistic update - immediately update UI
  await updateAbilityStatus(abilityInfo.value.id, {
    status: 'written',
    reviewed: false,
    written: true
  })
  
  // Create the revert action
  const executeRevert = async () => {
    reverting.value = true
    
    try {
      const filePath = `knowledge/abilities/${abilityInfo.value.filename}.md`
      
      // Step 1: Get current file content from GitHub
      const getResponse = await fetch(
        `https://api.github.com/repos/${REPO_OWNER}/${REPO_NAME}/contents/${filePath}`,
        {
          headers: {
            'Authorization': `token ${GITHUB_TOKEN}`,
            'Accept': 'application/vnd.github.v3+json'
          }
        }
      )
      
      if (!getResponse.ok) {
        throw new Error(`Failed to fetch file: ${getResponse.statusText}`)
      }
      
      const fileData = await getResponse.json()
      const currentContent = atob(fileData.content)
      
      // Step 2: Update frontmatter status
      let updatedContent = currentContent
      
      // Change status from reviewed to written
      if (updatedContent.includes('status: reviewed')) {
        updatedContent = updatedContent.replace(
          /status:\s*reviewed/,
          'status: written'
        )
      } else {
        // If no status field, add it
        const frontmatterEnd = updatedContent.indexOf('\n---\n')
        if (frontmatterEnd > 0) {
          updatedContent = updatedContent.slice(0, frontmatterEnd) + 
                          '\nstatus: written' + 
                          updatedContent.slice(frontmatterEnd)
        }
      }
      
      // Step 3: Commit the change
      const updateResponse = await fetch(
        `https://api.github.com/repos/${REPO_OWNER}/${REPO_NAME}/contents/${filePath}`,
        {
          method: 'PUT',
          headers: {
            'Authorization': `token ${GITHUB_TOKEN}`,
            'Accept': 'application/vnd.github.v3+json',
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            message: `Revert approval for ${abilityInfo.value.id} ${abilityInfo.value.name}`,
            content: btoa(updatedContent),
            sha: fileData.sha,
            branch: 'main'
          })
        }
      )
      
      if (!updateResponse.ok) {
        throw new Error(`Failed to update file: ${updateResponse.statusText}`)
      }
      
      // Step 4: Update local content
      originalContent.value = updatedContent
      editedContent.value = updatedContent
      
      showSuccess(`Successfully reverted approval for ${abilityInfo.value.name}!`, {
        duration: 8000
      })
      
    } catch (error) {
      console.error('Error reverting approval:', error)
      
      // Revert the optimistic update on failure
      await updateAbilityStatus(abilityInfo.value.id, {
        status: 'reviewed',
        reviewed: true,
        written: true
      })
      
      showError(`Failed to revert approval: ${error.message}`)
    } finally {
      reverting.value = false
    }
  }
  
  // Show undoable success notification and queue the revert
  showUndoableSuccess(
    `Reverting approval for ${abilityInfo.value.name}...`,
    executeRevert,
    { duration: 5000 }
  )
}
```

#### E. Add Modal Component (Line ~192)
```vue
<!-- Revert Modal -->
<Modal
  v-model:isOpen="revertModalOpen"
  title="Revert Ability Approval"
  :message="revertModalMessage"
  confirmText="Revert Approval"
  cancelText="Cancel"
  :danger="true"
  @confirm="handleRevertConfirm"
  @cancel="revertModalOpen = false"
/>
```

### 2. CSS Styling Changes

Add to the `<style scoped>` section (around line ~1350):

```css
/* Danger/Revert Button */
.editor-button.danger {
  background: #e53e3e;
  color: white;
  border-color: #e53e3e;
}

.editor-button.danger:hover:not(:disabled) {
  background: #c53030;
  border-color: #c53030;
  transform: translateY(-1px);
  box-shadow: 0 2px 8px rgba(229, 62, 62, 0.3);
}

.editor-button.danger:active:not(:disabled) {
  transform: translateY(0);
  box-shadow: 0 1px 4px rgba(229, 62, 62, 0.2);
}

.editor-button.danger:disabled {
  background: #feb2b2;
  border-color: #feb2b2;
}
```

## How It Works

### User Flow
1. User sees approved ability (green checkmark ✅)
2. Clicks red "Not Done Yet" button
3. Confirmation modal appears with clear messaging
4. User confirms → 5-second undo toast appears
5. UI immediately updates to show 🟠 (pending sync)
6. After 5 seconds, GitHub API call executes
7. GitHub Actions regenerate all status files
8. All connected users see the update within 2-5 seconds

### Technical Flow
1. **Optimistic Update**: `updateAbilityStatus()` immediately updates local state
2. **Undo Window**: `showUndoableSuccess()` delays the actual API call
3. **GitHub API**: Updates the frontmatter in the ability markdown file
4. **GitHub Actions**: Workflow regenerates `progress.md`, `ability-status.json`, etc.
5. **Polling Sync**: Real-time system propagates changes to all users
6. **Reconciliation**: Local state syncs with server state

## Testing Plan

### Single User Testing
1. Approve an ability → Verify green checkmark
2. Click "Not Done Yet" → Verify modal appears
3. Confirm → Verify undo toast (5 seconds)
4. Let it complete → Verify 🟠 status
5. Test undo (press Z within 5 seconds)

### Multi-User Testing
1. Open Codex in two browsers
2. User A reverts an ability
3. User B should see update within 5 seconds
4. Check "Other users active" indicator

### Error Testing
1. Disable network after clicking revert
2. Verify optimistic update reverts
3. Verify error message appears

## Benefits

1. **Mistake Correction**: Fix accidental approvals beyond 5-second window
2. **Quality Control**: Re-review abilities if issues found
3. **Consistent UX**: Same patterns as approve/save
4. **Real-Time Sync**: All users stay in sync
5. **Network Resilient**: Optimistic updates + error handling

## Future Enhancements

1. **Audit Log**: Track who reverted and when
2. **Bulk Revert**: Select multiple abilities to revert
3. **Revert Reason**: Optional text field for why reverting
4. **Notifications**: Email/Discord when abilities are reverted