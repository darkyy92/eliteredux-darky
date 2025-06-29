---
id: 860
name: Haste Makes Waste
status: ai-generated
character_count: 299
---

# Haste Makes Waste - Ability ID 860

## In-Game Description
"Stall + Analytic."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Combines Stall and Analytic. When moving after the opponent, takes 30% less damage from their attacks while dealing 30% more damage with own moves. Rewards tactical waiting over hasty action, providing both defensive and offensive benefits when slower.

## Detailed Mechanical Explanation

### Mechanical Implementation

**Source Code Location:** `src/abilities.cc` (lines 8740-8744)

**Implementation:**
```cpp
constexpr Ability HasteMakesWaste = {
    .onOffensiveMultiplier = Analytic.onOffensiveMultiplier,
    .onDefensiveMultiplier = Stall.onDefensiveMultiplier,
    .breakable = TRUE,
};
```

## Component Abilities

### Stall Component (Defensive)
- **Effect:** Takes 30% less damage when moving after the opponent
- **Condition:** `gCurrentTurnActionNumber < GetBattlerTurnOrderNum(battler)`
- **Multiplier:** 0.7x damage taken
- **Code:** `MUL(.7)` in `onDefensiveMultiplier`

### Analytic Component (Offensive)
- **Effect:** Deals 30% more damage when moving after the target
- **Condition:** `GetBattlerTurnOrderNum(target) < gCurrentTurnActionNumber`
- **Exception:** Does not apply to Future Sight
- **Multiplier:** 1.3x damage dealt
- **Code:** `MUL(1.3)` in `onOffensiveMultiplier`

## Battle Mechanics

### Turn Order Dependency
Both effects rely on turn order comparison:
- **Stall activates:** When this Pokemon moves after the opponent that's attacking it
- **Analytic activates:** When this Pokemon moves after the target it's attacking
- **Breakable:** This ability can be suppressed by Mold Breaker and similar effects

### Synergy
The combination creates a powerful defensive-offensive tool:
1. **Defensive Phase:** When slower, reduces incoming damage by 30%
2. **Offensive Phase:** When slower, increases outgoing damage by 30%
3. **Strategic Value:** Encourages slower, more calculated play styles

### Limitations
- **Speed Dependency:** Both effects only work when moving after the opponent
- **Future Sight Exception:** Analytic component doesn't boost Future Sight damage
- **Breakable:** Can be negated by abilities like Mold Breaker
- **Turn Order Sensitive:** Effects depend on exact turn order calculations

## Competitive Applications

**Ideal Usage:**
- Slow, bulky Pokemon that can capitalize on moving last
- Trick Room teams where speed inversion maximizes both effects
- Defensive pivots that can also hit hard when needed

**Strategic Considerations:**
- Works best on Pokemon with naturally low speed or in Trick Room
- Provides both survival and revenge killing potential
- Can be used with speed control moves to manipulate turn order