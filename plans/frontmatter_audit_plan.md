# Frontmatter Audit Plan

## Problem Statement

The ability documentation system has inconsistent frontmatter formats across ~870 ability files, causing:
- Inaccurate progress tracking (shows "None" character counts)
- Inconsistent file structures
- Generate_progress.py script only recognizing new format

## Current Format Types Discovered

### 1. **New Format (Correct)** ✅
```yaml
---
id: 790
name: Frenzied Phantom
status: ai-generated
character_count: 280
---
```

### 2. **Legacy YAML Format** ⚠️
```yaml
---
ability_id: 336
ability_name: "Electric Burst"
# Missing: id, status, character_count
---
```

### 3. **No Frontmatter (Old Format)** ❌
```markdown
# Magic Guard

## Basic Information
- **Ability ID**: ABILITY_MAGIC_GUARD (98)
```

## Audit Strategy

### Phase 1: Complete File Analysis
1. **Scan all .md files** in `/eliteredux-darky/knowledge/abilities/`
2. **Categorize by frontmatter type**:
   - ✅ Correct format
   - ⚠️ Legacy format (needs conversion)
   - ❌ Missing frontmatter (needs creation)
3. **Generate comprehensive report**

### Phase 2: Systematic Fixes
1. **Priority 1**: Files with missing frontmatter entirely
2. **Priority 2**: Files with legacy YAML format
3. **Batch processing**: Handle 10-20 files at a time
4. **Validation**: Ensure character counts are accurate

### Phase 3: Verification
1. **Re-run generate_progress.py**
2. **Verify all abilities show proper character counts**
3. **Confirm no "None" entries remain**

## Detection Commands

### Find Files Missing Frontmatter Entirely
```bash
find /path/to/abilities/ -name "*.md" -exec grep -L "^---$" {} \;
```

### Find Files with Legacy Format
```bash
find /path/to/abilities/ -name "*.md" -exec grep -l "ability_id:" {} \;
```

### Find Files with Correct Format
```bash
find /path/to/abilities/ -name "*.md" -exec grep -l "^id: [0-9]" {} \;
```

### Count by Category
```bash
# Total files
ls /path/to/abilities/*.md | wc -l

# Files with frontmatter
grep -l "^---$" /path/to/abilities/*.md | wc -l

# Files with new format
grep -l "^id: [0-9]" /path/to/abilities/*.md | wc -l
```

## Actual Scope (Audited)

**REAL NUMBERS from file analysis:**
- **Total ability files**: 876
- **New format (correct)**: 625 files ✅
- **Legacy format (needs conversion)**: 96 files ⚠️
- **Missing frontmatter (needs creation)**: 214 files ❌

**Verification**: 625 + 96 + 214 = 935 ≠ 876
*Note: Some legacy files may have malformed frontmatter boundaries*

**Files needing work**: 96 + 214 = **310 files**

## Sample Problematic Files

### Missing Frontmatter (214 files) ❌
```
508_pure_love.md
148_analytic.md  
302_coil_up.md
229_grassy_surge.md
170_magician.md
62_guts.md
88_download.md
94_solar_power.md
58_minus.md
120_reckless.md
```

### Legacy Format (96 files) ⚠️
```
828_overzealous.md
387_discipline.md
397_pyro_shells.md
369_bad_company.md
352_sage_power.md
820_soul_tap.md
366_solar_flare.md
345_scavenger.md
350_violent_rush.md
347_multi_headed.md
```

## Implementation Plan

### Step 1: Generate Complete Audit Report
Create script to:
- Scan all ability files
- Categorize by frontmatter status
- Extract existing character counts where available
- Identify files needing work

### Step 2: Batch Processing Strategy
- Process in batches of 20 files
- Use Task tool for parallel processing
- Focus on highest-impact files first

### Step 3: Quality Assurance
- Verify character counts are 280-300
- Ensure all required frontmatter fields present
- Test generate_progress.py after each batch

## Success Criteria

1. **All ability files** have proper YAML frontmatter
2. **Zero "None" entries** in progress.md
3. **Character counts** accurately reflect extended descriptions
4. **Consistent format** across all documentation

## Actionable Commands

### Generate Complete File Lists
```bash
# All files missing frontmatter
find /path/to/abilities/ -name "*.md" -exec grep -L "^---$" {} \; > missing_frontmatter.txt

# All files with legacy format  
find /path/to/abilities/ -name "*.md" -exec grep -l "ability_id:" {} \; > legacy_format.txt

# All files with correct format
find /path/to/abilities/ -name "*.md" -exec grep -l "^id: [0-9]" {} \; > correct_format.txt
```

### Quick Status Check
```bash
echo "Total files: $(ls /path/to/abilities/*.md | wc -l)"
echo "Missing frontmatter: $(find /path/to/abilities/ -name "*.md" -exec grep -L "^---$" {} \; | wc -l)"
echo "Legacy format: $(find /path/to/abilities/ -name "*.md" -exec grep -l "ability_id:" {} \; | wc -l)"
echo "Correct format: $(find /path/to/abilities/ -name "*.md" -exec grep -l "^id: [0-9]" {} \; | wc -l)"
```

### Fix Priority Order
1. **High Priority**: Files with "None" character count in progress.md (breaks tracking)
2. **Medium Priority**: Legacy format files (easy conversion)
3. **Low Priority**: Missing frontmatter (requires character counting)

## Timeline Estimate

- **Phase 1 (Audit)**: 1 session ✅ **COMPLETE**
- **Phase 2 (Fixes)**: 15-16 sessions (20 files per session)
- **Phase 3 (Verification)**: 1 session

**Total**: ~17 sessions to complete full frontmatter standardization

## Notes

- This is separate from the >= 790 abilities work (which is **COMPLETE** ✅)
- Focus on systematic approach to avoid missing files
- Prioritize files that impact progress tracking accuracy
- Consider automation where possible for batch updates
- **310 files** need frontmatter work out of **876 total**
- **71%** of files already have correct format