---
id: 92
name: Skill Link
status: ai-generated
character_count: 426
---

# Skill Link

## Basic Information
- **Ability ID**: ABILITY_SKILL_LINK (92)
- **Description**: Multi-hit moves always hit the maximum number of times.
- **Type**: Multi-hit modifier ability

## Detailed Mechanics

### Multi-hit Interaction
- Forces all multi-hit moves to hit the maximum number of times (5 hits for most)
- Bypasses the normal random hit distribution (2-5 hits with varying probabilities)
- Without Skill Link, multi-hit moves have:
  - 33.3% chance for 2 hits
  - 33.3% chance for 3 hits
  - 16.7% chance for 4 hits
  - 16.7% chance for 5 hits

### Code Implementation
From `src/battle_script_commands.c`:
```c
if (BattlerHasAbility(gBattlerAttacker, ABILITY_SKILL_LINK, FALSE) || 
    BattlerHasAbility(gBattlerAttacker, ABILITY_KUNOICHI_BLADE, FALSE)) {
    gTurnStructs[gBattlerAttacker].multiHitCounter = 5;
}
```

The ability is checked when setting the multi-hit counter and always sets it to 5.

### Affected Moves
All multi-hit moves that normally hit 2-5 times:
- Bullet Seed
- Rock Blast
- Icicle Spear
- Pin Missile
- Tail Slap
- Arm Thrust
- Barrage
- Bone Rush
- Comet Punch
- Double Slap
- Fury Attack
- Fury Swipes
- Scale Shot
- Spike Cannon
- Water Shuriken

### Damage Calculation
- Each hit is calculated separately with its own damage roll
- Each hit can trigger contact abilities and item effects
- Each hit has its own chance to be a critical hit
- Total damage = sum of all 5 individual hits

### Strategic Benefits
- Guarantees 5 hits, providing consistent damage output
- Effectively multiplies base power by 5 (e.g., Rock Blast: 25 × 5 = 125 power)
- More chances to break through Substitute/Focus Sash
- More chances to trigger secondary effects
- Excellent synergy with King's Rock/Razor Fang for increased flinch chance

### Interaction with Other Abilities/Items
- **Loaded Dice**: No interaction needed as Skill Link already guarantees max hits
- **Kunoichi's Blade**: This ability includes Skill Link's effect plus Technician
- **Choice Band/Specs**: Multiplies damage of each individual hit
- **Life Orb**: Applies recoil after all hits complete
- **King's Rock/Razor Fang**: Each hit has an independent flinch chance

## Extended In-Game Description
Skill Link guarantees that multi-hit moves always strike the maximum five times, turning unreliable attacks into consistent powerhouses. Each hit calculates damage independently with its own critical hit chance and can trigger contact effects. This transforms weak multi-hit moves into formidable options that effectively have 125+ base power while maintaining utility for breaking substitutes and sashes.

Character count: 293

## Usage Tips
- Pair with high Attack/Special Attack stats to maximize damage output
- Effective counter to Focus Sash and Substitute strategies
- Use King's Rock or Razor Fang for ~41% flinch chance (1 - 0.9^5)
- Consider moves' secondary effects that can trigger multiple times
- Remember each hit can be affected by type effectiveness and STAB

## Competitive Analysis
Skill Link transforms otherwise mediocre multi-hit moves into reliable, high-damage options. The guaranteed 5 hits provides both consistent damage and utility, making it especially valuable for breaking through defensive items and abilities. The ability essentially gives access to 100+ base power moves with added benefits like multiple chances for critical hits and secondary effects.

## Known Pokémon with Skill Link
While the codebase doesn't show specific Pokémon assignments, typical users in mainline games include:
- Cloyster (most notable user)
- Cinccino
- Ambipom
- Aipom
- Minccino
- Shellder

## Notes
- The ability flag is implemented as `.skillLink = TRUE` in the abilities system
- No accuracy check bypass for subsequent hits (handled separately in the battle system)
- Triple Kick and Population Bomb (10-hit move) are specifically excluded from needing Skill Link for consistent hits