---
id: 654
name: White Noise
status: ai-generated
character_count: 281
---

# White Noise - Ability ID 654

## In-Game Description
Static + Peaceful Rest.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

White Noise combines Static and Peaceful Rest. Contact moves against this Pokemon have a 30% chance to paralyze the attacker. During fog weather, heals 1/8 max HP at the end of each turn. Both effects work independently - paralysis on contact defense and healing in fog conditions.

## Detailed Mechanical Explanation

### Implementation Details

White Noise is implemented as a composite ability that inherits:
- `onAttacker` and `onDefender` from Static ability
- `onEndTurn` from PeacefulRest ability

### Static Component
- Triggers when opponent makes contact with the user
- 30% chance to inflict paralysis on the attacker
- Only works with moves that make physical contact
- Bypassed by abilities that prevent status conditions

### Peaceful Rest Component  
- Activates during fog weather conditions
- Heals 1/8 of maximum HP at the end of each turn
- Requires the Pokemon to not be at full HP
- Must be able to heal (not blocked by Heal Block, etc.)
- Does not activate on the first turn after switching in