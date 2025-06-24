---
id: 329
name: Scare
status: ai-generated
character_count: 295
---

# Scare (Ability #329)

## Overview
Scare is an intimidation-based ability that lowers the Special Attack of opposing Pokemon upon switching in. It functions as a Special Attack counterpart to the standard Intimidate ability, making it particularly effective against special attackers.

## Mechanics
- **Activation**: On switch-in (entry to battle)
- **Target**: Both opposing Pokemon in double battles, single opponent in single battles
- **Effect**: Lowers Special Attack by 1 stage (-1)
- **Immunity**: Blocked by abilities like Oblivious, Own Tempo, Inner Focus, and Scrappy

## Extended In-Game Description
Upon entering battle, this Pokemon's intimidating presence strikes fear into opposing Pokemon, causing them to lose confidence in their special attacks. The psychological effect reduces their Special Attack stat by one stage, making their special moves considerably weaker throughout the battle.

## Technical Implementation
Scare is implemented using the `UseIntimidateClone` system in the game engine. It references the `gIntimidateCloneData` array with the following configuration:
- `ability`: ABILITY_SCARE
- `numStatsLowered`: 1
- `statsLowered`: {STAT_SPATK, 0, 0}
- `targetBoth`: TRUE

## Pokemon with Scare
Notable Pokemon that can have Scare as a regular or innate ability include:
- Various Ghost-type Pokemon (as part of their intimidating nature)
- Dark-type Pokemon (fitting their menacing presence)
- Some multi-headed Pokemon (where multiple heads create an intimidating sight)
- Legendary and mythical Pokemon (whose presence naturally unnerves opponents)

## Strategic Usage
- **Anti-Special Sweeper**: Excellent for countering special attackers and setup sweepers
- **Pivot Role**: Works well on Pokemon designed to switch in and out frequently
- **Team Support**: Provides immediate value by weakening special threats for the team
- **Psychological Pressure**: Forces opponents to consider switching or using physical moves

## Interactions
- **Bypassed by**: Clear Body, White Smoke, Hyper Cutter (general stat-lowering immunity)
- **Blocked by**: Oblivious, Own Tempo, Inner Focus, Scrappy (intimidation immunity)
- **Stackable**: Can be combined with other stat-lowering entry abilities
- **Trace/Skill Swap**: Can be copied or transferred like other abilities

## Related Abilities
- **Intimidate**: Physical Attack equivalent
- **Fearmonger**: Lowers both Attack and Special Attack
- **Terrify**: Lowers Special Attack by 2 stages
- **Scarecrow**: Combines Scare with Bad Luck effects