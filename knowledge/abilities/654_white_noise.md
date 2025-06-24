---
id: 654
name: White Noise
status: ai-generated
character_count: 291
---

# White Noise

**ID:** 654
**Description:** Static + Rest in Peace.

## Extended Description

White Noise combines Static's paralysis-inducing contact effects with Peaceful Rest's restorative healing properties. When opponents make physical contact, this ability has a 30% chance to paralyze the attacker. Additionally, during fog weather, it heals 1/8 max HP at the end of each turn.

## Implementation Details

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
- Requires the Pokémon to not be at full HP
- Must be able to heal (not blocked by Heal Block, etc.)
- Does not activate on the first turn after switching in