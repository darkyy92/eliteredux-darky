---
id: 826
name: Tender Affection
status: ai-generated
character_count: 294
---

# Tender Affection (Ability #826)

## Quick Description
Cute Charm + Fairy STAB

## Extended In-Game Description
*For use in Elite Redux extended ability UI (IMPORTANT: exactly 280-300 chars counted WITH spaces)*
Combines Cute Charm's 50% chance to infatuate attackers on contact with Same Type Attack Bonus for Fairy-type moves. The infatuation effect triggers when hit by physical contact moves from opposite gender Pokemon. Fairy-type moves gain 1.5x damage multiplier regardless of the user's actual type.

Character count: 294

## Mechanics

### Cute Charm Component
- **Trigger**: When hit by a contact move
- **Effect**: 50% chance to infatuate the attacker
- **Condition**: Attacker must be opposite gender
- **Type**: Passive defensive ability

### Fairy STAB Component
- **Effect**: Grants STAB (1.5x damage) to all Fairy-type moves
- **Condition**: Works even if the Pokemon is not Fairy-type
- **Type**: Offensive damage modifier

## Implementation Details

The ability is implemented in `src/abilities.cc` as:

```cpp
constexpr Ability TenderAffection = {
    ON_EITHER_ABILITY(CuteCharm),
    .onStab = +[](ON_STAB) -> int { return moveType == TYPE_FAIRY; },
};
```

This implementation:
1. Inherits the full Cute Charm functionality for the infatuation effect
2. Adds a custom STAB check that returns true for Fairy-type moves

## Strategic Use

### Offensive Benefits
- Allows non-Fairy types to use Fairy moves with STAB damage
- Particularly useful for Pokemon with good Fairy move coverage
- Enables effective Fairy-type attackers without the defensive weaknesses

### Defensive Benefits
- Deters physical attackers of the opposite gender
- Infatuation can disrupt opponent's strategy
- Works well with bulky Pokemon that can take contact hits

### Synergies
- Pairs well with Pokemon that have diverse movepools including Fairy moves
- Excellent on Pokemon with high Special Attack for moves like Moonblast
- Works with physical Fairy moves like Play Rough for mixed attackers

## Notable Users
This ability is particularly valuable on Pokemon that:
- Have access to strong Fairy moves but aren't Fairy-type
- Need coverage against Dragon, Dark, or Fighting types
- Can benefit from both offensive and defensive utility

## Comparison to Similar Abilities
- **Cute Charm**: Only provides the infatuation effect
- **Pixilate**: Converts Normal moves to Fairy but doesn't affect contact defense
- **Fairy Aura**: Boosts all Fairy moves but lacks defensive utility