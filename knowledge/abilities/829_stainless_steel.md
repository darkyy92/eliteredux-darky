---
id: 829
name: Stainless Steel
status: ai-generated
character_count: 297
---

# Stainless Steel

**ID**: 829  
**Short Description**: Fort Knox + Wonder Skin.

## Extended In-Game Description
Stainless Steel provides dual defensive and offensive benefits. It blocks multi-hit abilities like Parental Bond from triggering against this Pokémon, unless the attacker resists Fort Knox. Additionally, all Normal-type moves become Steel-type and receive a 20% power boost. This makes it excellent for both tanking and sweeping.

**Character count: 297**

## Detailed Mechanics

### Fort Knox Protection
- Prevents multi-hit abilities (Parental Bond, Multi-Headed, etc.) from activating when attacking this Pokémon
- Only abilities with `resistsFortKnox = TRUE` can bypass this protection
- Currently only Parental Bond and Multi-Headed can resist Fort Knox

### Steel-type Conversion (-ate ability)
- Converts all Normal-type moves to Steel-type
- Converted moves receive a 20% power boost (`ateBoost`)
- Works on all Normal-type moves including status moves (though status moves don't benefit from the power boost)
- The type change happens before damage calculation, so Steel-type effectiveness and STAB apply

### Implementation Details
From `src/abilities.cc`:
```cpp
constexpr Ability StainlessSteel = {
    ATE_ABILITY(TYPE_STEEL),
    .fortKnox = TRUE,
};
```

The `ATE_ABILITY` macro handles the type conversion:
```cpp
#define ATE_ABILITY(type)                    \
    .onMoveType = +[](ON_MOVE_TYPE) -> int { \
        CHECK(moveType == TYPE_NORMAL)       \
        *ateBoost = TRUE;                    \
        return type + 1;                     \
    },
```

### Strategic Uses
- Excellent on Steel-types for STAB on converted Normal moves
- Strong defensive ability against common multi-hit strategies
- Pairs well with high-powered Normal moves like Return, Extreme Speed, or Boomburst
- The Fort Knox effect makes it valuable against teams relying on Parental Bond sweepers

### Notes
- Despite the description mentioning "Wonder Skin", this ability only inherits Wonder Skin's Fort Knox property, not any accuracy-related effects
- The Fort Knox protection is checked before applying multi-hit effects in battle calculations
- This is one of the few abilities that combines both defensive utility and offensive type conversion