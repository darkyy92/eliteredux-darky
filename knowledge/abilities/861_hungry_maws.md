---
id: 861
name: Hungry Maws
status: ai-generated
character_count: 295
---

# Hungry Maws Analysis

## Description
"This Pokémon's bite and jaw moves are boosted by 30%. When KOing opponents with these moves, it heals 50% of its max HP, but only 25% when using other moves."

**Character count: 295**

## Mechanics

### Strong Jaw Component
- Boosts damage of bite/jaw moves by 30% (1.3x multiplier)
- Affects moves with the `FLAG_STRONG_JAW_BOOST` flag
- Enhanced moves include: Bite, Crunch, Thunder Fang, Ice Fang, Fire Fang, Hyper Fang, Super Fang, Poison Fang, Psychic Fangs, Jaw Lock, Bolt Beak, Fishious Rend, and many more

### Jaws of Carnage Component
- Heals when KOing opponents with attacking moves
- **50% HP recovery** when KOing with Strong Jaw boosted moves
- **25% HP recovery** when KOing with non-Strong Jaw moves
- Only triggers on KO by the ability holder (attacker)
- Requires the Pokémon to not be at full HP to activate healing

## Implementation
- Combines `StrongJaw.onOffensiveMultiplier` for damage boost
- Uses `JawsOfCarnage.onBattlerFaints` for healing on KO
- Healing amount determined by whether the finishing move has `FLAG_STRONG_JAW_BOOST`

## Synergy
Perfect combination ability that rewards aggressive play with jaw-based moves, providing both offensive power and sustain for maintaining battle presence.