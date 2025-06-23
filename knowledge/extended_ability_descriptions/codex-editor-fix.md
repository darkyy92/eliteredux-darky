# Codex Editor Fix for Frontmatter Compatibility

## Problem
After adding frontmatter to ability files, the Codex inline editor broke:
- Character count showed 0/300 instead of the actual count
- Total changes count was inaccurate
- This prevented users from submitting edits to GitHub (validation failed)

## Root Cause
The InlineAbilityEditor component was including the YAML frontmatter when:
1. Calculating the extended description character count
2. Computing the diff for change tracking

The regex pattern was looking for the extended description section but couldn't find it properly because the content started with frontmatter.

## Solution
Added a `stripFrontmatter()` helper function that:
- Detects if content starts with `---\n`
- Extracts and removes the YAML frontmatter section
- Returns only the markdown content

Updated all character counting and diff calculations to use the stripped content:
- `extendedDescCharCount` computed property
- `changeCount` computed property
- `diffSummary` and `diffHtml` computed properties
- `getOriginalExtendedDescCharCount()` function

## Files Modified
- `/codex/docs/.vitepress/theme/components/InlineAbilityEditor.vue`

## Result
- Character count now correctly displays (e.g., 289/300)
- Change tracking accurately counts modifications
- Users can successfully edit abilities and submit to GitHub