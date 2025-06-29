---
id: 607
name: Tera Shell
status: ai-generated
character_count: 294
---

# Tera Shell - Ability ID 607

## In-Game Description
"Reduces all damage taken by 50% when at full HP."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

At full HP, all attacks deal half damage regardless of type effectiveness. This powerful defensive ability transforms the holder into a formidable wall, requiring strategic chip damage or status conditions to overcome. Unlike other defensive abilities, Tera Shell provides universal protection.

## Detailed Mechanical Explanation

**Implementation Location:** `src/abilities.cc` - TeraShell ability definition

**Core Mechanic:** 
- Reduces all damage taken by 50% when at full HP
- Only affects moves with 1x or greater type effectiveness
- Applied after type effectiveness calculations
- Does not affect moves that would deal 0 damage

### Technical Details
- Triggers on `onAfterTypeEffectiveness` event
- Checks if `*mod >= UQ_4_12(1.0)` (normal effectiveness or better)
- Checks if `BATTLER_MAX_HP(battler)` (at full HP)
- If both conditions met, sets `*mod = UQ_4_12(0.5)` (halves effectiveness)
- Applied to target (defensive ability)
- Ability is breakable by abilities like Mold Breaker

### Strategic Applications
- Provides defensive bulk similar to Multiscale but affects all attacks
- Forces opponents to use chip damage or status moves to break the effect
- Effective against both physical and special attacks
- Synergizes well with recovery moves and healing abilities

