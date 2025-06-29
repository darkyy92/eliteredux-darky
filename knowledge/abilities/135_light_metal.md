---
id: 135
name: Light Metal
status: ai-generated
character_count: 299
---

# Light Metal - Ability ID 135

## In-Game Description
"Boosts Speed by 1.3x and halves this Pokemon's weight."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (IMPORTANT: exactly 280-300 chars counted WITH spaces)*

Light Metal makes the Pokemon lighter and faster by halving its weight and boosting Speed by 30%. The weight reduction affects weight-based moves like Low Kick, Grass Knot, Heavy Slam, and Heat Crash. Lower weight reduces damage taken from opposing weight moves but also reduces damage dealt by the user's weight moves.

## Detailed Mechanical Explanation
Light Metal provides two distinct benefits:

### Speed Boost
- Increases the Pokemon's Speed stat by 30% (1.3x multiplier)
- This is a direct stat modifier that stacks with other speed modifiers
- Applied continuously as long as the ability is active
- Works similarly to abilities like Chlorophyll but without weather dependency

### Weight Reduction
- Reduces the Pokemon's weight by 50% (halves weight)
- Affects all weight-based move calculations:
  - **Defensive benefit**: Takes less damage from moves like Low Kick, Grass Knot, and Heavy Slam
  - **Offensive drawback**: Deals less damage with the user's own weight-based moves
- The weight modification is applied after species base weight but before held items like Float Stone
- Stacks multiplicatively with other weight modifiers

### Strategic Applications
- Excellent for fast, lightweight Pokemon that want to avoid weight-based attacks
- The Speed boost helps with sweeping strategies
- Particularly useful against Fighting-types that commonly use Low Kick
- Less ideal for Pokemon that rely on their own weight-based moves like Heavy Slam

### Technical Implementation
- Speed boost is handled through the `onStat` hook in abilities.cc
- Weight reduction is handled in `GetBattlerWeight()` function in battle_util.c
- Both effects are passive and always active while the Pokemon has this ability