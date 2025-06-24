---
id: 830
name: Temporal Rupture (N)
status: ai-generated
character_count: 294
---

# Temporal Rupture (N)

## Basic Information
- **ID**: 830
- **Name**: Temporal Rupture (N)
- **Type**: Innate Ability
- **Description**: Roar of Time is altered drastically.

## Detailed Description

Temporal Rupture is an innate ability possessed by legendary Dragon/Steel-type Pokémon. This ability fundamentally alters how Roar of Time functions. In Elite Redux, Roar of Time already differs from the main series by forcing switches at -6 priority instead of requiring recharge. Temporal Rupture further modifies this move's behavior, though the exact changes remain mysterious and powerful.

**Extended Description** (294 characters):
A legendary power that warps the fabric of time itself when Roar of Time is used. This innate ability fundamentally alters the move's properties, transforming it into something far more devastating than its already-modified form. The exact nature of this temporal distortion remains a closely guarded secret of the ancients.

## Technical Details

### Code Implementation
Located in `src/abilities.cc`:
```cpp
constexpr Ability TemporalRupture = {
    .breakable = TRUE,
};
```

### Properties
- **Breakable**: Yes (can be bypassed by Mold Breaker)
- **Innate**: Yes (cannot be changed or suppressed normally)

### Known Pokémon
This ability is found on legendary Dragon/Steel-type Pokémon with the following innate ability set:
- Temporal Rupture (changeable slot)
- Primal Armor (innate)
- Impenetrable (innate)  
- Power Core (innate)

## Notes
- The specific mechanical changes to Roar of Time are not explicitly defined in the code
- Roar of Time in Elite Redux already has EFFECT_HIT_SWITCH_TARGET with -6 priority
- The "drastic alteration" likely involves additional effects beyond the base switch-forcing mechanic
- This is one of the signature abilities of the most powerful legendary Pokémon in Elite Redux