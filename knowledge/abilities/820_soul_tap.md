---
id: 820
name: Soul Tap
status: ai-generated
character_count: 275
---

# Soul Tap - Ability ID 820

## In-Game Description
Drain 10% HP from foes at the end of each turn in fog.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Soul Tap drains 10% of max HP from all opposing Pokemon at the end of each turn during fog weather. The drained HP heals the user. Magic Guard blocks the damage. Ignores Substitute and Disguise. Requires active fog to function and affects all living opponents simultaneously.

## Detailed Mechanical Explanation

### Implementation Analysis
- **Weather Requirement**: Only activates during fog weather (`WEATHER_FOG_ANY`)
- **Damage Calculation**: Uses `hpfractiontodamage BS_STACK_2, 10` - drains 1/10th (10%) of target's maximum HP
- **Targeting**: Affects all living opposing Pokemon
- **HP Restoration**: Drained HP is restored to the Soul Tap user via `BattleScript_AbsorbLeech`
- **Magic Guard**: Pokemon with Magic Guard are immune to the damage
- **Bypasses**: Ignores Substitute and Disguise when dealing damage
- **Timing**: Activates at the end of turn phase

### Weather Conditions
- **Temporary Fog**: Created by moves like Fog
- **Permanent Fog**: Set by abilities or other permanent weather effects

### Key Code Elements
- Found in `src/abilities.cc` at line 8398
- Uses `BattleScript_AbilityDrainsHp` for damage and healing
- Weather check: `IsBattlerWeatherAffected(battler, WEATHER_FOG_ANY)`
- Magic Guard check: `IsMagicGuardProtected(target)`