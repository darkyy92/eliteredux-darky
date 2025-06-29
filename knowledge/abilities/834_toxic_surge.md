---
id: 834
name: Toxic Surge
status: ai-generated
character_count: 296
---

# Toxic Surge - Ability ID 834

## In-Game Description
Sets Toxic Terrain on entry.

## Extended In-Game Description
Toxic Surge automatically sets Toxic Terrain when the Pokemon enters battle. The toxic sludge covers the battlefield for 5 turns (8 with Terrain Extender). Each turn, grounded Pokemon that aren't Poison or Steel-type take damage equal to 1/16 of their max HP. Flying-types and Levitate users avoid damage unless grounded.

## Detailed Mechanical Explanation

### Terrain Activation
- Triggers immediately upon switch-in or battle start
- Replaces any existing terrain
- Duration: 5 turns (8 with Terrain Extender)
- Cannot be prevented by opponent abilities

### Toxic Terrain Effects
1. **End-of-turn Damage**:
   - Deals 1/16 max HP damage to grounded Pokemon
   - Poison and Steel types are immune to damage
   - Flying-types and Levitate users avoid damage unless grounded
   - Magic Guard and abilities with toxicTerrainImmune flag prevent damage

2. **Move Interactions**:
   - Changes Nature Power to a Poison-type move
   - Camouflage turns user into Poison-type

3. **Visual Effects**:
   - Message: "Toxic sludge covers the battlefield!"
   - End message: "The sludge disappeared from the battlefield."

### Implementation Details
- Defined in `src/abilities.cc` as ability ID `ABILITY_TOXIC_SURGE`
- Uses `TryChangeBattleTerrain` with `STATUS_FIELD_TOXIC_TERRAIN` flag
- Damage script: `BattleScript_ToxicTerrainDamages`
- Terrain type for moves: `TYPE_POISON`

### Competitive Analysis

### Strengths
- Provides passive chip damage to most opponents
- Synergizes well with Poison-type teams
- Can pressure switch-ins and wear down walls
- Denies other terrain effects

### Weaknesses
- No damage boost to Poison-type moves (unlike other terrains)
- Many common Pokemon are immune (Steel, Poison, Flying types)
- Can be overwritten by other terrain setters
- Limited offensive utility compared to other surge abilities

### Usage Tips
- Pair with grounding moves (Gravity, Thousand Arrows) to maximize damage
- Use on bulky Poison-types that benefit from chip damage on opponents
- Consider Terrain Extender to maintain field control
- Combine with hazards for increased passive damage

### Similar Abilities
- Electric Surge (sets Electric Terrain)
- Grassy Surge (sets Grassy Terrain)
- Misty Surge (sets Misty Terrain)
- Psychic Surge (sets Psychic Terrain)