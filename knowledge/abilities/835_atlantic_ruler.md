---
id: 835
name: Atlantic Ruler
status: ai-generated
character_count: 290
---

# Atlantic Ruler

## Short Description
Aquatic Dweller + Swift Swim.

## Extended Description
Empowers the user with mastery over aquatic environments. Water-type moves gain a 1.5x power boost, allowing for devastating oceanic attacks. During rain, the user's Speed is multiplied by 1.5x, enabling swift underwater maneuvers. This dual enhancement makes the bearer a true ruler of the seas.

## Mechanics

### Components
- **Aquatic Dweller**: Boosts the power of Water-type moves by 1.5x
- **Swift Swim**: Boosts Speed by 1.5x in rain

### Key Details
- Does NOT add Water type (unlike the base Aquatic ability)
- Both effects are always active when conditions are met
- Water move boost applies regardless of weather
- Speed boost only applies during rain weather
- Breakable: Can be suppressed by Mold Breaker and similar abilities

### Implementation
```c
constexpr Ability AtlanticRuler = {
    .onOffensiveMultiplier = AquaticDweller.onOffensiveMultiplier,
    .onStat = SwiftSwim.onStat,
    .breakable = TRUE,
};
```

## Strategic Value
- Excellent on Water-type Pokemon for STAB synergy
- Rain teams benefit from both offensive and speed boosts
- Non-Water types can use this for surprise Water coverage
- Pairs well with Rain Dance or Drizzle teammates

## Notable Interactions
- Stacks with STAB for 2.25x damage on Water moves from Water-types
- Speed boost in rain can help outspeed threats
- Vulnerable to abilities that ignore other abilities
- Both effects function independently - you get the Water boost even without rain