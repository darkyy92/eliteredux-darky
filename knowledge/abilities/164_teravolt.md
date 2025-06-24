---
id: 164
name: Teravolt
status: ai-generated
character_count: 284
---

# Teravolt (Ability ID: 164)

## Overview
Teravolt is a dual-function ability that combines mold breaker mechanics with type addition, making it one of the most strategically significant abilities for Electric-type attackers.

## Core Mechanics

### 1. Mold Breaker Effect
- **Function**: Moves bypass opponent abilities that would normally block, reduce, or redirect attacks
- **Implementation**: Via `ShouldSetMoldBreaker()` function in battle script commands
- **Scope**: Affects all moves used by the Pokemon with Teravolt
- **Examples**: Moves hit through Levitate, Volt Absorb, Lightning Rod, Wonder Guard, etc.

### 2. Type Addition (Electric)
- **Function**: Adds Electric type as a third type upon entry
- **Implementation**: `AddBattlerType(battler, TYPE_ELECTRIC)` on entry
- **Mechanics**: 
  - Only activates if Pokemon doesn't already have Electric type
  - Added as `type3` slot in battle data structure
  - Permanent for the duration of battle presence

### 3. Entry Message
- **Text**: "{Pokemon} is radiating a bursting aura!"
- **Trigger**: Displays when Pokemon enters battle
- **Visual**: Indicates both the mold breaker effect and type addition

## Strategic Applications

### Offensive Benefits
- **Ability Bypassing**: Counters defensive abilities like Levitate, type immunities, and damage reduction
- **STAB Enhancement**: Non-Electric types gain Electric STAB when using Electric moves
- **Coverage Expansion**: Adds Electric typing for resistances and weaknesses

### Type Synergies
Most effective on Pokemon that:
- Lack Electric typing naturally
- Have access to Electric moves in their movepool
- Benefit from Electric typing's resistances (Flying, Steel, Electric)

## Pokemon Distribution
Based on base stats analysis, Teravolt appears on several high-tier Pokemon:
- Multiple Electric/Dragon legendaries
- Electric/Grass utility Pokemon
- Various Electric/Flying forms
- Several Electric-type variants and legendary forms

## Battle AI Considerations
- **AI Score**: Adds Electric type consideration to AI scoring algorithms
- **Priority**: Rated as priority 7 in AI utility calculations
- **Strategy**: AI recognizes both offensive breakthrough and type advantages

## Technical Implementation

### Code Structure
```cpp
constexpr Ability Teravolt = {
    .onEntry = +[](ON_ENTRY) -> int { 
        return AddBattlerType(battler, TYPE_ELECTRIC); 
    },
};
```

### Mold Breaker Integration
```cpp
int ShouldSetMoldBreaker(int battler, MoveEnum move) {
    // ... other conditions ...
    if (BattlerHasAbility(gBattlerAttacker, ABILITY_TERAVOLT, FALSE)) return TRUE;
    // ...
}
```

## Extended In-Game Description
Teravolt charges the Pokemon with bursting electrical energy that allows moves to penetrate all defensive abilities while adding Electric typing. Bypasses Wonder Guard, Levitate, and other protective traits while granting Electric STAB and resistances for maximum battlefield control.

**Character count: 284**

## Related Abilities
- **Turboblaze**: Fire-type equivalent with identical mold breaker mechanics
- **Mold Breaker**: Pure mold breaker effect without type addition
- **Blind Rage**: Another mold breaker variant
- **Mycelium Might**: Status move-specific mold breaker

## Competitive Impact
Teravolt transforms non-Electric Pokemon into Electric-type threats while ensuring their moves cannot be easily walled by defensive abilities, making it a premium ability for mixed attackers and utility Pokemon requiring guaranteed move execution.