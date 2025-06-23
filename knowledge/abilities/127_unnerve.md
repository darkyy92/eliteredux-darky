---
id: 127
name: Unnerve
status: ai-generated
character_count: 293
---

# Unnerve (Ability #127)

## Summary
Unnerve prevents opposing Pokémon from consuming their held items during battle. This affects all consumable items including berries, herbs, and other single-use items.

## Effect Details
- **Trigger**: Active as long as a Pokémon with Unnerve is on the field
- **Range**: Affects all opposing Pokémon (both enemies in double battles)
- **Blocked Items**: All consumable held items including:
  - HP restoration berries (Oran Berry, Sitrus Berry, etc.)
  - Status-curing berries (Cheri Berry, Pecha Berry, etc.)
  - Stat-boosting berries (Liechi Berry, Petaya Berry, etc.)
  - Pinch berries (Custap Berry, Micle Berry, etc.)
  - Resistance berries (Occa Berry, Wacan Berry, etc.)
  - Damage-dealing berries (Jaboca Berry, Rowap Berry)
  - Herbs (Mental Herb, Power Herb, White Herb, Mirror Herb)
  - Seeds (Electric Seed, Grassy Seed, etc.)
  - Throat Spray, Booster Energy, and other single-use items

## Interactions
- Does **NOT** prevent consumption of items by moves like Bug Bite, Pluck, or Fling
- Does **NOT** prevent manual item use by trainers in battle
- Does **NOT** affect non-consumable items like Leftovers, Choice items, or Life Orb
- Does **NOT** affect items consumed outside of battle
- Affects Focus Sash - the AI specifically checks for Unnerve when considering Focus Sash
- Affects Eject Button activation
- Multiple Unnerve users don't stack - the effect is binary (on/off)

## Usage Strategy
- **Offensive**: Prevents defensive berries from activating, ensuring KOs on weakened opponents
- **Anti-Setup**: Stops stat-boosting berries from triggering during setup attempts  
- **Focus Sash Counter**: Denies Focus Sash activation, allowing OHKOs on frail Pokémon
- **Double Battle Synergy**: Affects both opponents simultaneously for maximum disruption
- **Pivot Support**: Forces opponents to switch or fight without item safety nets

## AI Behavior
The AI recognizes Unnerve's effect on Focus Sash and factors this into damage calculations. It will:
- Account for Focus Sash being disabled when calculating potential KOs
- Consider pivoting strategies differently when facing Unnerve users
- Recognize that Unnerve negates Focus Sash's protective effect at full HP

## Extended Description (293 characters)
Unnerve prevents all opposing Pokémon from consuming their held items during battle. This powerful disruption ability blocks berries, herbs, seeds, and other consumable items from activating, including crucial defensive tools like Focus Sash and Sitrus Berry. Works in both single and double battles.

## Known Pokémon
Several Pokémon can have Unnerve as one of their abilities, often Dark, Bug, or Flying types that thematically intimidate their opponents.

## Notes
- The ability announces itself when the Pokémon enters battle: "X's Unnerve made the opposing team too nervous to eat berries!"
- Despite the message mentioning berries, it affects all consumable items
- Implemented using a simple flag check that prevents item consumption when an opposing Unnerve user is present