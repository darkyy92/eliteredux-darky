---
id: 139
name: Harvest
status: ai-generated
character_count: 284
---

# Harvest - Ability ID 139

## In-Game Description
"50% chance to recycle a used Berry every turn, 100% in sun."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (IMPORTANT: exactly 280-300 chars counted WITH spaces)*

At the end of each turn, Harvest has a 50% chance to restore any Berry the Pokémon has consumed during battle. In sun weather (including harsh sun), this chance increases to 100%. The ability can restore Berries used by effects like Natural Gift, Fling, or consumed for their effects.

*Character count: 284*

## Detailed Mechanical Explanation

Harvest is an ability that allows Pokémon to potentially recover Berries they have consumed during battle. Here's how it works mechanically:

### Activation Conditions
- Triggers at the end of each turn
- Only activates if the Pokémon has no held item
- Only works for Berries that were consumed during the current battle
- The Berry must have been in the Berry pocket (game internally tracks this)

### Success Rate
- **Normal conditions**: 50% chance to restore the Berry
- **Sun weather**: 100% chance to restore the Berry (includes regular sun and harsh sun)
- The weather check uses `IsBattlerWeatherAffected`, meaning Cloud Nine/Air Lock can prevent the sun bonus

### Berry Sources
Harvest can restore Berries that were consumed through various means:
- Natural consumption (e.g., Oran Berry healing at low HP)
- Moves like Natural Gift or Fling that consume the Berry
- Bug Bite/Pluck when used by the Harvest Pokémon
- Berries consumed due to other abilities or effects

### Important Notes
- The ability tracks the last Berry held by checking `GetUsedHeldItem(battler)`
- It specifically checks that the Pokémon has no current item before attempting restoration
- The restored Berry becomes the Pokémon's held item again, ready for reuse
- This creates potential infinite Berry loops, especially with 100% activation in sun

### Strategic Applications
- Pairs excellently with powerful one-time Berries like Sitrus Berry or stat-boosting Berries
- Sun teams can guarantee Berry recycling for consistent healing or stat boosts
- Works well with Natural Gift strategies for repeated use of the move
- Can be combined with Recycle for additional Berry recovery options

### Code Implementation
The ability uses the `tryrecycleitem` battle script command, which handles the actual Berry restoration logic. The ability checks run after all other end-of-turn effects, ensuring proper interaction with consumed Berries from that turn.