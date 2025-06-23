---
id: 207
name: Surge Surfer
status: ai-generated
character_count: 284
---

# Surge Surfer - Ability ID 207

## In-Game Description
"If Electric Terrain is active, gets a 1.5x Speed boost."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (IMPORTANT: exactly 280-300 chars counted WITH spaces)*

Surge Surfer boosts the Pokémon's Speed by 50% when Electric Terrain is active. Works with any source of Electric Terrain including moves like Electric Terrain, abilities like Electric Surge, and terrain-setting effects. The boost applies immediately and disappears when terrain ends.

*Character count: 284*

## Detailed Mechanical Explanation
*For Discord/reference use*

**Core Mechanics:**
- Provides a 1.5x multiplier to the Speed stat when Electric Terrain is active
- Activates immediately when Electric Terrain becomes active
- Deactivates immediately when Electric Terrain disappears
- Functions as a stat multiplier, not a stage change

**Activation Conditions:**
- Electric Terrain must be active on the battlefield
- The Pokémon with Surge Surfer must be on the field
- Works regardless of which Pokémon or effect created the terrain

**Technical Implementation:**
```cpp
constexpr Ability SurgeSurfer = {
    .onStat =
        +[](ON_STAT) {
            if (statId == STAT_SPEED && IsTerrainActive(STATUS_FIELD_ELECTRIC_TERRAIN)) *stat *= 1.5;
        },
};
```

**Terrain Sources:**
- Electric Terrain (move)
- Electric Surge (ability)
- Terrain Extender (item extends duration)
- Other terrain-setting effects

**Numerical Values:**
- Speed multiplier: 1.5x (50% increase)
- Duration: Depends on terrain source (typically 5 turns, 8 with Terrain Extender)

**Interactions with Other Abilities/Mechanics:**
- Stacks multiplicatively with other speed modifiers (Choice Scarf, speed stages, etc.)
- Does not stack with multiple terrain abilities
- Unaffected by Ability Suppression when terrain is already active
- Works with abilities that extend terrain duration (no direct interaction in Elite Redux)

**Strategic Implications:**
- Excellent for Electric-type teams that naturally set Electric Terrain
- Pairs well with Electric Surge users like Tapu Koko
- Effective for hit-and-run strategies and revenge killing
- Can turn slow Pokémon into dangerous speed threats

**Example Speed Calculations:**
- Base 50 Speed → 75 Speed with Surge Surfer
- Base 80 Speed → 120 Speed with Surge Surfer
- Base 100 Speed → 150 Speed with Surge Surfer
- Stacks with Choice Scarf: Base 80 → 120 (Surge Surfer) → 180 (with Scarf)

**Common Users:**
- Alolan Raichu (signature ability)
- Other Electric-type Pokémon in Elite Redux's expanded ability system

**Competitive Usage Notes:**
- Highly situational but powerful when conditions are met
- Requires team support to set up Electric Terrain
- Most effective in Electric Terrain-focused team compositions
- Can surprise opponents with sudden speed advantage

**Counters:**
- Terrain-changing moves (Grassy Terrain, Misty Terrain, Psychic Terrain)
- Abilities that remove terrain
- Priority moves that bypass speed advantage
- Taunt to prevent terrain setup

**Synergies:**
- Electric Surge (automatic terrain setting)
- Terrain Extender (extends terrain duration)
- Electric-type moves (benefit from terrain's power boost)
- Other terrain-dependent abilities on the same team

**Version History:**
- Introduced in Generation 7 (Sun/Moon)
- Signature ability of Alolan Raichu
- Implementation in Elite Redux follows standard mechanics
- Part of the expanded ability system in Elite Redux