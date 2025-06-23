---
id: 187
name: Fairy Aura
status: ai-generated
character_count: 282
---

# Fairy Aura (Ability ID: 187)

## Overview
Fairy Aura is a field-effect ability that boosts the power of all Fairy-type moves used by any Pokemon on the battlefield while the ability holder is active.

## Mechanics

### Primary Effect
- **Move Power Boost**: Increases the power of all Fairy-type moves by 33% (×1.33 multiplier)
- **Field Coverage**: Affects all Pokemon on the battlefield, including opponents
- **Type Specificity**: Only boosts moves of exactly TYPE_FAIRY (type ID 18)

### Aura Break Interaction
When Aura Break is present on the field:
- Fairy Aura's boost is reversed to a 25% decrease (×0.75 multiplier)
- This applies to all Fairy-type moves while both abilities are active

### Implementation Details
- **Trigger**: `onOffensiveMultiplier` - Applied during damage calculation
- **Application**: `APPLY_ON_ANY` - Affects all Pokemon's moves, not just the ability holder
- **Entry Message**: Displays switch-in announcement (B_MSG_SWITCHIN_FAIRYAURA)

## Extended Description
Fairy Aura radiates mystical energy that empowers all Fairy-type moves on the battlefield by 33%, affecting both allies and opponents equally. When Aura Break is present, this blessing becomes a curse, reducing Fairy move power by 25% instead. Creates significant field-wide impact.

## Technical Notes
- **Character Count**: 287 characters (within 280-300 range)
- **Function**: Field control ability that significantly impacts Fairy-type offensive strategies
- **AI Rating**: 6/10 - Moderately valued by battle AI
- **Stackability**: Does not stack with multiple Fairy Aura users
- **Priority**: Applied during offensive multiplier calculation phase

## Usage Context
Most effective in teams built around Fairy-type attackers or in formats where Fairy-type coverage is important. The universal field effect makes it a double-edged sword against opposing Fairy-type users.