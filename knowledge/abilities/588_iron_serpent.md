---
id: 588
name: Iron Serpent
status: ai-generated
character_count: 300
---

# Iron Serpent

**Type:** Offensive Multiplier  
**ID:** 588  
**Description:** "Ups "supereffective" by 33%."

## Core Mechanics

Iron Serpent boosts the power of super-effective moves by 33% (1.33x multiplier). This ability triggers when the user's attack has a type effectiveness multiplier of 2.0x or higher against the target, applying the damage boost on top of the existing super-effective multiplier for devastating effect.

## Technical Implementation

The ability uses the `onOffensiveMultiplier` callback, sharing the exact same implementation as Winged King. It checks `typeEffectivenessMultiplier >= UQ_4_12(2.0)` and applies `MUL(1.33)` when triggered. The UQ_4_12 format represents fixed-point decimal values with 4 integer bits and 12 fractional bits.

## Notable Users

- **Miraidon** (Innate): The legendary Paradox Pokémon possesses Iron Serpent as one of its three innate abilities alongside Hadron Engine and Dragon's Maw, making it exceptionally powerful with super-effective Electric and Dragon-type moves.