# Codex Character Count Fix v2 - Complete Rewrite

## Problem Summary
Character counting in the Codex inline editor was severely broken:
1. First ability: Sometimes worked (289/300)
2. Second ability: Wrong count (~10 chars off)
3. Third+ abilities: Showed 0/300 or even 3030/300

## Root Cause Analysis
The 3030 character count (exactly 10x 303) indicated the regex was capturing way too much content - likely the entire file after the extended description section. The issues were:

1. **Overly complex regex patterns** that were too greedy
2. **Format variations** between abilities (asterisks vs plain text for instructions)
3. **Race conditions** during navigation between abilities
4. **State not properly reset** when component was reused

## Solution Implemented

### 1. New Extraction Function
Replaced complex regex with a more robust substring-based approach:

```javascript
function extractExtendedDescription(content) {
  if (!content) return ''
  
  // Strip frontmatter first
  const contentWithoutFm = stripFrontmatter(content)
  
  // Find the start of Extended In-Game Description section
  const startMatch = contentWithoutFm.match(/## Extended In-Game Description.*?\n/)
  if (!startMatch) return ''
  
  const startIndex = startMatch.index + startMatch[0].length
  let remainingContent = contentWithoutFm.substring(startIndex)
  
  // Skip the instruction line if present (with or without asterisks)
  const instructionMatch = remainingContent.match(/^(?:\*[^\n]*\*|For use in[^\n]*)\n\n/)
  if (instructionMatch) {
    remainingContent = remainingContent.substring(instructionMatch[0].length)
  } else if (remainingContent.startsWith('\n')) {
    // No instruction line, just skip the blank line
    remainingContent = remainingContent.substring(1)
  }
  
  // Find where the description ends
  // Look for: Character count line, next section header, or end of content
  const endPatterns = [
    /\n\*?Character count:/,
    /\n## /,
    /\n### /,
    /\n---/
  ]
  
  let endIndex = remainingContent.length
  for (const pattern of endPatterns) {
    const match = remainingContent.match(pattern)
    if (match && match.index < endIndex) {
      endIndex = match.index
    }
  }
  
  // Extract the description
  let description = remainingContent.substring(0, endIndex).trim()
  
  // Remove any trailing newlines but preserve internal spacing
  description = description.replace(/\n+$/, '')
  
  return description
}
```

### 2. Improved State Management
```javascript
// Watch for page changes with proper cleanup
watch(() => page.value.relativePath, async (newPath, oldPath) => {
  if (isAbilityPage.value && newPath !== oldPath) {
    // Reset ALL state when navigating
    isExpanded.value = false
    activeTab.value = 'edit'
    error.value = ''
    originalContent.value = ''
    editedContent.value = ''
    loading.value = false
    
    // Update ability info for new page
    await nextTick()
    updateAbilityInfo()
    
    if (import.meta.env.DEV) {
      console.log(`Navigated from ${oldPath} to ${newPath}`)
    }
  }
})
```

### 3. Better Error Handling
```javascript
const extendedDescCharCount = computed(() => {
  // Don't compute if no content or still loading
  if (!editedContent.value || loading.value) {
    return 0
  }
  
  try {
    const description = extractExtendedDescription(editedContent.value)
    const count = description.length
    
    // Only log if we're in development mode
    if (import.meta.env.DEV) {
      console.log(`Character count for ${abilityInfo.value.name}: ${count} chars`)
      if (count > 1000) {
        console.warn('Suspiciously high character count. Description:', description.substring(0, 100) + '...')
      }
    }
    
    return count
  } catch (error) {
    console.error('Error computing character count:', error)
    return 0
  }
})
```

## Key Improvements
1. **No more greedy regex** - Uses substring operations to extract exact content
2. **Handles all format variations** - Works with asterisk and non-asterisk instruction lines
3. **Proper state reset** - Clears all state variables on navigation
4. **Development logging** - Helps debug issues in dev mode
5. **Defensive programming** - Catches errors and provides fallbacks

## Files Modified
- `/codex/docs/.vitepress/theme/components/InlineAbilityEditor.vue` - Complete rewrite of character counting logic

## Testing
Test with these abilities to verify all formats work:
1. Water Absorb (ID: 11) - Has instruction line with asterisks
2. Leaf Guard (ID: 102) - Has instruction line without asterisks, includes frontmatter
3. Navigate between multiple abilities rapidly to test state management

## Result
Character counting should now work consistently across all navigation patterns and ability formats.