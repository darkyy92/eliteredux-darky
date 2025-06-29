---
id: 624
name: Snow Song
status: ai-generated
character_count: 299
---

# Snow Song - Ability ID 624

## In-Game Description
"Sound moves receive 1.2x damage boost and Normal sound moves become Ice-type."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Harmonizes battle prowess with icy melodies. Sound-based moves receive a powerful 1.2x damage boost, while Normal-type sound moves are converted to Ice-type, allowing for strategic type coverage. Perfect for Pokemon that rely on vocal attacks to freeze out the competition with enhanced precision.

## Detailed Mechanical Explanation

Snow Song is implemented in `src/abilities.cc` as a dual-effect ability that combines sound move enhancement with type conversion mechanics. The ability inherits its offensive multiplier from Liquid Voice while implementing its own type conversion logic.

### Core Mechanics

1. **Sound Move Boost**: All sound moves receive a 1.2x damage multiplier via `LiquidVoice.onOffensiveMultiplier`
2. **Type Conversion**: Normal-type sound moves are converted to Ice-type moves
3. **Sound Move Detection**: Uses `gBattleMoves[move].flags & FLAG_SOUND` to identify sound moves

### Code Structure
- References `LiquidVoice.onOffensiveMultiplier` for damage calculation
- Implements custom `onMoveType` callback for type conversion
- Requires both Normal typing and sound flag for type change

### Strategic Applications
- Enhances Normal-type sound moves like Hyper Voice, Boomburst, and Round
- Provides Ice typing for STAB or coverage against Grass, Ground, Flying, and Dragon types
- Works synergistically with Refrigerate-like effects but specifically for sound moves
- Particularly effective on Pokemon with natural sound move access

### Battle Interactions
- Sound moves gain both damage boost and type advantage opportunities
- Type conversion occurs before damage calculation
- Compatible with other sound-based abilities and items
- Affected by Soundproof and similar sound-blocking abilities

