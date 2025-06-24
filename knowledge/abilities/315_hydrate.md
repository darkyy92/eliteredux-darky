---
id: 315
name: Hydrate
status: ai-generated
character_count: 296
---

# Hydrate (Ability #315)

## Basic Information
- **ID**: 315
- **Name**: Hydrate
- **Type**: ATE Ability (Type-changing ability)
- **Breakable**: No
- **Implementation**: Uses `ATE_ABILITY(TYPE_WATER)` macro

## In-Game Description
"Normal-type moves become Water and Water gains STAB."

## Extended In-Game Description
Hydrate transforms all Normal-type moves used by the Pokémon into Water-type attacks, gaining a 20% power boost and STAB benefits. This includes physical moves like Tackle and Body Slam, special moves like Swift and Hyper Beam, and status moves. Water-type moves are boosted by rain weather and resisted by Grass/Dragon types. Perfect for versatile Water attackers.

Character count: 296

## Technical Implementation

### Core Mechanism
```cpp
constexpr Ability Hydrate = {
    ATE_ABILITY(TYPE_WATER),
};
```

### ATE_ABILITY Macro Breakdown
```cpp
#define ATE_ABILITY(type)                    \
    .onMoveType = +[](ON_MOVE_TYPE) -> int { \
        CHECK(moveType == TYPE_NORMAL)       \
        *ateBoost = TRUE;                    \
        return type + 1;                     \
    },                                       \
    .onStab = +[](ON_STAB) -> int { return moveType == type; }
```

### Key Functions

1. **Type Conversion** (`onMoveType`):
   - Checks if the move type is Normal
   - Sets `ateBoost` flag to TRUE (enables 20% power boost)
   - Returns `TYPE_WATER + 1` to change move type

2. **STAB Application** (`onStab`):
   - Grants STAB for Water-type moves
   - Works for both converted moves and natural Water moves

## Mechanical Details

### Power Boost
- **Base Effect**: 20% power increase (1.2x multiplier)
- **Applied To**: All Normal-type moves that get converted
- **Stacks With**: Weather, items, other ability boosts

### Type Interactions
- **Water-type advantages**: 2x vs Fire, Ground, Rock
- **Water-type resistances**: 0.5x vs Water, Grass, Dragon
- **Status moves**: Also converted but power boost irrelevant

### Move Examples
**Physical Moves Converted**:
- Tackle → Water Tackle (40 → 48 power + STAB)
- Body Slam → Water Body Slam (85 → 102 power + STAB)
- Double-Edge → Water Double-Edge (120 → 144 power + STAB)

**Special Moves Converted**:
- Swift → Water Swift (60 → 72 power + STAB, never misses)
- Hyper Beam → Water Hyper Beam (150 → 180 power + STAB)
- Tri Attack → Water Tri Attack (80 → 96 power + STAB)

**Status Moves Converted**:
- Thunder Wave → Water Thunder Wave (still causes paralysis)
- Toxic → Water Toxic (still badly poisons)

## Strategic Applications

### Offensive Benefits
1. **Movepool Expansion**: Converts Normal moves into powerful Water attacks
2. **STAB Advantage**: Gains 1.5x STAB on converted moves (stacks with 1.2x conversion boost)
3. **Weather Synergy**: Benefits from rain weather (additional 1.5x boost)
4. **Surprise Factor**: Unexpected Water-type coverage from Normal moves

### Defensive Considerations
1. **Type Chart Changes**: Normal moves now resist Fire/Ground/Rock
2. **New Weaknesses**: Converted moves resisted by Grass/Dragon types
3. **Immunity Loss**: Normal moves no longer immune to Ghost types

### Competitive Use Cases
1. **Rain Teams**: Excellent addition to rain-based strategies
2. **Mixed Attackers**: Benefits both physical and special Normal moves
3. **Utility Pokémon**: Status moves become Water-type for type-specific interactions

## Similar Abilities
- **Pixilate**: Converts Normal → Fairy (same mechanics)
- **Refrigerate**: Converts Normal → Ice (same mechanics)  
- **Aerilate**: Converts Normal → Flying (same mechanics)
- **Galvanize**: Converts Normal → Electric (same mechanics)

## Pokémon That Can Have This Ability
*Note: Specific Pokémon data would need to be extracted from SpeciesList.textproto*

## Battle Interactions

### With Weather
- **Rain**: Converted Water moves gain additional 1.5x boost (permanent rain: 1.2x)
- **Sun**: Converted Water moves receive 0.5x penalty
- **Other Weather**: No additional effects

### With Items
- **Mystic Water**: Boosts converted Water moves by 1.2x
- **Life Orb**: Stacks with conversion boost (1.2x × 1.3x)
- **Choice Items**: Work normally with converted moves

### With Other Abilities
- **Swift Swim**: Doubles Speed in rain (excellent synergy)
- **Water Absorb/Storm Drain**: Immune to converted moves from opponents
- **Protean**: Overrides Hydrate's type conversion

## Coding Notes
- Uses the standard ATE_ABILITY macro for consistent implementation
- `ateBoost` flag enables power calculation bonus
- Type conversion occurs before damage calculation
- STAB check works for both converted and natural Water moves
- Implementation is consistent with other ATE abilities in the codebase

## Version History
- Added in Elite Redux as ability #315
- Part of the expanded ability roster
- Implementation follows standard ATE ability patterns