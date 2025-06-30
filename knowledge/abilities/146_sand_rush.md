---
id: 146
name: Sand Rush
status: ai-generated
character_count: 298
---

# Sand Rush - Ability ID 146

## In-Game Description
"This Pokemon's Speed gets a 1.5x boost in a sandstorm."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Sand Rush significantly boosts the Pokemon's Speed by 50% during sandstorm weather, making it exceptionally swift in battle. The ability also provides complete immunity to sandstorm damage, allowing the Pokemon to battle unhindered by harsh weather conditions. Functions under any sandstorm effect.

## Detailed Mechanical Explanation
*For Discord/reference use*

Sand Rush is a weather-dependent ability that provides two key benefits during sandstorm conditions:

**Speed Boost:**
- Increases the Pokemon's Speed stat by 1.5x (50% boost) when sandstorm weather is active
- The boost applies immediately when sandstorm begins and is removed when sandstorm ends
- Stacks multiplicatively with other speed modifiers (items, stat boosts, etc.)
- Works during all forms of sandstorm weather in Elite Redux

**Sandstorm Immunity:**
- The Pokemon takes no damage from sandstorm weather effects
- This immunity is built into the ability (`sandImmune = TRUE` in the code)
- Allows the Pokemon to stay in battle indefinitely during sandstorms without weather damage

**Technical Implementation:**
- Implemented in `abilities.cc` as `SandRush` 
- Uses `onStat` callback to modify Speed when `IsBattlerWeatherAffected(battler, WEATHER_SANDSTORM_ANY)` returns true
- The `WEATHER_SANDSTORM_ANY` check ensures compatibility with all sandstorm variants

**Competitive Usage:**
- Excellent on offensive Pokemon that can set up sandstorm via Sand Stream or moves
- Synergizes well with other Ground, Rock, and Steel-type Pokemon that benefit from sandstorm
- The speed boost can turn normally slow Pokemon into formidable sweepers
- Immunity allows for reliable setup opportunities during sandstorm turns

**Strategic Considerations:**
- Requires sandstorm support from teammates or sandstorm-inducing moves
- Most effective on Pokemon with good offensive stats to take advantage of the speed boost
- Can be countered by weather-changing abilities or moves that override sandstorm