---
id: 179
name: Grass Pelt
status: ai-generated
character_count: 290
---

# Grass Pelt - Ability ID 179

## In-Game Description
"This Pokémon's Defense gets a 1.5x boost in Grassy Terrain."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (IMPORTANT: exactly 280-300 chars counted WITH spaces)*

Grass Pelt boosts the Pokémon's Defense stat by 50% when Grassy Terrain is active. Works with terrain from moves like Grassy Terrain or abilities like Grassy Surge. The boost applies immediately when terrain becomes active and disappears when terrain ends. Stacks with other Defense boosts.

*Character count: 290*

## Detailed Mechanical Explanation
*For Discord/reference use*

Grass Pelt is a straightforward terrain-based defensive ability that provides a significant boost to Defense when Grassy Terrain is active.

**Core Mechanics:**
- Provides a 1.5x multiplier (50% boost) to the Defense stat when Grassy Terrain is active
- Only affects Defense stat, not other stats
- The boost is applied through the `onStat` callback which modifies the stat calculation directly

**Terrain Interaction:**
- Responds to any source of Grassy Terrain:
  - The move "Grassy Terrain" 
  - Abilities that set Grassy Terrain (like Grassy Surge)
  - Any other effect that creates Grassy Terrain
- Uses `IsBattlerTerrainAffected(battler, STATUS_FIELD_GRASSY_TERRAIN)` to check if the Pokémon is affected by Grassy Terrain
- This means the Pokémon must be grounded to benefit (airborne Pokémon are not terrain-affected unless they have specific abilities)

**Timing and Stacking:**
- The boost applies immediately when Grassy Terrain becomes active
- The boost disappears immediately when Grassy Terrain ends
- Stacks multiplicatively with other Defense modifiers (items, moves, other abilities)
- Does not require the Pokémon to take an action - it's a passive stat modification

**Battle Applications:**
- Excellent for defensive pivots and walls in Grassy Terrain teams
- Pairs well with Pokémon that can set their own Grassy Terrain
- The 1.5x multiplier is substantial enough to meaningfully improve bulk
- Works particularly well on Pokémon with already high Defense stats due to multiplicative scaling

**Limitations:**
- Only works on grounded Pokémon (airborne Pokémon need specific terrain-interaction abilities)
- Dependent on terrain support from team members or moves
- Only affects physical bulk, not special bulk
- Terrain can be overwritten by opposing terrain effects

**Related Abilities:**
- Similar to other terrain-based stat boosters
- Grassy Surge is the most common way to activate this ability
- Seed Sower can also set Grassy Terrain when the Pokémon takes damage
- Flourish provides a different Grassy Terrain bonus (offensive rather than defensive)