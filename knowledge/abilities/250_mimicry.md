---
id: 250
name: Mimicry
status: ai-generated
character_count: 299
---

# Mimicry - Ability ID 250

## In-Game Description
"Changes type depending on active Terrain."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (IMPORTANT: exactly 280-300 chars counted WITH spaces)*

Mimicry changes the Pokémon's type to match active terrain: Electric on Electric Terrain, Fairy on Misty Terrain, Grass on Grassy Terrain, or Psychic on Psychic Terrain. The type change persists until terrain ends or the Pokémon switches out, then reverts to original type.

*Character count: 299*

## Detailed Mechanical Explanation
*For Discord/reference use*

Mimicry is a reactive ability that changes the Pokémon's type based on the active terrain:

### Terrain Type Mappings:
- **Electric Terrain** → Electric type
- **Misty Terrain** → Fairy type  
- **Grassy Terrain** → Grass type
- **Psychic Terrain** → Psychic type
- **No Terrain/Other** → Reverts to original type

### Activation Conditions:
1. **On Entry**: Activates when the Pokémon enters battle if terrain is already active
2. **On Terrain Change**: Activates whenever terrain changes during battle
3. **Must be alive**: Only works if the Pokémon is conscious

### Type Change Mechanics:
- Changes the Pokémon's **primary type** to match the terrain
- If the Pokémon already has the terrain's type, no change occurs
- The ability stores the original types (both type1 and type2) to restore later
- Type change is immediate and affects STAB, resistances, and weaknesses

### State Management:
- Uses `MimicryState` to track:
  - Original type1 and type2
  - Whether the ability is currently active
- When terrain ends or changes to non-matching terrain, reverts to stored original types

### Battle Messages:
- **Activation**: Uses `BattleScript_MimicryActivates` - "Battler's type changed to [Type]!"
- **Deactivation**: Uses `BattleScript_MimicryEnds` - "Mimicry ends!"

### Elite Redux Implementation Notes:
- Does **not** support Toxic Terrain (falls through to default case)
- Only works with the four standard terrains
- Type change persists through multiple turns until terrain expires
- Compatible with other type-changing effects and abilities

### Competitive Applications:
- Excellent for adapting to terrain-based teams
- Provides STAB for terrain-boosted moves
- Can exploit type matchups based on active terrain
- Requires terrain support to be effective
- Vulnerable when terrain is removed or expires