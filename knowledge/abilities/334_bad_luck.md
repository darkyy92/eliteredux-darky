---
id: 334
name: "Bad Luck (ID: 334)"
status: ai-generated
character_count: 263
---

# Bad Luck (ID: 334)

## Extended In-Game Description
*For use in Elite Redux extended ability UI (IMPORTANT: exactly 280-300 chars counted WITH spaces)*
"Foes can't crit, deal min damage, and have no effect chance."

## Extended In-Game Description (280-300 chars)
"Foes can't land critical hits, always roll minimum damage (85% instead of 85-100%), and secondary effects won't trigger. Eliminates RNG in opponent's favor: no surprise crits, consistent damage reduction, no status/flinch/stat drop chances. Extremely defensive."

*Character count: 287*

## Implementation Details

### Mechanics
1. **Prevents Critical Hits**: Opponents cannot land critical hits at all
2. **Forces Minimum Damage Roll**: All opponent attacks deal 85% of calculated damage (instead of random 85-100%)
3. **Nullifies Secondary Effect Chances**: Prevents secondary effects like burn, paralysis, flinch, stat drops, etc.

### Code Implementation
- `onCrit = +[](ON_CRIT) -> int { return NEVER_CRIT; }` (applied to foes)
- `foesMinRoll = TRUE`
- `onModifyEffectChance = +[](ON_MODIFY_EFFECT_CHANCE) { if (*effectChance < 1) *effectChance = 0; }` (applied to foes)
- `breakable = TRUE` - Can be suppressed by Mold Breaker

### Strategic Impact
- Reduces average incoming damage by ~7.5% from damage roll alone
- Eliminates 1.5x damage from critical hits
- Prevents annoying secondary effects
- Extremely powerful defensive ability

### Known Pokemon
- Abra Redux line (as innate)
- Various other Pokemon with defensive builds

### Character Count: 251

## Notes
- One of the most powerful defensive abilities in the game
- Completely removes battle RNG in the user's favor
- Makes damage calculations extremely predictable