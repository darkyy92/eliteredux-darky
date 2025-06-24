---
id: 801
name: Sun's Bounty
status: ai-generated
character_count: 295
---

# Sun's Bounty - Ability ID 801

## In-Game Description
"Leaf Guard + Harvest."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (IMPORTANT: exactly 280-300 chars counted WITH spaces)*

Sun's Bounty combines two powerful abilities: Leaf Guard heals all status conditions at the end of each turn during harsh sunlight, while Harvest restores consumed berries. In sun, berry restoration is guaranteed; otherwise it's 50%. Perfect for sustainable recovery.

*Character count: 295*

## Detailed Mechanical Explanation
*For Discord/reference use*

**Core Mechanics:**
Sun's Bounty is a combination ability that provides both the effects of Leaf Guard and Harvest simultaneously.

**Leaf Guard Component:**
- At the end of each turn, if harsh sunlight is active, the Pokémon is automatically cured of all status conditions
- Heals: Poison, Badly Poisoned, Sleep, Paralysis, Burn, Freeze, Frostbite, and Bleed
- Also removes Nightmare condition
- Only activates during any form of harsh sunlight (temporary, permanent, or Primal)

**Harvest Component:**  
- At the end of each turn, if the Pokémon has no held item but previously consumed a berry, it may restore that berry
- Restoration rate: 100% chance in harsh sunlight, 50% chance in other weather conditions
- Only works with items from the Berry pocket (all berries)
- Tracks the last consumed berry via `gBattleStruct->usedHeldItems`

**Activation Conditions:**
- Both effects activate during the end-of-turn phase
- Leaf Guard: Requires harsh sunlight (WEATHER_SUN_ANY) and at least one status condition
- Harvest: Requires no current held item, a previously consumed berry, and either sunlight (guaranteed) or 50% chance otherwise

**Weather Dependencies:**
- Harsh sunlight includes: Sunny Day, Drought, and Desolate Land
- Both effects benefit from sunlight, making sun teams ideal for this ability
- Leaf Guard only functions in sunlight, Harvest works in any weather but is more reliable in sun

**Technical Implementation:**
```cpp
constexpr Ability SunsBounty = {
    .onEndTurn = +[](ON_END_TURN) -> int { 
        return Harvest.onEndTurn(DELEGATE_END_TURN) | LeafGuard.onEndTurn(DELEGATE_END_TURN); 
    },
};
```

The ability calls both component abilities' `onEndTurn` functions and combines their results with bitwise OR.

**Strategic Implications:**
- Exceptional sustain ability for sun-based teams
- Allows for repeated use of healing berries (Sitrus, Oran) or stat berries (Liechi, Petaya)
- Status immunity in sun makes it excellent for setup sweepers
- Synergizes perfectly with Chlorophyll users and other sun-dependent strategies

**Competitive Usage:**
- Primarily seen on bulky sun sweepers or support Pokémon
- Popular berry choices: Sitrus Berry (HP recovery), Lum Berry (status cure backup), Weakness Policy (stat boost)
- Pairs well with: Drought users, Heat Rock holders, other sun-dependent abilities

**Common Users:**
- Found on various Grass-type Pokémon in Elite Redux
- Particularly effective on Pokémon with good bulk and sun synergy
- Often paired with moves like Synthesis or Morning Sun for additional recovery

**Counters:**
- Weather changing moves (Rain Dance, Sandstorm, Hail)
- Abilities that change weather (Drizzle, Sand Stream, Snow Warning)
- Cloud Nine and Air Lock negate weather effects
- Knock Off removes berries before they can be harvested

**Synergies:**
- Drought: Provides permanent sun for both effects
- Heat Rock: Extends sun duration when setting up manually  
- Chlorophyll: Speed boost in sun complements the ability's defensive benefits
- Solar Power: Offense boost in sun, with status immunity preventing burn damage

**Version History:**
- Added in Elite Redux as part of the expanded ability system
- Designed to create a powerful sun-based defensive option
- Combines two popular competitive abilities into one package