---
ability_id: 362
ability_name: "Frozen Soul"
ability_type: "Priority Control"
battle_mechanic: "Move Priority"
extended_description: "When this Pokémon is at maximum HP, all Ice-type moves it uses gain +1 priority. This allows faster Ice attacks to outspeed opponents but only while completely healthy, creating strategic pressure around HP management and positioning. Similar to Gale Wings but for Ice-type moves exclusively."
short_description: "Ice-type moves get +1 priority at max HP."
activation_condition: "Max HP + Ice-type move"
priority_boost: "+1"
type_restriction: "Ice-type moves only"
hp_requirement: "Must be at maximum HP"
tags: ["priority", "conditional", "ice-type", "gale-wings-variant"]
competitive_tier: "High"
strategic_value: "Excellent"
---

# Frozen Soul (Ability #362)

## Overview
Frozen Soul is a priority-granting ability that gives Ice-type moves +1 priority when the user is at maximum HP. It is functionally identical to Gale Wings but for Ice-type moves instead of Flying-type moves, making it a powerful tool for Ice-type attackers who can maintain their health.

## Code Implementation

### Source Location
- **File**: `/Users/joel/Github/eliteredux/eliteredux-source/src/abilities.cc`
- **Line**: 3796-3798
- **Definition**: `constexpr Ability FrozenSoul = { .onPriority = GALE_WINGS_CLONE(TYPE_ICE), };`

### Macro Definition
The ability uses the `GALE_WINGS_CLONE` macro (lines 128-133):
```cpp
#define GALE_WINGS_CLONE(type)                               \
    +[](ON_PRIORITY) -> int {                                \
        CHECK(GetTypeBeforeUsingMove(move, battler) == type) \
        CHECK(BATTLER_MAX_HP(battler))                       \
        return 1;                                            \
    }
```

### Key Technical Details
- **HP Check**: Uses `BATTLER_MAX_HP(battler)` macro defined in `/Users/joel/Github/eliteredux/eliteredux-source/include/battle.h:781`
  - Formula: `(gBattleMons[battlerId].hp == gBattleMons[battlerId].maxHP)`
- **Type Check**: Verifies move type before usage via `GetTypeBeforeUsingMove()`
- **Priority Boost**: Returns `1` for +1 priority boost
- **Ability Registration**: Listed in ability table at line 9207

## Mechanics

### Activation Requirements
1. **Maximum HP**: The Pokémon must have full HP (current HP = max HP)
2. **Ice-type Move**: The move being used must be Ice-type
3. **Move Usage**: Only applies when the Pokémon is using a move

### Priority System
- Normal moves have priority 0
- With Frozen Soul active, Ice moves get priority +1
- This allows Ice moves to outspeed most other moves
- Does not stack with other priority effects

### Limitations
- **HP Dependent**: Any damage taken disables the ability until HP is restored to maximum
- **Type Specific**: Only affects Ice-type moves
- **No Status Moves**: Only affects damaging and non-damaging Ice-type moves

## Strategic Applications

### Offensive Strategies
1. **Lead Sweeping**: Perfect for fast Ice-type leads with powerful moves
2. **Revenge Killing**: Guaranteed first strike when at full HP
3. **Priority Control**: Dominates priority wars with Ice moves
4. **Setup Protection**: Can interrupt setup attempts with priority Ice moves

### Synergistic Moves
- **Ice Beam**: Reliable priority special attack
- **Blizzard**: High-power priority special move (perfect accuracy in hail)
- **Icicle Crash**: Strong priority physical attack
- **Freeze-Dry**: Priority move that hits Water-types super effectively
- **Ice Shard**: Already has priority, becomes +2 priority

### Team Building Considerations
- Pairs well with healing support (Wish, Heal Bell)
- Benefits from Leftovers or other passive recovery
- Strong with Life Orb for maximum damage output
- Excellent with Choice items for hit-and-run tactics
- Synergizes with hail support for Blizzard accuracy

## Competitive Analysis

### Strengths
1. **Immediate Threat**: Forces opponents to respect priority Ice moves
2. **Speed Control**: Bypasses speed tiers entirely when active
3. **Versatile**: Works with both physical and special Ice moves
4. **Psychological Pressure**: Opponents must play around potential priority
5. **Type Coverage**: Ice moves hit many common types super effectively

