---
id: 216
name: Dancer
status: ai-generated
character_count: 295
---

# Dancer - Ability ID 216

## In-Game Description
"Copies dance moves used by others."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (IMPORTANT: exactly 280-300 chars counted WITH spaces)*

When any Pokémon on the field uses a dance move, this Pokémon immediately uses the same move. Dance moves include Swords Dance, Dragon Dance, Quiver Dance, Petal Dance, Feather Dance, Teeter Dance, Lunar Dance, Fiery Dance, Revelation Dance, and Aqua Step. Cannot copy if already moved this turn.

*Character count: 295*

## Detailed Mechanical Explanation
*For Discord/reference use*

Dancer is a unique ability that automatically triggers when any Pokémon (ally or opponent) uses a dance move on the battlefield.

### Core Mechanics
- **Automatic Activation**: When any battler uses a move with the FLAG_DANCE flag, Dancer triggers
- **Move Copying**: The Pokémon with Dancer immediately uses the same dance move that was just used
- **Out-of-Turn Usage**: The copied move is executed using UseOutOfTurnAttack, allowing it to occur immediately after the original move
- **No Power Modification**: The copied move uses its normal power and effects (movePower parameter is 0)

### Technical Implementation
```cpp
constexpr Ability Dancer = {
    .onCopyMove = +[](ON_COPY_MOVE) -> int {
        CHECK(IsDance(attacker, move))
        return UseOutOfTurnAttack(battler, target, ability, move, 0);
    },
};
```

The IsDance function checks:
1. If the move has FLAG_DANCE set in its flags
2. OR if the attacker has Taekkyeon ability and the move is not a status move

### Complete List of Dance Moves
1. **Swords Dance** - Raises Attack by 2 stages
2. **Petal Dance** - Physical Grass move that causes confusion after 2-3 turns
3. **Feather Dance** - Lowers target's Attack by 2 stages
4. **Teeter Dance** - Confuses all other Pokémon on the field
5. **Dragon Dance** - Raises Attack and Speed by 1 stage each
6. **Lunar Dance** - User faints, fully heals replacement Pokémon
7. **Quiver Dance** - Raises Special Attack, Special Defense, and Speed by 1 stage each
8. **Fiery Dance** - Special Fire move with 50% chance to raise Special Attack
9. **Revelation Dance** - Changes type to match user's primary type
10. **Aqua Step** - Water-type physical move

### Activation Conditions
- Any Pokémon on the field uses a dance move
- The Dancer Pokémon is still active and able to use moves
- The Dancer Pokémon hasn't already moved this turn (gTurnStructs check prevents infinite loops)

### Interactions with Other Abilities/Mechanics
- **Priority**: Dancer triggers immediately after the original move, before the turn continues
- **Multiple Dancers**: If multiple Pokémon have Dancer, they will all copy the move in turn order
- **Target Selection**: The copied move targets the same target as the original (or self for stat moves)
- **Taekkyeon Synergy**: Pokémon with Taekkyeon make all their non-status moves count as dance moves, creating synergy with Dancer teammates

### Strategic Implications
- **Team Support**: Excellent for copying beneficial stat-boosting dances from allies
- **Punishment**: Can backfire against opponents using setup moves like Dragon Dance or Quiver Dance
- **Double Battles**: Particularly powerful in doubles where ally setup moves can be copied
- **Prediction**: Opponents must be careful about using dance moves against Dancer users

### Example Scenarios
- Ally uses Dragon Dance → Dancer copies Dragon Dance → Both Pokémon get +1 Attack/Speed
- Opponent uses Quiver Dance → Dancer copies Quiver Dance → Dancer gets +1 SpA/SpD/Speed
- Teammate uses Swords Dance → Dancer copies Swords Dance → Dancer gets +2 Attack

### Common Users
In Elite Redux, Dancer is typically found on:
- Pokémon with naturally high offensive stats that benefit from setup moves
- Support Pokémon designed to capitalize on team synergy
- Pokémon with good speed to make use of copied priority moves

### Competitive Usage Notes
- **Team Building**: Build teams with beneficial dance moves to maximize Dancer's utility
- **Positioning**: In doubles, position Dancer users to benefit from ally setup moves
- **Mind Games**: Forces opponents to think twice about using setup moves

### Counters
- **Mold Breaker**: Bypasses Dancer entirely
- **Taunt**: Prevents the use of status dance moves
- **Priority Moves**: Can interrupt before Dancer gets to copy
- **Substitute**: Can block some dance move effects

### Synergies
- **Taekkyeon**: Makes the user's non-status moves count as dance moves for other Dancers
- **Setup Moves**: Any Pokémon with beneficial dance moves
- **Speed Control**: Pokémon that can ensure Dancer moves first after copying

### Version History
- Introduced in Generation VII as a standard ability
- In Elite Redux, maintains original functionality with no modifications
- Works with all dance moves including newer additions like Aqua Step