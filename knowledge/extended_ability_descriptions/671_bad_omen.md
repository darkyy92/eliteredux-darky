# Bad Omen Analysis
**ID**: 671 (ABILITY_BAD_OMEN)  
**Name**: Bad Omen  
**Current Description**: "Foes min roll. Takes 1/4 damage from crits."

---

## Extended Description (287 characters)
```
Opponents deal minimum damage rolls when attacking. Critical hits against this Pokemon deal only 25% of their normal damage instead of 150-200%. This ability can be suppressed by Mold Breaker and similar effects.
```

## Implementation Status
**PARTIALLY IMPLEMENTED** ⚠️

### Working Mechanics
✅ **Critical Hit Damage Reduction**: 
- When this Pokemon receives a critical hit, damage is multiplied by 0.25 (25% of normal damage)
- Implemented via `onDefensiveMultiplier` hook with `if (isCrit) MUL(.25)`

### Missing Mechanics  
❌ **Minimum Damage Roll**: 
- "Foes min roll" should force opponents to deal 85% damage instead of 85-100% variance
- **Not currently implemented** - requires additional hook

## Code Implementation
```cpp
constexpr Ability BadOmen = {
    .onDefensiveMultiplier =
        +[](ON_DEFENSIVE_MULTIPLIER) {
            if (isCrit) MUL(.25);
        },
    .breakable = TRUE,
};
```

## Technical Details

### Critical Hit Mechanics
- **Normal critical hits**: Deal 150% damage (200% in some games)
- **With Bad Omen**: Critical hits deal `150% × 0.25 = 37.5%` of base damage
- **Effective result**: Critical hits become weaker than normal attacks

### Damage Variance Mechanics (Intended)
- **Normal damage variance**: 85-100% of calculated damage (random roll)
- **With Bad Omen**: Should force opponents to always deal 85% (minimum roll)
- **Implementation needed**: Hook into damage calculation system

### Suppression
- **`.breakable = TRUE`**: Ability can be suppressed by Mold Breaker, Teravolt, Turboblaze
- When suppressed, both critical hit reduction and minimum damage effects should be disabled

## User Questions Answered

### "What's the Acc drop?"
**No accuracy drop exists.** Bad Omen doesn't affect accuracy at all. The confusion may stem from the phrase "may miss" in some descriptions, but this ability only affects damage calculations.

### "Does it mean you take more damage, or you lose 1/4 HP whenever you get crit?"
**You take LESS damage.** Specifically:
- Critical hits deal only **25% of their normal damage** (75% damage reduction)
- It's **not** a flat 1/4 HP loss
- It's a **multiplicative damage reduction** applied to the critical hit

## Competitive Analysis

### Strengths
- **Crit immunity**: Effectively makes critical hits deal less damage than normal attacks
- **Damage consistency**: Forces opponents into minimum damage rolls (when fully implemented)
- **Anti-setup**: Reduces effectiveness of high-crit moves and abilities

### Weaknesses
- **Suppressible**: Mold Breaker variants completely negate the ability
- **Partial implementation**: Missing the "minimum roll" component
- **Situational**: Only helps against specific attack patterns

### Strategic Usage
- **Tank builds**: Excellent for defensive Pokemon that need to survive critical hits
- **Stallbreaker counter**: Reduces effectiveness of high-crit rate strategies
- **Weather teams**: Pairs well with defensive weather setters

## Development Notes
- **Missing implementation**: Damage variance hook needed for "Foes min roll" effect
- **Testing required**: Verify critical hit multiplier works correctly in all scenarios
- **Documentation**: Description could be clearer about mechanics