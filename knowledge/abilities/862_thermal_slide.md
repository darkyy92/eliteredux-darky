---
id: 862
name: Thermal Slide
status: ai-generated
character_count: 295
---

# Thermal Slide (ID: 862)

## Basic Information
- **Name:** Thermal Slide
- **ID:** 862
- **Short Description:** "Ups speed by 50% in sun or hail."

## Extended Description (295 characters)
Thermal Slide increases the bearer's Speed by 50% when the weather is sunny or hailing. This boost applies to all forms of sun (temporary, permanent, and primal) and hail (temporary and permanent). The speed boost is applied during stat calculations, making it effective immediately when the weather changes.

## Mechanical Implementation

### Code Location
- **File:** `src/abilities.cc`
- **Function:** `ThermalSlide`

### Implementation Details
```cpp
constexpr Ability ThermalSlide = {
    .onStat =
        +[](ON_STAT) {
            if (statId == STAT_SPEED && IsBattlerWeatherAffected(battler, WEATHER_SUN_ANY | WEATHER_HAIL_ANY)) *stat *= 1.5;
        },
};
```

### Weather Conditions
The ability activates under these weather conditions:

**Sun Weather (`WEATHER_SUN_ANY`):**
- Temporary sun (from Sunny Day move)
- Permanent sun (from Drought ability)
- Primal sun (from Desolate Land)

**Hail Weather (`WEATHER_HAIL_ANY`):**
- Temporary hail (from Hail move)
- Permanent hail (from Snow Warning ability)

### Stat Modification
- **Stat Affected:** Speed only
- **Multiplier:** 1.5x (50% increase)
- **Timing:** Applied during stat calculation phase
- **Condition:** Weather must be affecting the battler (not blocked by Utility Umbrella)

## Interactions

### Weather Immunity
The ability respects weather immunity mechanics:
- **Utility Umbrella:** Blocks the effect if the weather is sun or rain
- **Weather Immunity:** Other weather immunity abilities don't affect this ability since it only works in sun/hail

### Stat Calculation
- The speed boost is multiplicative with other stat modifiers
- Applied to the final speed stat, not base speed
- Takes effect immediately when weather changes

## Strategic Applications

### Offensive Usage
- Excellent for fast sweepers that can utilize both sun and hail
- Provides speed control in weather-based teams
- Can outspeed threats that normally outspeed the user

### Defensive Usage
- Helps slower Pokemon escape unfavorable matchups
- Provides speed tier manipulation in weather wars
- Can enable revenge killing opportunities

### Team Synergy
- Works well with weather setters (Drought, Snow Warning)
- Complements both sun and hail team archetypes
- Provides flexible speed control regardless of weather type

## Comparison to Similar Abilities

### Chlorophyll/Swift Swim
- **Thermal Slide:** 50% speed boost in sun OR hail
- **Chlorophyll:** 100% speed boost in sun only
- **Swift Swim:** 100% speed boost in rain only

### Slush Rush
- **Thermal Slide:** 50% speed boost in sun OR hail
- **Slush Rush:** 100% speed boost in hail only

## Notes
- The ability name suggests thermal adaptation, hence effectiveness in both hot (sun) and cold (hail) conditions
- The 50% boost is moderate compared to other weather-based speed abilities but compensated by dual weather activation
- The ability is checked every time stats are calculated, so it activates/deactivates immediately with weather changes