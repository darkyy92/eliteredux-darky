---
id: 821
name: Scarecrow
status: ai-generated
character_count: 295
---

# Scarecrow (Ability #821)

## Basic Information
- **ID**: 821
- **Name**: Scarecrow
- **Description**: "Scare + Bad Luck."
- **Type**: Combination Ability
- **Breakable**: Yes

## Effects

### On Entry (Scare Component)
- Lowers opposing Pokémon's **Special Attack** by 1 stage when entering battle
- Affects both opponents in double battles
- Cannot be prevented by abilities like Substitute
- Triggers Guard Dog's Attack boost if the target has that ability

### Battle Effects (Bad Luck Component)
- **Critical Hit Prevention**: Completely prevents opposing Pokémon from landing critical hits
- **Effect Chance Reduction**: Reduces the effect chance of opposing moves to 0% if they're normally less than 100%
- **Minimum Rolls**: Forces opposing Pokémon to roll minimum values for damage ranges and other RNG effects
- **Applies to**: All opposing Pokémon (foes only)

## Implementation Details

### Code Location
- **Main Definition**: `src/abilities.cc` (Scarecrow ability)
- **Intimidate Data**: `src/pokemon.c` (gIntimidateCloneData array)
- **Battle Function**: `src/battle_util.c` (UseIntimidateClone function)

### Technical Mechanics
```cpp
constexpr Ability Scarecrow = {
    .onEntry = UseIntimidateClone,           // Scare effect
    .onCrit = BadLuck.onCrit,                // Prevent crits
    .onModifyEffectChance = BadLuck.onModifyEffectChance,  // Reduce effect chances
    .onCritFor = BadLuck.onCritFor,          // Apply to foes
    .onModifyEffectChanceFor = BadLuck.onModifyEffectChanceFor,
    .breakable = TRUE,
};
```

### Intimidate Clone Data
```cpp
{
    .ability = ABILITY_SCARECROW,
    .numStatsLowered = 1,
    .statsLowered = {STAT_SPATK, 0, 0},  // Special Attack only
    .targetBoth = TRUE,                   // Affects both opponents
}
```

## Extended In-Game Description
**Character count: 295**

Scarecrow combines Scare and Bad Luck abilities into one powerful entry hazard. Upon switching in, it intimidates opposing Pokémon by lowering their Special Attack by one stage, affecting both foes in double battles. Additionally, it cursed opponents with extremely bad luck throughout battle, completely preventing them from landing critical hits and reducing any move effect chances below 100% to 0%. This combination makes Scarecrow excellent for neutering special attackers while providing consistent battle control through RNG manipulation.

## Interactions

### Guard Dog Interaction
- If the target has Guard Dog, the Special Attack drop is converted to a +1 Attack boost
- Guard Dog's ability popup will trigger after the intimidate effect

### Ability Interactions
- **Breakable**: Can be suppressed by Mold Breaker and similar abilities
- **Clear Body/White Smoke**: Prevents the Special Attack drop but not the Bad Luck effects
- **Competitive/Defiant**: Will trigger from the Special Attack drop

### Move Interactions
- **Critical Hit Moves**: Completely blocked - moves like Storm Throw become regular attacks
- **Effect Chances**: Moves with <100% effect rates (like Thunderbolt's 10% paralysis) become 0%
- **Perfect Accuracy Moves**: Effect chances still reduced, but accuracy unaffected

## Strategic Usage

### Best Used For
- **Special Wall Setup**: Crippling special attackers while setting up
- **RNG Control**: Eliminating critical hit threats and secondary effect risks
- **Double Battles**: Maximum value from intimidating both opponents
- **Status Spreaders**: Shutting down unreliable status moves

### Situational Considerations
- Less effective against physical attackers (only affects Special Attack)
- Bad Luck effects don't stack with multiple Scarecrow users
- Guard Dog users can turn the intimidate against you
- Mold Breaker completely bypasses all effects