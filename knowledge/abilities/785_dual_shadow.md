---
id: 785
name: Dual Shadow
status: ai-generated
character_count: 270
---

# Dual Shadow - Ability ID 785

## In-Game Description
"Hunger Switch + Elec and Dark deal 1.35x with 10% recoil."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

This ability combines two effects: it switches between two forms at the end of each turn like Hunger Switch, and boosts Electric and Dark-type moves. When using Electric or Dark-type moves, damage is increased by 35% but the user takes 10% recoil damage from the attack.

## Detailed Mechanical Explanation
*For Discord/reference use*

**Dual Shadow** is a complex ability that merges form-switching mechanics with offensive enhancement:

### Form Switching Component (Hunger Switch)
- At the end of each turn, the Pokemon switches between two forms
- Currently implemented for Morpeko ↔ Morpeko-Hangry transformation
- Does not activate if the Pokemon is transformed via Transform
- Form switching is unsuppressable and cannot be negated by abilities like Neutralizing Gas

### Offensive Enhancement Component
- Electric and Dark-type moves deal 1.35x damage (35% increase)
- This multiplier applies to the base power calculation during damage calculation
- Stacks multiplicatively with other damage modifiers (STAB, type effectiveness, etc.)

### Recoil Mechanic
- When using Electric or Dark-type moves, the user takes recoil damage
- Recoil damage equals 10% of the damage dealt to the target
- Minimum recoil damage is 1 HP (even if calculated recoil would be less)
- Uses normal recoil message formatting in battle

### Technical Implementation Details
- The ability is marked as unsuppressable, meaning it cannot be disabled by Neutralizing Gas or similar effects
- Form switching uses the same logic as the standalone Hunger Switch ability
- Damage multiplier only applies to moves of Electric or Dark type, regardless of the user's typing
- Recoil calculation occurs after damage is dealt and uses the actual damage value

### Strategic Implications
- Provides significant offensive boost for Electric/Dark attackers
- The recoil creates a risk/reward dynamic for using enhanced moves
- Form switching may provide access to different stat distributions or movesets
- Cannot be suppressed, making it a reliable combat ability

### Interactions
- Works with multi-hit moves (recoil calculated per hit)
- Affected by abilities that modify recoil damage (like Rock Head would negate recoil)
- Form switching occurs regardless of whether Electric/Dark moves were used that turn