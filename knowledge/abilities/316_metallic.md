---
ability_id: 316
ability_name: "Metallic"
short_description: "Adds Steel type to itself."
extended_description: "Metallic adds Steel as a third type upon entry, granting Steel resistances and immunities while preserving original typing. Provides defensive utility without losing STAB. Particularly effective for frail Pokemon seeking defensive coverage while maintaining offensive versatility and type matchups."
character_count: 298
implementation_file: "src/abilities.cc"
trigger: "onEntry"
category: "Type Addition"
breakable: false
---

# Metallic (Ability #316)

## Overview
Metallic is a defensive utility ability that grants the holder an additional Steel typing upon switching into battle. This creates a triple-type Pokémon, combining the defensive benefits of Steel typing with the offensive capabilities of the Pokémon's original dual typing.

## Basic Information
- **ID**: 316 (ABILITY_METALLIC)
- **Name**: Metallic
- **Short Description**: "Adds Steel type to itself."
- **Category**: Type Addition Ability
- **Breakable**: No
- **Trigger**: On Entry (when Pokémon switches in)

## Extended Description
Metallic adds Steel as a third type upon entry, granting Steel resistances and immunities while preserving original typing. Provides defensive utility without losing STAB. Particularly effective for frail Pokemon seeking defensive coverage while maintaining offensive versatility and type matchups.

**Character count: 298**

## Mechanics

### Core Functionality
```cpp
constexpr Ability Metallic = {
    .onEntry = +[](ON_ENTRY) -> int { return AddBattlerType(battler, TYPE_STEEL); },
};
```

### How It Works
1. **Activation**: Triggers automatically when the Pokémon enters battle (switching in)
2. **Type Addition**: Uses the `AddBattlerType(battler, TYPE_STEEL)` function
3. **Storage**: The Steel type is stored in `gBattleMons[battler].type3`
4. **Check**: Only activates if the Pokémon doesn't already have Steel typing (`CHECK_NOT(IS_BATTLER_OF_TYPE(battler, type))`)
5. **Message**: Displays battle message about gaining the Steel type

### Type System Integration
- **Triple Typing**: Creates a Pokémon with three types (original two + Steel)
- **Preservation**: Original typing remains unchanged (type1 and type2 intact)
- **STAB**: Retains Same Type Attack Bonus for original moves
- **Resistances**: Gains all Steel-type resistances and immunities
- **Weaknesses**: Gains Steel-type weaknesses (Fire, Fighting, Ground)

## Steel Type Benefits

### Resistances (0.5x damage)
- Normal
- Flying  
- Rock
- Bug
- Steel
- Grass
- Psychic
- Ice
- Dragon
- Fairy

### Immunity (0x damage)
- Poison (both damage and status)

### Weaknesses (2x damage)
- Fire
- Fighting  
- Ground

## Strategic Applications

### Defensive Utility
- **Frail Attackers**: Provides defensive bulk to glass cannon Pokémon
- **Status Immunity**: Complete immunity to poison damage and poisoning
- **Resistances**: Significant damage reduction from 10 common types
- **Typing Coverage**: Shores up defensive weaknesses without losing offensive options

### Offensive Preservation  
- **STAB Retention**: Maintains 1.5x damage bonus for original typing moves
- **Coverage Moves**: Original typing determines move effectiveness calculations
- **Versatility**: Triple typing provides unique resistance profile

### Team Building
- **Role Flexibility**: Allows offensive Pokémon to pivot into defensive roles
- **Matchup Coverage**: Improves neutral matchups into favorable ones
- **Synergy**: Pairs well with moves that benefit from type diversity

## Comparison to Similar Abilities

### Type Addition Abilities
- **Turboblaze**: Adds Fire type (ID varies)
- **Teravolt**: Adds Electric type (ID varies)  
- **Grounded**: Adds Ground type (ID varies)
- **IceAge**: Adds Ice type (ID varies)
- **HalfDrake**: Adds Dragon type (ID varies)
- **Aquatic**: Adds Water type (ID varies) 
- **Phantom**: Adds Ghost type (ID varies)
- **FairyTale**: Adds Fairy type (ID varies)
- **Hover**: Adds Psychic type (ID varies)
- **LightningBorn**: Adds Electric type (ID varies)

### Unique Features
- **Steel Focus**: Only ability that adds Steel typing specifically
- **Defensive Emphasis**: Steel provides more resistances than most other types
- **Poison Immunity**: Unique among type-addition abilities for complete poison immunity

## Implementation Details

### Function Call Chain
1. `onEntry` trigger fires when Pokémon switches in
2. `AddBattlerType(battler, TYPE_STEEL)` called
3. `IS_BATTLER_OF_TYPE` check prevents duplicate typing
4. `gBattleMons[battler].type3 = TYPE_STEEL` stores the new type
5. `BattleScript_BattlerAddedTheType` displays message

### Battle Script Integration
- Uses `BattleScript_BattlerAddedTheType` for message display
- Text buffer prepared with `PREPARE_TYPE_BUFFER`
- Integrates with standard battle message system

### Type Checking System
- `IS_BATTLER_OF_TYPE(battler, type)` macro checks all three type slots
- `type3` serves as the additional typing slot
- Standard type effectiveness calculations include all three types

## Code References

### Primary Implementation
- **File**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc`
- **Line**: Search for "constexpr Ability Metallic"
- **Function**: Uses `AddBattlerType` helper function

### Related Files
- **Constants**: `/Users/joel/Github/eliteredux/eliteredux-source/include/generated/constants/abilities.h`
- **Protobuf**: `/Users/joel/Github/eliteredux/eliteredux-source/proto/AbilityList.textproto`

### Battle Scripts
- **Message Script**: `BattleScript_BattlerAddedTheType`
- **Text Preparation**: `PREPARE_TYPE_BUFFER` macro

## Related Abilities

### Metallic Jaws (ID: 792)
```cpp
constexpr Ability MetallicJaws = {
    .onEntry = Metallic.onEntry,
    .onParentalBond = PrimalMaw.onParentalBond,
};
```
Combination ability that includes Metallic's type addition plus Primal Maw's multi-hit effect.

## Conclusion
Metallic is a straightforward but powerful defensive utility ability that transforms any Pokémon into a Steel-type hybrid. Its value lies in providing significant defensive improvements while preserving all offensive capabilities, making it particularly valuable for fragile offensive Pokémon that need survivability without sacrificing their role as attackers.