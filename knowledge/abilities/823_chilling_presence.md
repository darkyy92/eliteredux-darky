---
ability_id: 823
ability_name: "Chilling Presence"
short_description: "10BP Icy Wind on entry."
character_count: 292
---

# Chilling Presence (Ability ID: 823)

## Short Description
10BP Icy Wind on entry.

## Extended Description
Chilling Presence automatically uses a weakened Icy Wind when the Pokémon enters battle, targeting all opposing Pokémon. The move deals 10 base power Ice-type damage instead of the usual 60, but retains perfect accuracy and guaranteed Speed reduction effects. Useful for slowing fast threats.

Character count: 292

## Technical Implementation
- **Implementation**: Uses `UseEntryMove(battler, ability, MOVE_ICY_WIND, 10)` on entry
- **Base Move**: Icy Wind (normally 60 base power, 100% accuracy, hits both opponents)
- **Modified Power**: 10 base power instead of 60
- **Target**: Both opposing Pokémon (MOVE_TARGET_BOTH)
- **Secondary Effect**: 100% chance to lower Speed by 1 stage (retained from original move)
- **Type**: Ice-type damage
- **Accuracy**: 100% (inherited from Icy Wind)

## Strategic Use
- Provides immediate speed control upon entry
- Low damage makes it primarily a utility ability
- Effective for breaking Focus Sashes or dealing chip damage
- Can activate abilities that trigger on taking damage
- Useful for slower Pokémon to gain speed advantage over faster threats