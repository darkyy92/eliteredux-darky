---
id: 103
name: Klutz
status: ai-generated
character_count: 289
---

# Klutz - Ability ID 103

## In-Game Description
"Own held item has no effect. Mega Stones are unaffected."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (IMPORTANT: exactly 280-300 chars counted WITH spaces)*

Klutz disables all held item effects including berries, stat boosts, damage multipliers, and special abilities. Items can still be knocked off or stolen but give no benefits. Item-based moves like Fling fail. Mega Stones bypass this restriction allowing mega evolution despite the ability.

*Character count: 289*

## Detailed Mechanical Explanation

Klutz is an ability that completely negates the effects of held items for the Pokémon that has it. Here's how it works in detail:

### Item Effect Negation
- **All item effects are disabled**: This includes berries (Sitrus, Lum, etc.), Choice items, Life Orb, Leftovers, Focus Sash, and all other held items
- **Items remain equipped**: The Pokémon still holds the item and it appears in battle, but provides no benefits
- **Negative effects also blocked**: Items like Sticky Barb, Black Sludge (on non-Poison types), or Flame Orb deal no damage

### Item Interactions
- **Knock Off**: Can still remove the item and gets the damage bonus for knocking off an item
- **Trick/Switcheroo**: Can still swap items with opponents
- **Thief/Covet**: Can still steal the Pokémon's item
- **Bestow**: Can give the item to another Pokémon
- **Fling**: Cannot use this move as it requires the item's effect to work
- **Natural Gift**: Also fails as it requires berry effects
- **Poltergeist**: The move can still target a Klutz Pokémon holding an item

### Special Exceptions
- **Mega Stones**: The only items that work with Klutz, allowing mega evolution
- **Z-Crystals**: Would theoretically be blocked if they existed in Elite Redux
- **Items consumed**: Berries and other consumable items can still be "consumed" but provide no effect when triggered

### Technical Implementation
The ability is implemented through the `IsItemNegated()` function in battle_util.c, which returns TRUE for any Pokémon with Klutz. This check is used throughout the battle system whenever item effects would normally apply.

### Strategic Implications
- Useful for Pokémon that want to avoid negative item effects (Trick Room teams with Room Service)
- Can be used with Trick/Switcheroo strategies to give opponents useless items
- Protects against opponents trying to give you harmful items
- Synergizes with Fling-immune strategies as the Pokémon cannot use its own item offensively