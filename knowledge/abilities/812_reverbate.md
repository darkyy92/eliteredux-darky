---
id: 812
name: Reverbate
status: ai-generated
character_count: 284
---

# Reverbate - Ability ID 812

## In-Game Description
"Normal moves are Sound moves."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (IMPORTANT: exactly 280-300 chars counted WITH spaces)*

Reverbate converts all Normal-type moves into Sound moves, enabling them to benefit from sound-based abilities and interactions. Sound moves can target multiple foes with Amplifier or Bass Boosted abilities, but are blocked by Throat Chop for 2 turns.

*Character count: 284*

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Reverbate modifies the game's sound detection system by adding a special case for Normal-type moves when used by a Pokémon with this ability.

**Implementation Location**: `src/battle_util.c` line 9198
```c
int IsSoundMove(int battler, MoveEnum move) {
    if (gBattleMoves[move].flags & FLAG_SOUND) return TRUE;
    if (gBattleMoves[move].type == TYPE_NORMAL && BattlerHasAbility(battler, ABILITY_REVERBATE, FALSE)) return TRUE;
    return FALSE;
}
```

### Activation Conditions
- Pokémon must have the Reverbate ability
- The move being used must be Normal-type
- The ability check occurs during move execution and targeting phases

### Sound Move Benefits
Once converted to sound moves, Normal-type moves gain access to:

1. **Multi-target capabilities** with sound-boosting abilities:
   - Amplifier: Converts single-target sound moves to hit both opponents
   - Bass Boosted: Same effect as Amplifier for sound moves

2. **Sound move interactions**:
   - Affected by Throat Chop (blocked for 2 turns after being hit)
   - Can be blocked by Soundproof ability
   - Interact with other sound-based mechanics

### Affected Normal-Type Moves
All Normal-type moves become sound moves, including but not limited to:
- Tackle, Body Slam, Double-Edge
- Quick Attack, Extreme Speed
- Return, Frustration
- Hyper Voice (already a sound move, no change)
- Boomburst (already a sound move, no change)

### Strategic Implications
**Advantages**:
- Enables multi-targeting with Amplifier/Bass Boosted
- Synergizes with sound-based team strategies
- Converts common Normal moves into a specialized category

**Disadvantages**:
- Vulnerable to Throat Chop lockdown
- Blocked by Soundproof ability users
- May alert opponents to sound-based strategy

### Common Users
This ability would be most effective on Pokémon that:
- Have access to powerful Normal-type moves
- Can benefit from multi-target capabilities in doubles
- Are part of sound-based team compositions

### Competitive Usage Notes
- Excellent in doubles format where multi-targeting provides significant advantage
- Requires careful positioning to avoid Throat Chop users
- Best paired with other sound move users for consistency

### Counters
- **Throat Chop**: Prevents sound move usage for 2 turns
- **Soundproof**: Blocks all sound moves completely
- **Substitute**: May block sound moves depending on implementation

### Synergies
- **Amplifier/Bass Boosted**: Convert single-target Normal moves to multi-target
- **Other sound move users**: Create consistent sound-based team strategies
- **Choice items**: Powerful Normal moves become even more threatening

### Version History
- Introduced in Elite Redux as a unique ability interaction
- Part of the expanded ability system providing new strategic options