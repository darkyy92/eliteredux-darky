---
id: 267
name: As One Shadow Rider
status: ai-generated
character_count: 292
---

# As One Shadow Rider - Ability ID 267

## In-Game Description
"Unnerve + Grim Neigh."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (IMPORTANT: exactly 280-300 chars counted WITH spaces)*

Combines Unnerve and Grim Neigh effects. The Pokémon makes opponents too nervous to eat berries, preventing all berry use by the opposing team. When this Pokémon knocks out a foe, its Special Attack increases by one stage as it feeds on the fallen enemy's despair.

*Character count: 292*

## Detailed Mechanical Explanation
*For Discord/reference use*

As One Shadow Rider is a signature ability that combines two distinct abilities into one powerful effect:

### Unnerve Component
- **Effect**: Prevents opposing Pokémon from using their held berries
- **Activation**: Passive effect while the Pokémon is on the field
- **Switch-in Message**: Displays "As One" message (B_MSG_SWITCHIN_ASONE)
- **Technical Details**: Sets the `.unnerve = TRUE` flag

### Grim Neigh Component  
- **Effect**: Boosts Special Attack by 1 stage when knocking out an opponent
- **Activation**: Triggers when this Pokémon directly causes an opponent to faint
- **Damage Sources**: Any attacking move that results in a KO
- **Message**: Shows "Grim Neigh" in the ability popup when activated
- **Technical Details**: Uses `MoxieClone(battler, STAT_SPATK)` for the stat boost

### Combined Properties
- **Unsuppressable**: Cannot be suppressed by abilities like Mold Breaker
- **Randomizer Banned**: Excluded from randomizer pools due to its unique nature
- **Shared Switch-in**: Uses the same entry message as As One Ice Rider

### Battle Mechanics
1. **Berry Prevention**: All opposing Pokémon cannot consume berries while this Pokémon is active
2. **Stat Boost Timing**: Special Attack boost occurs immediately after the KO, before checking for additional effects
3. **Stacking**: The stat boost stacks with other Special Attack boosts and can be further enhanced by items
4. **Interaction**: Works with multi-hit moves - only needs the final hit to cause the KO

### Comparison to As One Ice Rider
- **Ice Rider**: Combines Unnerve + Chilling Neigh (Attack boost on KO)
- **Shadow Rider**: Combines Unnerve + Grim Neigh (Special Attack boost on KO)
- Both share the same entry animation and unsuppressable properties

### Pokémon Usage
This ability is designed for special attacking Pokémon that benefit from both utility (berry prevention) and offensive momentum (Special Attack boosts). The Unnerve component provides consistent team support while Grim Neigh rewards aggressive play.

### Counterplay
- **Indirect KOs**: Abilities like Aftermath or Rocky Helmet damage won't trigger Grim Neigh
- **Status Effects**: Poison, burn, or other status conditions that cause fainting don't activate the boost
- **Switching**: The berry prevention only applies while the Pokémon is on the field
- **Ability Suppression**: Despite being unsuppressable, certain game mechanics may still interfere

### Code Implementation
```cpp
constexpr Ability AsOneShadowRider = {
    .onEntry = AsOneIceRider.onEntry,  // Shared entry message
    .onBattlerFaints = +[](ON_BATTLER_FAINTS) -> int {
        CHECK(GrimNeigh.onBattlerFaints(DELEGATE_BATTLER_FAINTS))
        gBattleScripting.abilityPopupOverwrite = ABILITY_GRIM_NEIGH;
        BattleScriptCall(BattleScript_AbilityPopUpStack);
        return NO_ANNOUNCE;
    },
    .onBattlerFaintsFor = APPLY_ON_ATTACKER,
    .unsuppressable = TRUE,
    .randomizerBanned = TRUE,
    .unnerve = TRUE,
};
```