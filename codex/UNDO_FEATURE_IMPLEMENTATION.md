# UNDO Feature Implementation

## Overview
Added an UNDO feature that delays GitHub API calls by 5 seconds, allowing users to cancel save/approve actions by pressing 'Z' or clicking the undo button.

## Simple Implementation

### 1. useUIState.js - Added Pending Action System
```javascript
const pendingAction = ref(null)
const pendingTimeout = ref(null)

function showUndoableSuccess(message, action, options = {}) {
  // Cancel any existing pending action
  if (pendingTimeout.value) {
    clearTimeout(pendingTimeout.value)
  }
  
  // Store and delay the action
  pendingAction.value = action
  pendingTimeout.value = setTimeout(() => {
    if (pendingAction.value) {
      pendingAction.value()
    }
  }, duration)
  
  // Show toast with undo button
  return showToast({
    type: 'success',
    message,
    duration,
    undoable: true,
    action: { text: 'Undo (Z)', handler: cancelAction }
  })
}
```

### 2. Toast.vue - Added Z Keyboard Support
- Added `undoable` prop
- Enhanced keyboard handler to support 'Z' key
- Only triggers when not typing in input fields

### 3. InlineAbilityEditor.vue - Refactored Handlers
**Before:**
```javascript
// GitHub API call happens immediately after modal confirm
showSuccess('Saved!')
```

**After:**
```javascript
// Create action callback
const executeSave = async () => {
  // GitHub API call happens here
  showSuccess('Saved!')
}

// Queue action with undo capability
showUndoableSuccess('Saving...', executeSave, { duration: 5000 })
```

## How It Works

1. User clicks Save/Approve → Modal confirms
2. Toast appears: "Saving... [Undo (Z)]" with progress bar
3. User has 5 seconds to:
   - Press 'Z' to cancel
   - Click "Undo (Z)" button
   - Or let it complete
4. If not cancelled, GitHub API is called
5. Success message shows after completion

## Benefits
- **Simple**: Single pending action, no complex queues
- **Effective**: Prevents accidental commits
- **Accessible**: Keyboard shortcut 'Z'
- **Visual**: Progress bar shows remaining time

## Testing
```bash
cd eliteredux-darky/codex
npm run dev
```

1. Edit an ability
2. Save changes
3. Press 'Z' during the 5-second delay
4. Verify "Action cancelled" appears
5. Verify no GitHub commit was made