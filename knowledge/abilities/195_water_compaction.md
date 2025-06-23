---
id: 195
name: Water Compaction
status: ai-generated
character_count: 289
---

# Water Compaction Analysis

## Current Implementation
**Ability ID:** 195  
**Current Description:** "Takes 1/2 dmg from Water-type moves. +2 Def when hit by those."

## Mechanics

### Defensive Multiplier
- **Effect:** Takes 0.5x damage from Water-type moves
- **Implementation:** Uses `RESISTANCE(.5)` in `onDefensiveMultiplier`
- **Timing:** Applied during damage calculation

### Stat Boost
- **Effect:** Raises Defense by 2 stages when hit by Water-type moves
- **Implementation:** Uses `SetStatChanger(STAT_DEF, 2)` in `onDefender`
- **Timing:** Triggers after damage is dealt (if any)
- **Requirements:** 
  - Must pass `ShouldApplyOnHitAffect(battler)` check
  - Move must be Water-type
  - Must be able to raise Defense stat (`CanRaiseStat(battler, STAT_DEF)`)

## Key Properties

### Breakability
- **Breakable:** Yes (`breakable = TRUE`)
- Can be suppressed by abilities like Mold Breaker

### Interaction Order
1. Damage reduction applies first (0.5x Water damage)
2. Stat boost triggers after damage calculation
3. Both effects work on the same Water-type move

### Edge Cases
- Works against both damaging and non-damaging Water-type moves
- Stat boost only triggers if the Pokémon can still raise its Defense
- Does not activate if the ability is suppressed

## Battle Applications

### Defensive Strategy
- Excellent counter to Water-type attackers
- Becomes progressively harder to KO with repeated Water attacks
- +2 Defense boost is significant (2 stages = 2x effective Defense)

### Type Synergy
- Particularly effective on Rock, Ground, or Fire-types
- Can turn a weakness into a setup opportunity
- Creates mindgames against mixed Water/other-type attackers

## Code Location
- **Main Implementation:** `/src/abilities.cc` - `WaterCompaction` ability
- **Constants:** `/include/generated/constants/abilities.h` - `ABILITY_WATER_COMPACTION = 195`
- **Description:** `/proto/AbilityList.textproto`