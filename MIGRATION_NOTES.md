# Migration Notes - Submodule Transition

## Important: Script Path Updates Required

### Context
Most AI-related files (`knowledge/`, `plans/`, `scripts/`) have been moved from the main repository to this submodule. This affects how scripts are executed and referenced.

**Important Exception**: The `.claude/` folder must remain in the main repository for slash commands to work. Only `knowledge/`, `plans/`, and `scripts/` are in the submodule.

### Scripts That May Need Updates

1. **Build Scripts**
   - Previously: `./scripts/clean_build.sh`
   - Now: `./eliteredux-darky/scripts/clean_build.sh`

2. **Python Scripts**
   - Previously: `python3 scripts/trainer_tools/script.py`
   - Now: `python3 eliteredux-darky/scripts/trainer_tools/script.py`

3. **Any Script Referencing Other Files**
   - Scripts that reference files in `knowledge/`, `plans/`, or other `scripts/` may need path updates
   - Example: A script looking for `knowledge/abilities/` now needs `eliteredux-darky/knowledge/abilities/`

### Scripts to Review

- `scripts/ability_tools/*.py` - May reference knowledge files
- `scripts/trainer_tools/*.py` - May reference other project files
- `scripts/wiki_tools/*.py` - May reference documentation
- `scripts/find_weather_moves.py` - Check for any file references

### How to Update Scripts

1. **For scripts run from main repo root:**
   - Update internal paths to include `eliteredux-darky/` prefix
   - Example: `open('knowledge/file.md')` → `open('eliteredux-darky/knowledge/file.md')`

2. **For scripts that import from other scripts:**
   - Update import paths if necessary
   - Consider using relative imports within the submodule

3. **For scripts that generate files:**
   - Decide if output should go to main repo or submodule
   - Update output paths accordingly

### Testing After Migration

Always test scripts after the migration to ensure they still work correctly:

```bash
# From main repo root
python3 eliteredux-darky/scripts/your_script.py
```

### Notes
- CLAUDE.md remains in the main repo and has already been updated with new paths
- The .gitignore in the main repo still excludes these directories to prevent accidental commits
- This submodule structure keeps AI development files separate while maintaining functionality