---
ability_id: 331
ability_name: Soul Eater
ability_description: "Dealing a KO heals 1/4 of this Pokémon's max HP."
extended_description: "When this Pokémon knocks out an opponent with any damaging move, it immediately recovers 25% of its maximum HP. This healing effect triggers after each knockout, making the Pokémon increasingly difficult to defeat in prolonged battles as it sustains itself through consecutive victories."
extended_description_length: 287
trigger_conditions:
  - "onBattlerFaints with APPLY_ON_ATTACKER"
healing_amount: "25% of maximum HP"
battle_script: "BattleScript_HandleSoulEaterEffect"
analysis_date: "2025-06-24"
---

# Soul Eater (Ability #331)

## Basic Information
- **Name**: Soul Eater
- **ID**: 331 (ABILITY_SOUL_EATER)
- **Description**: "Dealing a KO heals 1/4 of this Pokémon's max HP."

## Extended Description (287 characters)
When this Pokémon knocks out an opponent with any damaging move, it immediately recovers 25% of its maximum HP. This healing effect triggers after each knockout, making the Pokémon increasingly difficult to defeat in prolonged battles as it sustains itself through consecutive victories.

## Mechanical Analysis

### Implementation Details
- **Trigger**: `onBattlerFaints` with `APPLY_ON_ATTACKER`
- **Condition**: Activates when the Pokémon with Soul Eater knocks out an opponent
- **Effect**: Heals 25% of the user's maximum HP
- **Battle Script**: `BattleScript_HandleSoulEaterEffect`

### Code Implementation
```cpp
constexpr Ability SoulEater = {
    .onBattlerFaints = +[](ON_BATTLER_FAINTS) -> int {
        CHECK_NOT(BATTLER_MAX_HP(battler));
        CHECK(CanBattlerHeal(battler));
        BattleScriptCall(BattleScript_HandleSoulEaterEffect);
        return TRUE;
    },
    .onBattlerFaintsFor = APPLY_ON_ATTACKER,
};
```

### Battle Script
```assembly
BattleScript_HandleSoulEaterEffect::
    tryhealpercenthealth BS_STACK_1, 25, BattleScript_Return
BattleScript_HandleSoulEaterEffect_AfterHeal:
    orword gHitMarker, HITMARKER_IGNORE_SUBSTITUTE
    healthbarupdate BS_STACK_1
    datahpupdate BS_STACK_1
    printstring STRINGID_STACKREGAINEDHEALTH
    waitmessage B_WAIT_TIME_LONG
    return
```

## Strategic Analysis

### Strengths
- **Sustain**: Provides excellent longevity in battles through healing
- **Snowball Effect**: Each victory makes the Pokémon harder to defeat
- **Reliable Activation**: Triggers on any knockout, not just specific move types
- **Substantial Healing**: 25% HP recovery is significant

### Limitations
- **Requires Knockouts**: No benefit if the Pokémon can't secure KOs
- **No Effect at Full HP**: Cannot heal beyond maximum HP
- **Single Battle Focus**: Most effective in battles with multiple opponents

### Tactical Applications
- **Sweeper Role**: Ideal for Pokémon designed to sweep through multiple opponents
- **Late Game Power**: Becomes increasingly valuable as battles progress
- **Endurance Battles**: Excellent for longer, drawn-out fights
- **Double/Triple Battles**: More opportunities for knockouts and healing

## Related Abilities
Soul Eater's healing mechanic is shared by several other abilities in the codebase:
- **Blood Bath**: Also uses `SoulEater.onBattlerFaints` for healing
- **Jaws of Carnage**: Uses `BattleScript_HandleJawsOfCarnageEffect` (50% healing)
- **Hunter's Horn**: References the same 25% healing mechanism
- **Various Combination Abilities**: Many abilities incorporate Soul Eater's effect

## Technical Notes
- The ability uses `tryhealpercenthealth` with a 25% value
- Healing is subject to standard battle conditions (can't heal at full HP, must be able to heal)
- The effect bypasses Substitute due to `HITMARKER_IGNORE_SUBSTITUTE`
- Displays the standard "regained health" message after healing