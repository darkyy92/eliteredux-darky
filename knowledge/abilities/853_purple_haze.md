---
id: 853
name: Purple Haze
status: ai-generated
character_count: 290
---

# Purple Haze - Extended Analysis

## Implementation Details

Purple Haze (ID: 853) is a follow-up move ability that triggers after the user successfully uses any move. The ability automatically uses Poison Gas with 20 base power against the same target immediately after the original move resolves.

### Technical Mechanics

**Trigger Condition**: After any move is used by the Pokémon with Purple Haze
**Follow-up Move**: Poison Gas (normally 65 base power, reduced to 20 for this ability)
**Target**: Same as the original move (uses FOLLOWUP_STANDARD targeting)
**Activation**: Uses `UseAttackerFollowUpMove` function with the onAttacker callback

### Poison Gas Properties (When Triggered by Purple Haze)

- **Base Power**: 20 (reduced from normal 65)
- **Type**: Poison
- **Accuracy**: 100%
- **Effect**: 20% chance to poison (this is the effect_chance from Poison Gas, not modified by Purple Haze)
- **Target**: Varies based on original move target
- **Category**: Special
- **Additional**: Super effective against Flying-type Pokémon, hits both opponents in doubles

### Strategic Implications

Purple Haze provides consistent chip damage and poison pressure after every move. The 20% poison chance on the follow-up Poison Gas can accumulate significant passive damage over time. The ability is particularly strong on Pokémon that use non-damaging moves frequently, as it provides offensive presence regardless of the original move's damage output.

## Extended Description (280-300 characters)

After using any move, this Pokémon automatically follows up with a weakened Poison Gas attack that deals 20 base power damage. The poisonous gas has a 20% chance to inflict poison status and is super effective against Flying-types, providing consistent chip damage and battlefield pressure.