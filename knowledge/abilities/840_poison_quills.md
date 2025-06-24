---
id: 840
name: Poison Quills
status: ai-generated
character_count: 294
---

# Poison Quills

## Short Description
Rough Skin + Poison Point.

## Extended Description
Sharp, venomous barbs cover the user's body, punishing physical contact. When struck by a contact move, the attacker takes damage equal to 1/8 of their maximum HP from the rough quills. Additionally, contact moves have a 30% chance to poison the attacker. This dual defense makes physical attackers think twice before engaging.

## Mechanics

### Components
- **Rough Skin**: Deal 1/8 max HP damage to attackers using contact moves
- **Poison Point**: 30% chance to poison attackers using contact moves

### Key Details
- Both effects trigger on the same contact move
- Damage occurs even if poison fails to inflict
- Poison chance is independent of damage dealt
- Only triggers on moves that make contact
- Magic Guard prevents the damage but not poison chance
- Protective Pads/Long Reach prevent both effects

### Implementation
```c
constexpr Ability PoisonQuills = {
    .onAttacker = PoisonPoint.onAttacker,
    .onDefender = +[](ON_DEFENDER) -> int { 
        return RoughSkin.onDefender(DELEGATE_DEFENDER) | PoisonPoint.onDefender(DELEGATE_DEFENDER); 
    },
};
```

## Strategic Value
- Excellent deterrent against physical attackers
- Chip damage adds up quickly in longer battles
- Poison status provides additional residual damage
- Forces opponents to use special moves or status moves
- Particularly effective on bulky Pokemon

## Notable Interactions
- Both effects can trigger on the same hit
- Substitute blocks both effects
- Multi-hit moves can trigger multiple times
- Protective abilities/items prevent activation
- Poison immunity prevents poison but not the damage