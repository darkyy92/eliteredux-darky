---
id: 823
name: Chilling Presence
status: ai-generated
character_count: 292
---

# Chilling Presence - Ability ID 823

## In-Game Description
10BP Icy Wind on entry.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Chilling Presence automatically uses a weakened Icy Wind when the Pokemon enters battle, targeting all opposing Pokemon. The move deals 10 base power Ice-type damage instead of the usual 60, but retains perfect accuracy and guaranteed Speed reduction effects. Useful for slowing fast threats.

## Detailed Mechanical Explanation

### Technical Implementation
- **Implementation**: Uses `UseEntryMove(battler, ability, MOVE_ICY_WIND, 10)` on entry
- **Base Move**: Icy Wind (normally 60 base power, 100% accuracy, hits both opponents)
- **Modified Power**: 10 base power instead of 60
- **Target**: Both opposing Pokemon (MOVE_TARGET_BOTH)
- **Secondary Effect**: 100% chance to lower Speed by 1 stage (retained from original move)
- **Type**: Ice-type damage
- **Accuracy**: 100% (inherited from Icy Wind)

### Strategic Use
- Provides immediate speed control upon entry
- Low damage makes it primarily a utility ability
- Effective for breaking Focus Sashes or dealing chip damage
- Can activate abilities that trigger on taking damage
- Useful for slower Pokemon to gain speed advantage over faster threats