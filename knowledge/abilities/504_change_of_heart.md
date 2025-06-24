---
id: 504
name: Change of Heart
status: ai-generated
character_count: 287
---

# Change of Heart (Ability ID 504)

## Summary
Change of Heart automatically uses Heart Swap upon switching into battle, swapping all stat stage changes between the user and the target opponent.

## Technical Implementation

### Code Location
- **File**: `src/abilities.cc`
- **Function**: `ChangeOfHeart`
- **Implementation**: Uses `UseEntryMove` to execute Heart Swap (MOVE_HEART_SWAP) on switch-in

```cpp
constexpr Ability ChangeOfHeart = {
    .onEntry = +[](ON_ENTRY) -> int { return UseEntryMove(battler, ability, MOVE_HEART_SWAP, 0); },
};
```

### Heart Swap Effect
- **Effect**: EFFECT_HEART_SWAP
- **Target**: Selected opponent
- **Type**: Psychic-type status move
- **PP**: 10
- **Description**: "The user employs its psychic powers to swap stat changes with the target."

### Battle Mechanics
- Swaps all stat stage modifications (+/-6 stages) between user and target
- Uses `Cmd_swapstatstages` command for each stat individually
- Affects Attack, Defense, Special Attack, Special Defense, Speed, Accuracy, and Evasion stages
- Does not affect base stats, only the temporary stage changes

## Pokémon with This Ability

### Manaphy
- **Dex #490** - Seafaring Pokémon
- **Type**: Water
- **Ability Slot**: Innate (always active)
- **Other Abilities**: Seaborne, Power Spot, Healer (changeable)
- **Other Innates**: Parental Bond, High Tide
- **Signature Move**: Learns Heart Swap at level 1

## Strategic Analysis

### Competitive Use
- **Entry Hazard**: Automatically disrupts opponent's setup attempts
- **Stat Swap Utility**: Steals opponent's boosts while giving them your debuffs
- **Forced Activation**: Cannot be disabled or prevented when switching in
- **Surprise Factor**: Catches opponents off-guard who have accumulated stat boosts

### Synergies
- **Parental Bond**: Manaphy's other innate ability doubles certain moves
- **High Tide**: Boosts Water-type moves, enhancing Manaphy's offensive potential
- **Seaborne**: Protects from Water-type moves while on the battlefield

### Counters
- **Clear Smog/Haze**: Resets all stat changes after the swap
- **Substitute**: Blocks the Heart Swap effect
- **Taunt**: Prevents setup moves that create stat changes to swap

## Extended In-Game Description
*Character count: 287*

Change of Heart activates the moment its user switches into battle, automatically swapping all stat stage modifications with the target opponent. This includes boosts and drops to Attack, Defense, Special Attack, Special Defense, Speed, Accuracy, and Evasion. Perfect for disrupting setup sweepers.

## Notes
- Triggers on every switch-in, not just the first entry
- Cannot be suppressed by abilities like Damp or Queenly Majesty
- Bypasses Substitute when used as an entry ability
- AI recognizes this as a valuable disruption tool and scores it highly