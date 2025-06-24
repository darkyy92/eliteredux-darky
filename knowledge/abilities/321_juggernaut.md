---
ability_id: 321
ability_name: "Juggernaut"
category: "Contact Enhancement"
implemented: true
breakable: true
status_immunity: ["paralysis"]
removes_status_on_immunity: true
---

# Juggernaut (Ability #321)

## Basic Information
**Name:** Juggernaut  
**ID:** 321  
**Category:** Contact Enhancement  
**Breakable:** Yes  
**Removes Status on Immunity:** Yes  

## Short Description
Contact moves add 20% Def to attack. Paralysis-immune.

## Extended Description (295 characters)
Juggernaut enhances contact moves by adding 20% of the user's Defense stat to attack calculations, making bulky Pokemon surprisingly powerful. Also provides complete immunity to paralysis status and automatically removes paralysis if inflicted by unblockable abilities like Mold Breaker.

## Mechanics Analysis

### Contact Move Enhancement
- **Trigger:** When using any move with the `contact` flag
- **Effect:** Adds 20% of the user's Defense stat to the attack calculation
- **Implementation:** Uses `secondaryAtkStatToUse[STAT_DEF] += 20` mechanism
- **Calculation:** Final attack = Base attack + (Defense × 0.20)

### Paralysis Immunity
- **Complete Immunity:** Cannot be paralyzed by any means
- **Status Removal:** If paralysis is inflicted by unblockable effects (like Mold Breaker), it's immediately removed
- **Implementation:** `onStatusImmune` with `CHECK_PARALYSIS` flag

### Ability Properties
- **Breakable:** Can be suppressed by abilities like Mold Breaker
- **Stackable:** Works with other stat-boosting effects
- **Contact-Only:** Only affects moves that make physical contact

## Strategic Applications

### Defensive Pivots
- Transforms defensive Pokemon into offensive threats
- Rewards investment in Defense stat for dual purposes
- Creates unique mixed-role archetypes

### Contact Move Synergy
- Benefits physical attackers with naturally high Defense
- Encourages use of contact moves over non-contact alternatives
- Synergizes with abilities that boost Defense

### Paralysis Immunity Benefits
- Prevents speed reduction and move failure
- Valuable against Thunder Wave users
- Protects against Body Slam paralysis chance

## Code Implementation

```cpp
constexpr Ability Juggernaut = {
    .onChooseOffensiveStat =
        +[](ON_CHOOSE_OFFENSIVE_STAT) {
            if (gBattleMoves[move].contact) secondaryAtkStatToUse[STAT_DEF] += 20;
        },
    .onStatusImmune = +[](ABILITY_ON_STATUS_IMMUNE) -> int {
        CHECK(status & CHECK_PARALYSIS)
        return TRUE;
    },
    .breakable = TRUE,
    .removesStatusOnImmunity = TRUE,
};
```

## Similar Abilities
- **Speed Force:** Uses Speed stat for contact moves instead of Defense
- **Iron Giant:** Combines Heatproof with Juggernaut's contact enhancement
- **Heatproof:** Provides fire resistance but lacks the contact enhancement

## Usage in Game
Found on several Pokemon species in the codebase, typically those with naturally high Defense stats that benefit from the dual offensive/defensive utility this ability provides.