# Frontmatter Migration Plan for Extended Ability Descriptions

## Overview
This plan outlines the migration from dual file tracking (progress.md + individual files) to a single source of truth using frontmatter in individual ability markdown files.

## Current State
- **Abilities completed**: Continuously increasing (check progress.md for current count)
- **progress.md**: Manual tracking table with columns for status
- **Individual files**: Content without metadata at `knowledge/abilities/{id}_{name}.md`
- **Codex website**: Displays abilities but no visual review status

## Target State
- **Single source of truth**: Frontmatter in each ability file
- **Generated progress.md**: Auto-built from frontmatter data
- **Visual indicators**: Checkmarks in Codex for reviewed abilities
- **Automated workflows**: Scripts handle all synchronization

## Frontmatter Schema

```yaml
---
id: 1
name: Stench
status: ai-generated  # Options: pending, ai-generated, reviewed
character_count: 285
# Fields added after review:
reviewer: github_username
review_date: 2025-01-14
review_iteration: 1
---
```

## Implementation Steps

### Phase 1: Core Infrastructure

#### 1.1 Update /analyze-ability Slash Command
- Modify to add frontmatter when creating new ability files
- Remove direct progress.md updates
- Keep extended_descriptions.txt update
- Frontmatter fields: id, name, status: "ai-generated", character_count

#### 1.1b Update Batch Analyze Prompt
- Update the frequently-used batch analyze prompt to include frontmatter
- Add frontmatter template to subagent instructions
- Ensure character_count from extended description is included in frontmatter

#### 1.2 Create generate_progress.py Script
```python
# Location: eliteredux-darky/scripts/ability_tools/generate_progress.py
# Function: Read all ability files' frontmatter and generate progress.md
# Features:
#   - Parse YAML frontmatter from all ability files
#   - Generate markdown table with status indicators
#   - Sort by ability ID
#   - Count totals (pending/ai-generated/reviewed)
```

#### 1.3 Update process_github_issues.py
- Modify to update frontmatter instead of progress.md
- Add fields: status: "reviewed", reviewer, review_date, review_iteration
- Increment review_iteration if already reviewed

### Phase 2: Data Migration

#### 2.1 Add Frontmatter to Existing Completed Abilities
- Create migration script to add frontmatter to completed abilities
- Set status: "ai-generated" for all existing ones
- Extract character count from existing files
- Preserve all existing content

### Phase 3: Codex Integration

#### 3.1 Update copy-abilities.js
- Ensure frontmatter is preserved when copying to codex
- No changes needed if using standard file copy

#### 3.2 Create Visual Review Indicators
- Custom Vitepress component for sidebar
- Show ✅ for reviewed abilities
- Use frontmatter data available in Vitepress

#### 3.3 Configure Vitepress Sidebar
- Use createContentLoader to read frontmatter
- Generate sidebar with review status
- Sort abilities by ID with visual indicators

### Phase 4: Automation

#### 4.1 Pre-commit Hook
- Run generate_progress.py before commits
- Ensure progress.md is always up to date
- Use husky or similar for Git hooks

#### 4.2 CI/CD Integration
- GitHub Action to validate frontmatter schema
- Check that progress.md matches frontmatter data
- Fail PR if out of sync

## File Structure

```
eliteredux-darky/
├── knowledge/
│   ├── abilities/
│   │   ├── 1_stench.md (with frontmatter)
│   │   ├── 2_drizzle.md (with frontmatter)
│   │   └── ...
│   └── extended_ability_descriptions/
│       ├── progress.md (GENERATED - DO NOT EDIT)
│       ├── extended_descriptions.txt
│       └── frontmatter-migration-plan.md (this file)
├── scripts/
│   └── ability_tools/
│       ├── generate_progress.py (NEW)
│       ├── process_github_issues.py (UPDATED)
│       └── migrate_frontmatter.py (NEW - one-time use)
└── codex/
    ├── docs/
    │   └── abilities/ (copied with frontmatter)
    └── .vitepress/
        └── theme/
            └── components/
                └── AbilitySidebar.vue (NEW)
```

## Benefits
1. **No sync issues**: Single source of truth
2. **Git-friendly**: Metadata changes tracked with content
3. **Queryable**: Scripts can easily parse frontmatter
4. **Visual feedback**: Instant review status in Codex
5. **Scalable**: Works efficiently for 869 abilities

## Risks & Mitigations
- **Risk**: Forgetting to run generate_progress.py
  - **Mitigation**: Pre-commit hook + CI validation
- **Risk**: Invalid frontmatter breaking Vitepress
  - **Mitigation**: Schema validation in scripts
- **Risk**: Migration errors on existing files
  - **Mitigation**: Backup before migration, test on subset first

## Timeline
- **Week 1**: Update scripts and slash command
- **Week 2**: Migrate existing abilities, test thoroughly
- **Week 3**: Implement Codex visual indicators
- **Week 4**: Add automation and CI/CD

## Success Metrics
- Zero manual progress.md edits needed
- All existing completed abilities migrated successfully
- Visual indicators working in Codex
- Community can see review status instantly
- No sync issues reported

## Notes for Implementation
- Always validate YAML frontmatter before writing
- Character count must include spaces (GBA requirement)
- Keep extended_descriptions.txt for backward compatibility
- Test migration on 5-10 abilities first
- Document the new workflow for contributors

## Pending Questions
1. Should we track multiple reviewers or just the latest?
2. Do we need review comments in frontmatter?
3. Should rejected reviews be tracked differently?
4. Integration with user's frequently-used prompt?

## Implementation Progress

### Completed Tasks ✅
1. **Created generate_progress.py** - Reads frontmatter from ability files and generates progress.md
2. **Created process_github_issues_updated.py** - Modified to update frontmatter instead of directly editing progress.md
3. **Created analyze-ability-updated.md** - Updated slash command to include frontmatter in new ability files
4. **Comprehensive plan document** - This file with all implementation details

### Files Created/Updated
- `/scripts/ability_tools/generate_progress.py` - NEW
- `/scripts/ability_tools/process_github_issues_updated.py` - NEW (updated version)
- `/.claude/commands/analyze-ability.md` - UPDATED (replaced with frontmatter version)

### Remaining Tasks
- Add frontmatter to existing 153+ completed abilities (saved for last)
- Test the full workflow end-to-end

### Recently Completed ✅
- Updated batch analyze prompt with frontmatter requirements - `/batch-analyze-prompt-updated.md`
- Verified Codex copy-abilities.js preserves frontmatter (no changes needed - it copies entire files)
- Created visual review indicators for Vitepress:
  - Updated config.mjs to read frontmatter and show ✅ for reviewed abilities
  - Added gray-matter dependency to package.json
  - Updated custom.css with review indicator styles
  - Created config-update-notes.md with implementation details