### Weaknesses
1. **HP Dependency**: Easily disabled by any damage
2. **Type Limitation**: No priority on non-Ice moves
3. **Predictable**: Opponents know to damage first to disable
4. **Stealth Rock Vulnerability**: Ice types are often weak to Rock moves
5. **Limited STAB Users**: Fewer Ice-type Pokémon compared to other types

### Comparison to Similar Abilities
- **Gale Wings**: Same mechanics but for Flying-type moves
- **Flaming Soul**: Same mechanics but for Fire-type moves  
- **Triage**: +3 priority but only for healing moves
- **Prankster**: +1 priority for status moves only
- **Quick Draw**: 30% chance for +1 priority on any move

## Pokémon with Frozen Soul

Based on proto file analysis, the following Pokémon have access to Frozen Soul:

### Primary Ability Holders
- **Vulpix (Alolan)**: Ice/Fairy type with solid special stats and Snow Warning synergy
- **Ninetales (Alolan)**: Ice/Fairy type with excellent special attack and support options
- **Vibrava (Redux)**: Ground/Dragon type with Ice-type as innate ability
- **Flygon (Redux)**: Ground/Dragon type with versatile movepool
- **Castform (Snowy)**: Ice-type form with Weather Control synergy

### Usage Patterns
- Most common on Ice-type Pokémon with strong offensive stats
- Often paired with weather-setting abilities (Snow Warning)
- Frequently combined with other defensive abilities as innates
- Excellent on Pokémon with access to diverse Ice-type movepool

## Related Abilities

### Direct Variants (GALE_WINGS_CLONE Family)
- **Gale Wings** (Ability #177): Flying-type version
- **Flaming Soul** (Ability #351): Fire-type version
- **Volt Rush** (Ability #430): Electric-type version
- **Early Grave** (Ability #522): Ghost-type version
- **Dark Gale Wings** (Ability #558): Dark-type version
- **Water Gale Wings** (Ability #559): Water-type version
- **Cute Antecedence** (Ability #579): Fairy-type version

### Complementary Abilities
- **Snow Warning**: Weather support for Ice moves (Blizzard accuracy)
- **Refrigerate**: Converts Normal moves to Ice-type
- **Slush Rush**: Speed boost in hail/snow
- **Snow Cloak**: Evasion boost in hail

## Counters and Interactions

### Effective Counters
1. **Residual Damage**: Stealth Rock, Spikes, hail damage, burn, poison
2. **Multi-hit Moves**: Breaks through and disables ability
3. **Priority Moves**: Can still be outsped by higher priority
4. **Fire-type Users**: Resist Ice moves and can deal super effective damage
5. **Steel-type Users**: Resist Ice moves naturally

### Notable Interactions
- **Choice Items**: Lock into one move but maintain priority
- **Life Orb**: Extra damage without HP dependency issues
- **Hail/Snow**: Enables perfect accuracy Blizzard with priority
- **Weather**: Sun weakens Ice moves, hail provides indirect support
- **Aurora Veil**: Can be set up with priority in hail conditions

### Weather Synergy
- **Hail/Snow**: Perfect accuracy Blizzard becomes devastating
- **Sun**: Reduces Ice-type move damage
- **Rain**: Neutral but may conflict with hail setup
- **Sandstorm**: Chips HP and disables ability

## Strategic Depth

### Early Game Advantages
- Priority Ice Beam can eliminate frail sweepers immediately
- Forces opponents to lead with bulky Pokémon or priority users
- Excellent for applying immediate pressure in lead matchups

### Mid-Game Applications
- Revenge killing after team members fall
- Breaking through weakened defensive cores
- Preventing setup sweepers from getting going

### Late Game Value
- Cleaning up weakened teams with priority moves
- Last-ditch offensive pressure when other options fail
- Game-winning priority in speed tie situations

## Conclusion

Frozen Soul is a high-impact ability that transforms Ice-type Pokémon into immediate threats when at full HP. Its strategic value lies in the constant pressure it applies to opponents, forcing them to prioritize dealing damage to disable the ability. While HP-dependent, skilled players can leverage healing support and careful positioning to maintain the advantage throughout battle.

The ability rewards aggressive play while punishing passive strategies, making it excellent for fast-paced offensive teams that can protect their Frozen Soul user's HP while applying constant pressure with priority Ice moves. The synergy with hail weather and moves like Blizzard makes it particularly potent in weather-based team compositions.

Ice-type moves' natural coverage against Dragon, Flying, Grass, and Ground types makes Frozen Soul users versatile revenge killers and offensive threats that can break through many common defensive strategies when properly supported.