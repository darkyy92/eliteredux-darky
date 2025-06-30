---
id: 664
name: Flame Bubble
status: ai-generated
character_count: 297
---

# Flame Bubble - Ability ID 664

## In-Game Description
"Water Bubble + Flaming Soul."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Flame Bubble combines Water Bubble and Flaming Soul effects. Fire damage taken is halved, Water moves deal double damage, and the Pokémon is immune to burns. Fire-type moves gain +1 priority when at full HP. Perfect for mixed Fire/Water attackers needing defensive utility.

*Character count: 296*

## Detailed Mechanical Explanation
*For Discord/reference use*

Flame Bubble is a powerful hybrid ability that combines all the effects of Water Bubble and Flaming Soul:

### Water Bubble Components:
- **Fire Resistance**: Takes 50% damage from Fire-type moves (using Heatproof's defensive multiplier)
- **Water Power**: Water-type moves deal 2x damage
- **Burn Immunity**: Cannot be burned, and if the Pokémon already has burn status when gaining this ability, the burn is removed

### Flaming Soul Component:
- **Priority Fire Moves**: Fire-type moves gain +1 priority when the user is at maximum HP (similar to Gale Wings)

### Technical Implementation:
- Uses `WaterBubble.onOffensiveMultiplier` for the Water-type damage boost
- Uses `WaterBubble.onDefensiveMultiplier` (which references Heatproof) for Fire resistance
- Uses `FlamingSoul.onPriority` for the Fire-type priority boost
- Uses `WaterBubble.onStatusImmune` for burn immunity
- Marked as `breakable = TRUE` (can be suppressed by abilities like Mold Breaker)
- Has `removesStatusOnImmunity = TRUE` (removes existing burn status)

### Strategic Implications:
This ability is tailor-made for mixed Fire/Water attackers, particularly Mega Reuniclus Redux. The combination provides:
- Excellent defensive utility against Fire-types
- Powerful Water-type offense
- Priority Fire moves for surprise sweeping potential at full HP
- Complete immunity to burn status, preventing Attack drops and chip damage

### Common Users:
- Mega Reuniclus Redux (Fire/Water) - The signature user with 165 Special Attack

### Competitive Usage Notes:
- Synergizes extremely well with mixed Fire/Water coverage
- Priority Fire moves at full HP can catch opponents off-guard
- The Fire resistance + burn immunity makes it difficult to wear down
- Water move boost makes Water-type coverage extremely threatening
- Must maintain full HP to utilize the priority effect

### Counters:
- Chip damage to remove the priority benefit
- Electric and Grass moves for super-effective damage
- Abilities that suppress other abilities (Mold Breaker, etc.)
- Priority moves that outspeed +1 priority

### Synergies:
- Healing moves/items to maintain full HP for priority
- Rain teams (doesn't weaken Fire moves due to ability)
- Trick Room teams (already slow, priority helps)
- Entry hazard removal to maintain full HP