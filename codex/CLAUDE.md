# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

The Elite Redux Ability Codex is a VitePress-based documentation site that provides a searchable database of all game abilities with extended descriptions. It includes an inline editing system for community contributions.

## Commands

### Development
```bash
# Install dependencies (first time setup)
npm install

# Start development server (runs on port 5173)
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Sync abilities from knowledge/abilities/ directory
npm run copy-abilities
```

## Architecture

### Key Components

1. **VitePress Site Structure**
   - `docs/` - Content directory with all markdown files
   - `docs/.vitepress/` - VitePress configuration and theme
   - `docs/abilities/` - Auto-synced ability documentation (DO NOT EDIT DIRECTLY)
   - `scripts/copy-abilities.js` - Syncs abilities from `../knowledge/abilities/`

2. **Custom Vue Components**
   - `InlineAbilityEditor.vue` - In-browser markdown editor with character counting
   - `SuggestEdit.vue` - GitHub issue creation for community contributions

3. **Ability Sync System**
   - Abilities are maintained in `../knowledge/abilities/` (source of truth)
   - `copy-abilities.js` copies them to `docs/abilities/` before dev/build
   - Also runs `fix_ability_caps.py` to normalize title capitalization

### Character Count Requirements

Extended ability descriptions MUST be 280-300 characters INCLUDING spaces due to GBA hardware limitations. The inline editor enforces this with real-time character counting.

### Frontmatter Structure

Each ability file uses frontmatter for metadata:
```yaml
---
name: "Ability Name"
id: 123
description: "Short description"
extendedDescription: "280-300 character extended description..."
reviewed: true  # Shows ✅ in sidebar when true
---
```

## Common Tasks

### Updating Ability Documentation
1. Edit the source file in `../knowledge/abilities/`
2. Run `npm run dev` (automatically syncs)
3. Verify changes in the local site

### Testing Character Count Editor
The inline editor component calculates character count for the extended description. When testing:
- Ensure count shows correctly (e.g., "295/300")
- Verify the count updates as you type
- Check that it only counts the extendedDescription value

### Deployment
The site auto-deploys to GitHub Pages when changes are pushed to main branch. Custom domain: `codex.elite-redux.com`

## Keyboard Shortcuts

### Current Shortcuts
- **E** - Open the ability editor (when on an ability page)
- **Ctrl+S / Cmd+S** - Save changes (when editor is open)
- **Escape** - Close editor, modals, or dismiss toasts
- **Enter** - Confirm modal actions
- **Tab** - Navigate within modals (focus trapped)
- **Z** - Undo pending save/approve actions (when toast is visible)

### Implementation Learnings

When implementing keyboard shortcuts in Vue/VitePress:

1. **Check for Input Context**
   ```javascript
   const isTyping = ['INPUT', 'TEXTAREA', 'SELECT'].includes(event.target.tagName)
   ```
   Always check if the user is typing in a form field to avoid triggering shortcuts accidentally.

2. **Modifier Key Awareness**
   - Check for `event.ctrlKey`, `event.metaKey`, `event.altKey` to avoid conflicts
   - Use both `event.key === 'e'` and `event.key === 'E'` for case-insensitive matching

3. **State-Based Shortcuts**
   - Different shortcuts should be active in different states (collapsed vs expanded editor)
   - Use conditional logic: `if (!isExpanded.value && isAbilityPage.value)`

4. **Visual Hints**
   - Add `title` attributes to buttons: `title="Edit this ability (E)"`
   - Include visible keyboard hints: `<kbd>E</kbd>` styled elements
   - Show hints near relevant UI elements for better discoverability

5. **Event Handling Best Practices**
   - Always `event.preventDefault()` for handled shortcuts
   - Register/unregister listeners in `onMounted`/`onUnmounted` lifecycle hooks
   - Use document-level listeners for global shortcuts

### UI Component Integration

The codex now uses inline UI components instead of browser popups:
- **Modal.vue** - Replaces `confirm()` dialogs
- **Toast.vue** - Replaces `alert()` messages
- **UIProvider.vue** - Manages global UI state
- **useUIState.js** - Composable for UI interactions

This solves Firefox popup blocking issues and provides better UX with full keyboard support.

### UNDO Feature Implementation

The codex now includes an UNDO feature for save/approve actions:

1. **Delayed Execution**: GitHub API calls are delayed by 5 seconds
2. **Undo Toast**: Shows "Undo (Z)" button during the delay
3. **Keyboard Support**: Press 'Z' to cancel the pending action
4. **Simple Implementation**:
   - `showUndoableSuccess()` in useUIState.js handles the delay
   - Single pending action at a time (new actions cancel previous)
   - Toast progress bar shows remaining time
5. **User Benefits**:
   - Prevents accidental saves/approvals
   - No immediate commits to GitHub
   - Time to reconsider actions

## Important Notes

- Never edit files in `docs/abilities/` directly - they are auto-generated
- The inline editor uses regex to parse frontmatter - be careful with complex markdown
- Character counts ALWAYS include spaces (GBA renders spaces as tiles)
- The site uses dark theme by default but supports theme switching

## Future Enhancement: Real-Time Updates

Real-time updates are currently disabled. The planned automated approval workflow (see `/plans/automated_approval_workflow/`) will provide instant updates without the polling issues.