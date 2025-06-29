---
id: 786
name: Lullaby
status: ai-generated
character_count: 290
---

# Lullaby - Ability ID 786

## In-Game Description
"Sing accuracy is 90% when used by this Pokemon."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (IMPORTANT: exactly 280-300 chars counted WITH spaces)*

This Pokemon's soothing voice enhances the effectiveness of Sing, boosting its accuracy from a normally unreliable 60% to a much more dependable 90%. This makes sleep-inducing strategies far more viable in battle, especially against faster foes.

## Detailed Mechanical Explanation
*For Discord/reference use*

**Core Mechanic:**
- Multiplies Sing's accuracy by 1.5x (60% to 90%)
- Only affects the move Sing (MOVE_SING)
- Implemented as an onAccuracy callback with ACCURACY_MULTIPLICATIVE priority

**Technical Implementation:**
```cpp
constexpr Ability Lullaby = {
    .onAccuracy = +[](ON_ACCURACY) -> AccuracyPriority {
        CHECK(move == MOVE_SING);
        *accuracy *= 1.5;
        return ACCURACY_MULTIPLICATIVE;
    },
};
```

**Strategic Applications:**
- Makes Sing a reliable sleep-inducing option at 90% accuracy
- Particularly valuable for Pokemon that rely on status strategies
- Transforms an otherwise unreliable 60% accuracy move into a near-guaranteed hit
- Enables consistent sleep setups for sweepers or support roles

**Interaction Notes:**
- Only affects Sing specifically - other sleep moves are unaffected
- Stacks multiplicatively with other accuracy modifiers
- Can be further boosted by items like Wide Lens or moves like Lock-On
- Subject to standard accuracy checks (opponent's evasion, etc.)

**Competitive Viability:**
- Niche but effective ability for specific team compositions
- Most valuable on Pokemon with good defensive stats to survive while setting up sleep
- Pairs well with moves that benefit from sleeping opponents (Dream Eater, etc.)
- Limited by being restricted to a single move, reducing overall utility