---
id: 333
name: Sweet Dreams
status: ai-generated
character_count: 282
---

# Sweet Dreams (Ability #333)

## Basic Information
- **Ability ID**: 333
- **Name**: Sweet Dreams
- **Short Description**: Heals 1/8 of max HP every turn if asleep. Immune to Bad Dreams.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (IMPORTANT: exactly 280-300 chars counted WITH spaces)*
Sweet Dreams provides restorative healing while sleeping, regenerating exactly 1/8 of maximum HP at the end of each turn when the Pokémon is asleep or has the Comatose ability. Additionally, it grants complete immunity to Bad Dreams damage, making this a powerful defensive ability.

## Detailed Mechanics

### Healing Effect
- **Trigger**: Activates at the end of each turn
- **Condition**: Pokémon must be asleep (STATUS1_SLEEP) OR have the Comatose ability
- **Healing Amount**: 1/8 of maximum HP (minimum 1 HP if calculation results in 0)
- **Restrictions**: 
  - Does not activate if Pokémon is at maximum HP
  - Requires the Pokémon to be able to heal (checked via `CanBattlerHeal()`)

### Bad Dreams Immunity
- **Complete Protection**: Pokémon with Sweet Dreams are completely immune to Bad Dreams damage
- **Implementation**: The `trygetbaddreamstarget` battle script command specifically checks for Sweet Dreams ability and skips the Pokémon if present
- **Battle Script**: When Bad Dreams attempts to target this Pokémon, it jumps to the "prevented" branch

## Code Implementation

### Core Ability Function
```cpp
constexpr Ability SweetDreams = {
    .onEndTurn = +[](ON_END_TURN) -> int {
        CHECK_NOT(BATTLER_MAX_HP(battler))
        CHECK(CanBattlerHeal(battler))
        CHECK(gBattleMons[battler].status1 & STATUS1_SLEEP || BATTLER_HAS_ABILITY(battler, ABILITY_COMATOSE))

        gBattleMoveDamage = gBattleMons[battler].maxHP / 8;
        if (gBattleMoveDamage == 0) gBattleMoveDamage = 1;
        gBattleMoveDamage *= -1;
        BattleScriptPushCursorAndCallback(BattleScript_SweetDreamsActivates);
        return TRUE;
    },
};
```

### Bad Dreams Immunity Check
```cpp
// In Cmd_trygetbaddreamstarget function
else if (BattlerHasAbility(gBattlerTarget, ABILITY_SWEET_DREAMS, TRUE))
    gBattlescriptCurrInstr = T1_READ_PTR(gBattlescriptCurrInstr + 5);
```

## Ability Interactions

### Synergistic Abilities
- **Comatose**: Sweet Dreams healing triggers when Pokémon has Comatose, even if not actually asleep
- **Peaceful Slumber**: Uses Sweet Dreams as a base effect and adds additional healing (1/16 HP from Self Sufficient)

### Defensive Interactions
- **Bad Dreams**: Complete immunity to Bad Dreams damage while asleep
- **Magic Guard**: Would protect against indirect damage but Sweet Dreams already provides immunity

## Strategic Applications

### Offensive Use
- **Rest Strategy**: Pairs excellently with Rest for sustained healing
- **Sleep Talk**: Can continue attacking while benefiting from healing
- **Comatose Synergy**: Always active healing when paired with Comatose

### Defensive Use
- **Stall Strategy**: Provides consistent healing for defensive Pokemon
- **Bad Dreams Counter**: Direct counter to Bad Dreams strategies
- **Sleep Immunity**: Transforms sleep from a disadvantage into an advantage

## Battle Message
When Sweet Dreams activates, it displays:
- **String ID**: STRINGID_SWEETDREAMSHPUP
- **Animation**: Status animation with health bar update
- **Timing**: Occurs during end-of-turn phase

## Technical Notes
- **Healing Calculation**: Uses standard 1/8 HP calculation with minimum 1 HP guarantee
- **Priority**: Activates during standard end-turn ability phase
- **Substitute**: Healing ignores Substitute status (uses HITMARKER_IGNORE_SUBSTITUTE)
- **Damage Flag**: Uses HITMARKER_PASSIVE_DAMAGE flag for proper damage classification

## Related Abilities
- **Comatose**: Provides permanent sleep status for consistent Sweet Dreams activation
- **Bad Dreams**: Directly countered by Sweet Dreams immunity
- **Peaceful Slumber**: Inherits Sweet Dreams functionality with additional effects
- **Self Sufficient**: Used in combination with Sweet Dreams in Peaceful Slumber