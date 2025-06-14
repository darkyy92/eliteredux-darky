# Adaptability - Ability ID 91

## In-Game Description
"STAB damage is raised to 2x."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Adaptability enhances the Same Type Attack Bonus (STAB) from 1.5x to 2x damage when using moves matching the Pokémon's type. This massive 33% relative increase makes STAB moves hit significantly harder than coverage options. Works with all types including dual-types. Pure offensive power boost.

*Character count: 293*

## Detailed Mechanical Explanation
*For Discord/reference use*

**ADAPTABILITY** is a pure offensive ability that modifies the STAB (Same Type Attack Bonus) multiplier for increased damage output.

### Core Mechanics:
- **Normal STAB**: 1.5x damage multiplier (3/2)
- **Adaptability STAB**: 2.0x damage multiplier (4/2)
- **Relative Increase**: 33.3% more damage on STAB moves
- **Applies To**: All damaging moves that match the Pokémon's type(s)

### Calculation Details:
1. **Type Matching**:
   - Single-type Pokémon: Move must match their type
   - Dual-type Pokémon: Move must match either type
   - Changed types (via Protean, etc): Uses current type(s)

2. **Damage Formula Integration**:
   - Applied during damage calculation after all other modifiers
   - Stacks multiplicatively with other damage modifiers
   - Example: 100 BP STAB move → 150 BP equivalent (normal) → 200 BP equivalent (Adaptability)

### Notable Interactions:
- **Type-changing moves**: If the Pokémon's type changes mid-battle, Adaptability uses the new type(s)
- **Hidden Power**: Gets Adaptability boost if it matches the user's type
- **Multi-hit moves**: Each hit receives the Adaptability boost
- **Variable-type moves**: Moves like Judgment get the boost if they match the user's type

### Technical Implementation:
```c
// In battle_util.c
if (isStab) {
    ON_ABILITY(battler, FALSE, gAbilities[ability].adaptability, return 4)
    return 3;  // Normal STAB is 3/2 (1.5x)
}
```

The ability uses a simple flag system where `adaptability = TRUE` triggers the enhanced STAB calculation.

### Competitive Analysis:
**Strengths**:
- Makes STAB moves overwhelmingly powerful
- Reduces need for coverage moves
- Excellent on Pokémon with strong STAB options
- No setup or conditions required

**Weaknesses**:
- No defensive benefits
- Doesn't help coverage moves
- Less useful on Pokémon with poor STAB options
- Can be predictable (opponents know you'll use STAB)

### Optimal Users:
- Pokémon with high-BP STAB moves
- Mixed attackers who can utilize both physical and special STAB
- Pokémon with good STAB move variety
- Fast sweepers who need immediate power

### Mathematical Example:
Porygon-Z with Adaptability using Tri Attack (80 BP Normal move):
- Base Power: 80
- With normal STAB: 80 × 1.5 = 120 effective BP
- With Adaptability: 80 × 2.0 = 160 effective BP
- Difference: 40 BP increase (equivalent to a 50% power boost over normal STAB)

### Version History:
- Introduced in Gen 4
- No mechanical changes across generations
- Consistent 2.0x STAB multiplier since inception