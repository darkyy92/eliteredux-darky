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

## Important Notes

- Never edit files in `docs/abilities/` directly - they are auto-generated
- The inline editor uses regex to parse frontmatter - be careful with complex markdown
- Character counts ALWAYS include spaces (GBA renders spaces as tiles)
- The site uses dark theme by default but supports theme switching