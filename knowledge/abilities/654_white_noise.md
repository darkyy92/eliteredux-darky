---
id: 654
name: White Noise
status: ai-generated
character_count: 357
---

# White Noise - Ability ID 654

## In-Game Description
Static + Peaceful Rest.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

White Noise combines the effects of Static and Peaceful Rest. This Pokemon has a 30% chance to paralyze opponents that make contact with physical attacks, utilizing electrical discharge as a defensive mechanism. Additionally, it heals 1/8 of its maximum HP at the end of each turn during foggy weather conditions, recovering naturally in misty environments.

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