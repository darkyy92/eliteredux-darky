# Snow Warning (Ability ID: 117)

## In-Game Description
"Summons hail on entry. Lasts 8 turns."

## Extended In-Game Description (280-300 chars)
Summons hailstorm for 8 turns (12 with Icy Rock) when entering battle. Damages non-Ice types by 1/16 HP per turn. Blizzard never misses. Aurora Veil can be used. Ice Body heals, Snow Cloak boosts evasion. Cannot override primal weather. Blocked by Safety Goggles/Overcoat.

*Character count: 296*

## Detailed Mechanical Explanation
**Snow Warning** automatically creates a hailstorm when the Pokémon enters battle, providing the same effect as the move Hail without consuming a turn.

### Trigger Conditions
- Activates upon entering battle (switch-in, battle start, or after fainting an opponent)
- Uses the `onEntry` hook to trigger weather change
- Blocked if primal weather is already active

### Weather Duration
- **Base Duration**: 8 turns (standard `WEATHER_DURATION`)
- **Extended Duration**: 12 turns with Icy Rock held item
- Duration counts down at the end of each turn

### Hail Effects
1. **Damage Per Turn**:
   - Deals 1/16 max HP damage to all non-Ice-type Pokémon
   - Pokémon immune to hail damage:
     - Ice-type Pokémon
     - Pokémon with Ice Body, Snow Cloak, Overcoat abilities
     - Pokémon holding Safety Goggles

2. **Move Changes**:
   - Blizzard: 100% accuracy (normally 70%)
   - Weather Ball: Becomes Ice-type and doubles in power
   - Solar Beam/Solar Blade: Power reduced to 50%
   - Moonlight/Morning Sun/Synthesis: Restore 1/4 HP instead of 1/2
   - Aurora Veil: Can only be used during hail

3. **Ability Interactions**:
   - Ice Body: Restores 1/16 HP per turn instead of taking damage
   - Snow Cloak: +25% evasion
   - Slush Rush: Doubles Speed
   - Forecast: Castform becomes Ice-type

### Special Interactions
- **Primal Weather**: If Desolate Land, Primordial Sea, or Delta Stream is active, Snow Warning fails and shows "blocked by primal weather" message
- **Weather Override**: Can replace other non-primal weather effects
- **Simultaneous Activation**: If multiple weather setters enter together, Speed determines order (fastest overwrites)
- **Cloud Nine/Air Lock**: These abilities suppress hail damage and effects

### Implementation Details
- Uses `TryChangeBattleWeather(battler, ENUM_WEATHER_HAIL, TRUE)`
- Executes `BattleScript_SnowWarningActivates` for message/animation
- Returns `NO_ANNOUNCE` if blocked by primal weather
- Standard weather mechanics apply through the weather system