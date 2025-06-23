---
id: 119
name: Frisk
status: ai-generated
character_count: 282
---

# Frisk - Ability ID 119

## In-Game Description
"Checks foes' item and disables their items for two turns."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (IMPORTANT: exactly 280-300 chars counted WITH spaces)*

Upon entering battle, Frisk immediately scans all opposing Pokémon, revealing their held items to you. It then applies Embargo status for two turns, preventing all foes from using their items. This enhanced version provides strong tactical advantage by denying crucial item usage.

*Character count: 282*

## Detailed Mechanical Explanation
*For Discord/reference use*

Frisk is significantly enhanced in Elite Redux compared to vanilla Pokémon games:

**On Entry Effect:**
- Automatically activates when the Pokémon enters battle
- Scans all opposing Pokémon for held items
- If any opponent has an item, displays messages revealing what items they possess
- Simultaneously applies STATUS3_EMBARGO to all opposing Pokémon

**Embargo Effect:**
- Prevents affected Pokémon from using their held items for exactly 2 turns
- Items that normally activate automatically (like Leftovers) are also disabled
- Does not affect items that were already consumed before Frisk activated
- Timer decrements each turn until embargo expires

**Tactical Applications:**
- Ideal for disrupting item-dependent strategies (Choice items, healing items, etc.)
- Provides information advantage by revealing opponent's item choices
- Particularly effective against defensive Pokémon relying on Leftovers/recovery items
- Can shut down setup sweepers using Choice items or status orbs

**Technical Details:**
- Only affects opposing Pokémon (different sides in battle)
- Does not stack - multiple Frisk activations don't extend embargo duration
- Works in both single and double battles
- Embargo timer is stored in gVolatileStructs[battler].embargoTimer