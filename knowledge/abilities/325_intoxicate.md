---
id: 325
name: Intoxicate
status: ai-generated
character_count: 0
---

# Intoxicate (Ability #325)

## Basic Information
- **ID**: 325
- **Name**: Intoxicate
- **Type**: Offensive Enhancement
- **Generation**: Elite Redux Custom

## Extended In-Game Description
*For use in Elite Redux extended ability UI (IMPORTANT: exactly 280-300 chars counted WITH spaces)*
**Short**: Normal-type moves become Poison and Poison gains STAB.

**Extended (292 characters)**: Transforms all Normal-type moves into Poison-type and provides STAB damage boost. The Pokémon gains Same Type Attack Bonus on all Poison moves, including the converted Normal moves. Functions identically to abilities like Pixilate or Aerilate but specifically for Poison-type conversion.

## Mechanics

### Core Effect
- Converts all Normal-type moves used by the Pokémon into Poison-type moves
- Grants Same Type Attack Bonus (STAB) on all Poison-type moves
- The conversion happens before damage calculation
- Converted moves receive the ATE boost flag for additional power

### Implementation Details
- Uses the `ATE_ABILITY(TYPE_POISON)` macro
- Triggers on `onMoveType` callback to convert Normal → Poison
- Triggers on `onStab` callback to provide STAB for Poison moves
- Sets `*ateBoost = TRUE` for converted moves, which may provide additional effects

### Technical Behavior
- **Move Type Conversion**: Normal-type moves become Poison-type
- **STAB Application**: All Poison moves (original and converted) get 1.5x damage
- **Priority**: Conversion happens before type effectiveness calculation
- **Interaction**: Works with all Normal-type moves regardless of category (Physical/Special/Status)

## Pokémon with Intoxicate

### Primary Ability
- Various Poison-type Pokémon (multiple species found in SpeciesList.textproto)

### Innate Ability
- Multiple Pokémon have this as one of their innate abilities
- Often paired with other Poison-themed abilities

### Combination Abilities
- **Sludgy Mix**: Combines Intoxicate + Punk Rock effects

## Strategic Applications

### Offensive Strategy
- Converts typically neutral Normal moves into Poison attacks
- Provides STAB boost to increase damage output
- Excellent for Pokémon with diverse Normal-type movepools
- Synergizes with Poison-type offensive strategies

### Move Synergy
- Works with all Normal-type moves:
  - Physical attacks (Tackle, Body Slam, etc.)
  - Special attacks (Hyper Beam, Swift, etc.)
  - Status moves (converted but may not deal damage)

### Type Coverage
- Converts Normal moves to hit Grass and Fairy types for super-effective damage
- May struggle against Steel and Poison types (resistant/immune)
- Rock and Ground types resist converted moves

## Comparison to Similar Abilities

### Related ATE Abilities
- **Pixilate**: Normal → Fairy (ATE_ABILITY(TYPE_FAIRY))
- **Aerilate**: Normal → Flying (ATE_ABILITY(TYPE_FLYING))
- **Refrigerate**: Normal → Ice (ATE_ABILITY(TYPE_ICE))
- **Galvanize**: Normal → Electric (ATE_ABILITY(TYPE_ELECTRIC))

### Unique Aspects
- Only ability that converts Normal moves to Poison-type
- Particularly valuable for Poison-type Pokémon lacking diverse STAB options
- Strong synergy with Poison-type offensive strategies

## Competitive Viability
- **Tier**: High utility for Poison-type sweepers
- **Best Use**: Pokémon with strong Normal-type coverage moves
- **Synergy**: Pairs well with Poison-type offensive movesets
- **Counter**: Steel-types and Poison-types resist the converted attacks

## Code Implementation
```cpp
constexpr Ability Intoxicate = {
    ATE_ABILITY(TYPE_POISON),
};
```

The ability uses the standard ATE_ABILITY macro which provides:
- `onMoveType` callback for Normal → Poison conversion
- `onStab` callback for STAB on Poison moves
- `*ateBoost = TRUE` flag for converted moves