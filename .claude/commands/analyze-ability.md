Think deeply and perform comprehensive code analysis of a specific ability or innate to understand exactly how it works mechanically.

Steps:
0. **Create Todo List** (Always do this first):
   - Use TodoWrite to plan and track the analysis tasks:
     - Read accumulated system knowledge
     - Find ability ID in proto file  
     - Locate implementation in abilities.cc
     - Analyze ability struct and hooks
     - Check battle integration points
     - Write analysis file
     - Update learnings concisely
     - Update progress tracking

1. **Read accumulated system knowledge**:
   - Read `eliteredux-darky/knowledge/ability-and-innates-learnings.md` to understand patterns and insights
   - This file contains important information about:
     - Common implementation patterns (weather, multi-hit, etc.)
     - Damage multiplier tables (Parental Bond variants)
     - Weather duration constants
     - Code organization insights
   - Use this knowledge to guide your analysis

1. **Find the ability ID**:
   - Search `proto/AbilityList.textproto` for `ABILITY_NAME = number` format
   - Note the ability ID number for the filename

2. **Locate the implementation**:
   - Search `src/abilities.cc` for `constexpr Ability {AbilityName}` struct
   - Look for the ability name in various case formats (IceColdHunter, ICE_COLD_HUNTER, etc.)
   - Check the abilities array at the end of `abilities.cc` for registration

3. **Analyze the ability struct**:
   - Identify which hooks are used (onParentalBond, onModifyDamage, etc.)
   - Note any property flags (hailImmune, sandstormImmune, etc.)
   - Track any CHECK() conditions that determine activation
   - Follow any enum values or special types referenced

4. **Check battle integration**:
   - For multi-hit abilities: 
     - Check `GetParentalBondCount()` in `src/battle_script_commands.c` for hit count
     - Check `GetParentalBondMultiplier()` in `src/battle_util.c` for damage per hit
   - For damage modifiers: Look for the ability in damage calculation functions
   - For special effects: Search for the ability ID in battle event handlers
   - Check `include/abilities.hh` for any related enum definitions

5. **Write analysis file automatically**:
   - Create analysis file in `eliteredux-darky/knowledge/abilities/` without asking for permission
   - Use filename format: `{ability_id}_{ability_name_kebab_case}.md` (e.g., `644_ice_cold_hunter.md`)
   - Include the in-game description from proto file
   - Write TWO versions:
     1. **Extended In-Game Description** (280-300 chars max, continuous text, no line breaks)
        - GBA UI limit: 11 usable lines × 30 chars/line = 330 absolute max
        - Target 280-300 to account for word-wrap
        - Be extremely concise while keeping key mechanics
     2. **Detailed Mechanical Explanation** (Discord-friendly, comprehensive)
   - Be specific about damage percentages, trigger conditions, and interactions
   - Compare to similar abilities (e.g., "unlike Parental Bond which reduces damage")
   - Update `eliteredux-darky/knowledge/ability-and-innates-learnings.md` with system insights:
     - Keep updates concise and focused
     - Check for similar patterns already documented
     - Merge new insights with existing ones rather than duplicating
     - Avoid redundancy - consolidate related information
   - Add to `eliteredux-darky/knowledge/extended_ability_descriptions/extended_descriptions.txt`
   - Update progress in `eliteredux-darky/knowledge/extended_ability_descriptions/progress.md`

**Key files to always check**:
- `proto/AbilityList.textproto` - Ability IDs and data (source of truth)
- `src/abilities.cc` - Main ability implementation
- `src/battle_util.c` - Battle mechanics
- `src/battle_script_commands.c` - Battle effects
- `include/battle.h` - Battle constants and enums
- `include/abilities.hh` - Special enum definitions (NOT ability IDs - those are auto-generated)

**Note**: The ability enum is auto-generated from proto files during compilation, so always check the proto file for ability IDs.

**Common ability patterns**:
- Multi-hit abilities often use `onParentalBond` hook
- Weather abilities check `IsBattlerWeatherAffected(battler, WEATHER_X)`
- Type-based abilities check `moveType == TYPE_X` or `IS_BATTLER_OF_TYPE()`
- Damage modifiers use `onModifyDamage` or similar hooks
- Immunity flags like `hailImmune`, `sandstormImmune` are common

**Important**: Never rely solely on ability descriptions - always verify through actual code implementation. The goal is 100% mechanical accuracy.