---
id: 822
name: Ominous Shroud
status: ai-generated
character_count: 295
---

# Ominous Shroud (Ability ID: 822)

**Short Description:** Phantom + Shadow Shield.

## Extended In-Game Description
Ominous Shroud grants the Pokémon Ghost typing upon entering battle, even if it wasn't Ghost-type originally. Additionally, when at full HP, the Pokémon takes only 50% damage from all attacking moves. This defensive bonus is lost when the Pokémon's HP drops below maximum, but the Ghost typing remains permanent throughout battle.

**Character count: 295**

## Mechanical Implementation

Ominous Shroud is a combination ability that merges two distinct effects:

### Phantom Component (onEntry)
- **Function:** Adds Ghost type to the Pokémon upon entering battle
- **Implementation:** `AddBattlerType(battler, TYPE_GHOST)`
- **Effect:** The Pokémon gains Ghost typing as a third type (stored in `type3` slot)
- **Persistence:** Remains active throughout the entire battle
- **Interaction:** Only adds Ghost type if the Pokémon doesn't already have it

### Shadow Shield Component (onDefensiveMultiplier)
- **Function:** Reduces incoming damage by 50% when at full HP
- **Implementation:** `if (BATTLER_MAX_HP(battler)) MUL(.5)`
- **Condition:** Only active when the Pokémon is at maximum HP
- **Breakable:** Yes - this defensive bonus can be negated by Mold Breaker-like abilities

## Battle Interactions

### Type Addition Mechanics
1. **Ghost Type Addition:** Immediately upon entering battle, the Pokémon gains Ghost typing
2. **Type Immunities:** Gains immunity to Normal and Fighting moves (standard Ghost-type immunity)
3. **Type Weaknesses:** Becomes weak to Ghost and Dark moves
4. **STAB Bonus:** Can now receive STAB on Ghost-type moves if learned

### Damage Reduction Mechanics
1. **Full HP Requirement:** Must be at exactly maximum HP for damage reduction
2. **All Move Types:** Affects physical, special, and status moves that deal damage
3. **Multiplicative Reduction:** 50% damage reduction applies after type effectiveness calculations
4. **Loss Condition:** Any HP loss removes the defensive bonus until HP is restored to maximum

## Strategic Applications

### Offensive Benefits
- **STAB Ghost Moves:** Enhanced Ghost-type move damage if the Pokémon learns them
- **Type Coverage:** Access to Ghost-type immunities and resistances

### Defensive Benefits
- **Initial Bulk:** Extreme durability on the first hit received
- **Switch-In Safety:** Safer entry against predicted attacks
- **Setup Opportunities:** Can survive strong attacks while setting up

### Counterplay
- **Multi-Hit Moves:** First hit removes damage reduction, subsequent hits deal full damage
- **Residual Damage:** Entry hazards, weather, or status conditions remove the damage reduction
- **Mold Breaker:** Abilities that ignore opponent abilities negate the damage reduction component
- **Ghost/Dark Coverage:** The added Ghost typing creates new weaknesses to exploit

## Related Abilities

- **Phantom:** Provides only the Ghost-type addition component
- **Shadow Shield:** Provides only the damage reduction at full HP component
- **Multiscale:** Similar damage reduction mechanic (Shadow Shield is based on Multiscale)
- **Disguise:** Another defensive ability that prevents damage, but works differently

## Pokémon Distribution

This ability is designed for Pokémon that benefit from both defensive bulk and Ghost-type properties, typically used on bulky setup sweepers or defensive pivots that can leverage the temporary damage reduction.