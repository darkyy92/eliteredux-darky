---
id: 670
name: Draco Morale
status: ai-generated
character_count: 298
---

# Draco Morale - Ability ID 670

## In-Game Description
Uses Dragon Cheer on switch-in.

## Extended In-Game Description
Upon entering battle, automatically uses Dragon Cheer, boosting critical hit rate by one stage. Dragon-type Pokemon receive two stages instead. This draconic inspiration immediately prepares the user for more accurate strikes, making it especially powerful for Dragons who gain enhanced benefits.

## Detailed Mechanical Explanation

### Mechanical Details
- **Trigger**: On switch-in (onEntry)
- **Effect**: Automatically uses MOVE_DRAGON_CHEER with no additional parameters
- **Critical Hit Boost**: +1 stage normally, +2 stages for Dragon types
- **Implementation**: Uses UseEntryMove function to execute Dragon Cheer on entry
- **Suppressable**: Yes (breakable ability)
- **AI Consideration**: AI evaluates this as an extra move with MOVE_DRAGON_CHEER

### Competitive Analysis
This ability provides immediate setup potential upon switching in, making it valuable for offensive strategies. Dragon-type Pokemon gain exceptional benefit from the doubled critical hit boost, while other types still receive meaningful offensive support. The ability is particularly useful in scenarios where the Pokemon can safely switch in and immediately threaten high-damage critical hits.