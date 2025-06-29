---
id: 627
name: Ethereal Rush
status: ai-generated
character_count: 288
---

# Ethereal Rush - Ability ID 627

## In-Game Description
"Boosts Speed by 1.5x in fog weather conditions."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Ethereal Rush grants a potent 1.5x Speed boost in fog weather, enabling swift tactical dominance. This weather-dependent ability transforms slower Pokemon into speed demons, perfect for offensive strategies requiring priority control or sweeping potential in misty battlefield conditions.

## Detailed Mechanical Explanation

Boosts Speed by 1.5x in fog weather conditions. This ability activates when permanent or temporary fog is present on the battlefield, providing a significant speed advantage for swift offensive strategies or priority control.

### Implementation Details
- **Ability ID**: 627 (ABILITY_ETHEREAL_RUSH)
- **Code Location**: `src/abilities.cc` - EtherealRush constexpr
- **Weather Check**: Uses `IsBattlerWeatherAffected(battler, WEATHER_FOG_ANY)`
- **Speed Multiplier**: 1.5x when fog conditions are active
- **Fog Types**: Both permanent (WEATHER_FOG_PERMANENT) and temporary (WEATHER_FOG_TEMPORARY) fog

### Strategic Applications
- **Speed Control**: Outspeeds normally faster opponents in fog
- **Weather Teams**: Synergizes with fog-setting moves or abilities
- **Priority Moves**: Enhanced speed can make priority moves unnecessary
- **Offensive Sweeping**: Enables powerful sweeping potential under fog conditions

### Mechanics Analysis
The ability modifies the Speed stat directly through the `onStat` callback when:
1. The stat being calculated is STAT_SPEED
2. The battler is affected by any fog weather condition
3. Applies a 1.5x multiplier to the base speed calculation

