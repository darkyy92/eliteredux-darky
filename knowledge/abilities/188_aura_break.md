---
id: 188
name: Aura Break
status: ai-generated
character_count: 298
---

# Aura Break (Ability ID 188)

## Current Description
"Cancels aura abilities and makes them 25% weaker instead."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (IMPORTANT: exactly 280-300 chars counted WITH spaces)*
Reverses aura abilities' effects, causing Dark Aura and Fairy Aura to reduce their respective type moves by 25% instead of boosting them by 33%. Only affects Dark-type and Fairy-type move power boosts. Battle Aura and other aura-named abilities remain unaffected by this field-wide reversal effect.

**Character count: 288** ✓

## Mechanics Analysis

### Core Functionality
- **Field Presence**: Aura Break affects the battlefield while the Pokemon is active
- **Aura Reversal**: Specifically targets Dark Aura and Fairy Aura abilities
- **Damage Modifier**: Changes aura boost from 1.33x to 0.75x (25% reduction)
- **Scope**: Only affects offensive move power, not other aura effects

### Technical Implementation
```cpp
// In Dark Aura and Fairy Aura implementations:
if (IsAbilityOnField(ABILITY_AURA_BREAK))
    MUL(.75);  // 25% reduction
else
    MUL(1.33); // Normal 33% boost
```

### Affected Abilities
1. **Dark Aura (ID 187)**: Dark-type moves become 0.75x power instead of 1.33x
2. **Fairy Aura (ID 186)**: Fairy-type moves become 0.75x power instead of 1.33x

### Unaffected Abilities
- **Battle Aura (ID 490)**: Critical hit boost remains unchanged
- Other abilities with "Aura" in name but different mechanics

## Battle Interactions

### Multi-Pokemon Scenarios
- If multiple Pokemon have Dark/Fairy Aura, Aura Break still applies the reversal
- Aura Break's effect applies to all battlers' moves of the affected types
- Effect persists as long as any Pokemon with Aura Break remains on field

### Stacking Behavior
- Multiple Aura Break abilities don't stack (effect is binary)
- If both boosting aura and Aura Break are present, Aura Break takes precedence

## Strategic Applications

### Offensive Use
- Counter teams heavily reliant on Dark Aura or Fairy Aura strategies
- Punish opponents using Xerneas or Yveltal with their signature abilities
- Create defensive advantage against aura-boosted sweepers

### Defensive Considerations
- Pokemon with Aura Break should avoid using Dark or Fairy moves themselves
- Teammates benefit from the aura reversal effect
- Effective in doubles/multi-battles where aura effects are more common

### Team Synergy
- Pairs well with Pokemon that resist Dark and Fairy types
- Benefits teammates using moves of other types
- Consider as anti-meta pick in aura-heavy environments

## Competitive Viability

### Strengths
- Hard counter to specific meta strategies
- Field-wide effect benefits entire team
- Cannot be easily bypassed once active

### Weaknesses
- Very situational utility
- Useless against teams without Dark/Fairy Aura
- Only available on Zygarde forms
- Self-sabotage if using affected move types

### Usage Recommendations
- **Meta-dependent**: Valuable when Dark/Fairy Aura are common
- **Team Role**: Specialized counter rather than core strategy
- **Format Preference**: More effective in doubles than singles

## Code References
- **Implementation**: `/src/abilities.cc` lines 2013-2016
- **Data**: `/proto/AbilityList.textproto` lines 944-948
- **Battle Logic**: Checked via `IsAbilityOnField()` in aura ability implementations
- **Available on**: Zygarde (all forms) in `/proto/SpeciesList.textproto`