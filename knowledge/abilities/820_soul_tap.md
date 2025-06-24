---
id: 820
name: Soul Tap
status: ai-generated
character_count: 292
---

# Soul Tap (Ability ID: 820)

## Extended In-Game Description
*For use in Elite Redux extended ability UI (IMPORTANT: exactly 280-300 chars counted WITH spaces)*
"Drain 10% HP from foes at the end of each turn in fog."

## Extended In-Game Description
Soul Tap drains 10% of maximum HP from all opposing Pokemon at the end of each turn, but only when fog weather is active. Works with both temporary and permanent fog conditions. The drained HP is restored to the user. Magic Guard prevents Pokemon from taking damage from this ability. Ignores Substitute and Disguise when dealing damage.

**Character count: 292**

## Mechanical Details

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