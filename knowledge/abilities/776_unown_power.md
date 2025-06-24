---
id: 776
name: Unown Power
status: ai-generated
character_count: 289
---

# Unown Power - Ability ID 776

## In-Game Description
"Mystic Power + Hidden and Secret Power hit Super-effectively."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (IMPORTANT: exactly 280-300 chars counted WITH spaces)*

Grants STAB to all moves (Mystic Power effect) and makes Hidden Power and Secret Power deal super-effective damage against all targets regardless of type matchups. This ability transforms these variable-type moves into universally effective attacks while providing STAB on every move used.

*Character count: 289*

## Detailed Mechanical Explanation
*For Discord/reference use*

Unown Power is a hybrid ability that combines two distinct effects:

### Mystic Power Component (STAB on All Moves)
- **Effect**: Grants Same Type Attack Bonus (STAB) to ALL moves, regardless of type matching
- **Implementation**: Uses `.onStab = +[](ON_STAB) -> int { return TRUE; }` which always returns TRUE for STAB calculation
- **Benefit**: Every move gets a 1.5x damage multiplier, making the Pokémon extremely versatile offensively

### Super-Effective Hidden/Secret Power Component
- **Effect**: Forces Hidden Power and Secret Power to deal super-effective (2x) damage against all targets
- **Implementation**: Uses `.onAfterTypeEffectiveness` callback that checks if the effectiveness multiplier is less than 2.0x for these specific moves, then forces it to 2.0x
- **Mechanics**: `if (*mod < UQ_4_12(2.0) && (move == MOVE_HIDDEN_POWER || move == MOVE_SECRET_POWER)) *mod = UQ_4_12(2.0);`

### Move Details
- **Hidden Power**: Special move with 80 base power, variable type based on IVs (EFFECT_HIDDEN_POWER)
- **Secret Power**: Physical move with 80 base power, Normal-type with variable effects (EFFECT_HIDDEN_POWER)
- Both moves become universally super-effective (2x) with this ability

### Overall Impact
- **Total Multiplier**: Hidden Power and Secret Power get both STAB (1.5x) AND super-effective (2x) = 3.0x total multiplier
- **All Other Moves**: Get STAB (1.5x) regardless of type
- **Strategic Value**: Transforms Unown into a versatile attacker with guaranteed effectiveness on signature moves

### Pokémon with This Ability
- **Unown (Revelation Form)**: A legendary variant with enhanced stats (138 Attack/Special Attack, 133 Defense/Special Defense)
- **Ability Slot**: Innate ability (always active alongside other abilities)
- **Tier**: Tier 1 legendary Pokémon

### Restrictions
- **Randomizer Banned**: This ability is marked as `randomizerBanned = TRUE`, preventing it from appearing on random Pokémon during randomizer runs
- **Form-Specific**: Only available on the special Revelation form of Unown, not regular Unown forms

This ability effectively makes Unown Revelation a formidable special attacker with guaranteed super-effective coverage through Hidden Power and Secret Power, while maintaining offensive presence with STAB on all other moves.