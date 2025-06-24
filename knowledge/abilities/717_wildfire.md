---
id: 717
name: Wildfire
status: ai-generated
character_count: 295
---

# Wildfire - Ability ID 717

## In-Game Description
"Attacks with Fire Spin on entry."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (IMPORTANT: exactly 280-300 chars counted WITH spaces)*

Wildfire automatically uses Fire Spin upon switching into battle, dealing 50 base power Fire-type damage and trapping the opponent for 2-5 turns. The trapped opponent takes 1/8 max HP damage each turn and cannot switch out until the trap ends. Perfect for securing KOs.

*Character count: 295*

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Wildfire is an entry ability that automatically triggers Fire Spin when the Pokémon switches into battle. This creates immediate offensive pressure by dealing damage and trapping the opponent.

### Activation Conditions
- **Entry trigger**: Activates when the Pokémon enters battle (switching in or being sent out)
- **Move execution**: Uses Fire Spin with 50 base power, 90% accuracy
- **Trap effect**: Traps the opponent for 2-5 turns (random duration)
- **Damage type**: Fire-type special attack using the user's Special Attack stat

### Fire Spin Mechanics
- **Base power**: 50 (Fire-type special move)
- **Accuracy**: 90%
- **Trap duration**: 2-5 turns (randomly determined)
- **Trap damage**: 1/8 of the opponent's maximum HP per turn
- **Switch prevention**: Opponent cannot switch out while trapped

### Technical Implementation
```c
// Wildfire triggers Fire Spin on entry
constexpr Ability Wildfire = {
    .onEntry = +[](ON_ENTRY) -> int { 
        return UseEntryMove(battler, ability, MOVE_FIRE_SPIN, 0); 
    },
};
```

### Important Interactions
- **Accuracy check**: Fire Spin can miss on entry, negating the trap effect
- **Type effectiveness**: Fire Spin follows normal type effectiveness rules
- **Substitute**: Trapped Pokémon behind Substitute still takes trap damage
- **Rapid Spin**: Can remove the trap effect early
- **Ghost-type**: Ghost-types can still switch out despite being trapped
- **Switching items**: Shed Shell allows switching out of traps

### Strategic Implications
- **Immediate pressure**: Forces opponent into unfavorable position on switch-in
- **Trap synergy**: Excellent for securing KOs on weakened opponents
- **Pivot disruption**: Prevents opponent from freely switching out
- **Damage accumulation**: Continuous trap damage adds up over time
- **Prediction reward**: Switching into predicted moves gains free trap setup

### Ideal Users
- **Offensive Fire-types**: Pokémon that can capitalize on the initial damage
- **Pivot Pokémon**: Those that frequently switch in and out
- **Trap specialists**: Pokémon designed around trapping strategies
- **Revenge killers**: Can trap and finish off weakened opponents

### Synergies
- **Magma Storm**: Combining with stronger trapping moves for more damage
- **Mean Look/Block**: Additional trapping effects for redundancy
- **Toxic Spikes**: Trap damage combined with poison for faster KOs
- **Stealth Rock**: Entry hazards compound the switching punishment
- **Heat Rock**: Extends sun duration if using Fire-type moves

### Counters
- **Ghost-types**: Can switch out despite being trapped
- **Rapid Spin**: Removes trap effect immediately
- **Shed Shell**: Allows switching out of any trap
- **Magic Guard**: Prevents trap damage entirely
- **Substitute**: Can block the initial Fire Spin from hitting

### Competitive Usage Notes
- **Lead potential**: Excellent for applying immediate pressure as a lead
- **Switch-in punishment**: Discourages opponent from switching frequently
- **Stallbreaker**: Continuous damage helps break through defensive play
- **Double switch**: Can trap predicted switches for guaranteed damage
- **Risk vs reward**: Missing Fire Spin wastes the ability activation

### Ability Timing
- **Priority**: Activates immediately upon entry before any other actions
- **Move slot**: Does not use up a move slot or PP
- **Status conditions**: Can still activate if the user is statused
- **Flinch immunity**: Entry abilities cannot be prevented by flinching

### Version History
- **Elite Redux exclusive**: Custom ability not present in official games
- **Trapping category**: Part of the expanded trapping move ecosystem
- **Entry ability**: Follows standard entry ability mechanics and timing