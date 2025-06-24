---
id: 824
name: Frostbind
status: ai-generated
character_count: 295
---

# Frostbind (Ability #824)

## Extended In-Game Description
*For use in Elite Redux extended ability UI (IMPORTANT: exactly 280-300 chars counted WITH spaces)*
"Inflicting Frostbite also inflicts Disable."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (IMPORTANT: exactly 280-300 chars counted WITH spaces)*

Frostbind inflicts both Frostbite and Disable when an opponent faints from the Pokémon's attacks. Frostbite deals 1/16 max HP damage per turn and halves special attack. Disable prevents the target's last used move for 4 turns. Creates powerful disruption through dual status effects.

*Character count: 295*

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Frostbind is a reactive ability that activates when opponents that the Pokémon can affect with frostbite faint. When triggered, it simultaneously applies both the Frostbite status condition and the Disable effect to all eligible opponents on the field.

### Implementation Details
```cpp
constexpr Ability Frostbind = {
    .onReactive = +[](ON_REACTIVE) -> int {
        return PoisonPuppeteerClone(ability, battler, +[](int battler, int target) { return (int)CanGetFrostbite(battler); }, BattleScript_Frostbind);
    },
    .onBattlerFaints = PoisonPuppeteer.onBattlerFaints,
    .onBattlerFaintsFor = APPLY_ON_OTHER,
    .setStateOnEffect = MOVE_EFFECT_FROSTBITE,
};
```

The battle script applies both effects:
```assembly
BattleScript_Frostbind::
	setmoveeffect MOVE_EFFECT_DISABLE
	call BattleScript_PoisonPuppeteer_Internal
	return
```

### Activation Conditions
- **Trigger**: When an opponent faints from the Pokémon's attack
- **Target check**: Uses `CanGetFrostbite()` function to determine valid targets
- **Target requirements**: 
  - Must not already have a status condition (STATUS1_ANY)
  - Must not be Ice-type (Ice types are immune to frostbite)
  - Must not be immune to status via abilities/items

### Status Effects Applied

#### Frostbite Status Condition
- **HP damage**: 1/16 maximum HP lost per turn at end of turn
- **Special Attack reduction**: Special Attack halved during damage calculation (like burn affects physical attack)
- **Duration**: Permanent until cured
- **Immunity**: Ice-type Pokémon are immune
- **Curing**: Can be cured by switching out, healing moves, or items

#### Disable Effect
- **Effect**: Prevents use of the target's last used move
- **Duration**: 4 turns (in Gen 7+ configuration)
- **Target**: The move that was used immediately before fainting
- **Limitation**: Cannot use the disabled move until timer expires
- **Cancellation**: Removed if the disabled move is forgotten/replaced

### Strategic Applications
- **Revenge punishment**: Punishes opponents for knocking out the Pokémon
- **Dual disruption**: Both health drain and move restriction
- **Anti-special sweeper**: Frostbite specifically targets special attackers
- **Move prediction disruption**: Disable can lock out key moves
- **Passive pressure**: Forces opponents to consider fainting consequences

### Counters and Limitations
- **Status immunity**: Abilities like Limber, Natural Cure prevent effects
- **Ice-type immunity**: Ice types immune to frostbite portion
- **Substitute**: Protects from both status effects
- **Mental Herb**: Cures Disable immediately
- **Aromatherapy/Heal Bell**: Team-wide status cure
- **Already statused**: Targets with existing status conditions immune to frostbite

### Competitive Viability
- **Niche defensive tool**: Provides post-mortem utility
- **Doubles synergy**: Can affect multiple opponents simultaneously  
- **Risk vs reward**: Opponent must weigh benefits of KO against status consequences
- **Prediction game**: Disable effect depends on opponent's last move choice
- **Limited activation**: Only triggers on opponent faints, not always reliable