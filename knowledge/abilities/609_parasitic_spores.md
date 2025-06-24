---
id: 609
name: Parasitic Spores
status: ai-generated
character_count: 293
---

# Parasitic Spores

**Ability ID**: 609
**Type**: Regular Ability

**In-Game Description**: "Deals 1/8 HP damage to non-Ghost. Spreads on contact."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

On switch-in, coats the user in parasitic spores. Each turn, affected Pokémon lose 1/8 max HP (Ghost types immune). When using contact moves, spreads spores to the target. Magic Guard prevents damage but not spreading. Spores persist until switch-out. Multiple Pokémon can be infected at once.

*Character count: 293*

## Detailed Mechanical Explanation (Discord/Reference)

**Parasitic Spores** is a multi-faceted ability that both inflicts damage over time and spreads to other Pokémon through contact moves.

### Core Mechanics
1. **Initial Application (On Entry)**: Sets the `parasiticSpores` volatile flag for the battler
2. **Damage Phase**: End-of-turn damage of 1/8 max HP per turn (12.5%)
3. **Spread Mechanism**: Contact moves spread spores to targets
4. **Type Immunity**: Ghost types are completely immune to damage

### Implementation Details
- **Storage**: Uses `gVolatileStructs[battler].parasiticSpores` (1-bit flag)
- **Persistence**: Lasts until Pokémon switches out or faints
- **Message System**: Dedicated battle script messages for entry, spread, and damage

## Trigger Conditions

- **Entry Effect**: Activates when Pokémon with this ability enters battle
- **Damage Trigger**: End-of-turn damage phase
- **Spread Trigger**: When using contact moves against unaffected targets

## Numerical Effects

- **Damage Amount**: 1/8 of max HP per turn (12.5%)
- **Minimum Damage**: 1 HP (if calculated damage would be 0)
- **Spread Condition**: Must make contact and hit successfully

## Interactions

- **Magic Guard**: Completely prevents parasitic spores damage but allows spreading
- **Ghost Types**: Full immunity to damage (can still have spores and spread them)
- **Contact Moves**: Any move with the contact flag can spread spores
- **Switch Out**: Removes parasitic spores effect completely

## Special Cases

- **Turn Order**: Damage occurs between Toxic Waste and generic battler timers
- **Self-Damage**: The original user still takes damage from their own spores
- **Spread Immunity**: Pokémon already affected by spores cannot be affected again
- **Failed Moves**: Spread only occurs if the contact move successfully hits

## Notes

- **Dual Nature**: Both passive damage dealer and contact-based spreader
- **Contagion Effect**: Can create widespread damage in longer battles
- **Contact Punishment**: Discourages physical attackers from making contact
- **Strategic Switching**: Effect removal on switch creates counterplay options
- **Unique Implementation**: Combines volatile effects, contact detection, and type immunity systems