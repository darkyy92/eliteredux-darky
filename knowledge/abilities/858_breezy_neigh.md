---
id: 858
name: Breezy Neigh
status: ai-generated
character_count: 287
---

# Breezy Neigh (ID: 858)

## Short Description
"KOs raise Speed by one stage."

## Extended In-Game Description
When this Pokémon knocks out an opponent with a direct attack, its Speed stat increases by one stage. This boost occurs immediately after the target faints, potentially allowing the user to outspeed previously faster opponents. The effect activates only when the Pokémon with this ability directly causes a knockout through damage.

## Technical Implementation

**File**: `src/abilities.cc`
**Mechanism**: Uses the `MoxieClone` function with `STAT_SPEED` parameter
**Trigger**: `onBattlerFaints` with `APPLY_ON_ATTACKER`

```cpp
constexpr Ability BreezyNeigh = {
    .onBattlerFaints = AdrenalineRush.onBattlerFaints,
    .onBattlerFaintsFor = APPLY_ON_ATTACKER,
};

constexpr Ability AdrenalineRush = {
    .onBattlerFaints = +[](ON_BATTLER_FAINTS) -> int { return MoxieClone(battler, STAT_SPEED); },
    .onBattlerFaintsFor = APPLY_ON_ATTACKER,
};
```

## Key Mechanics

1. **Activation Condition**: Only activates when the Pokémon with Breezy Neigh directly causes a knockout
2. **Stat Boost**: Raises Speed by exactly one stage (+50% of base Speed stat)
3. **Timing**: Speed boost occurs immediately after the target faints
4. **Stacking**: Multiple knockouts result in multiple Speed boosts (up to +6 stages maximum)
5. **Battle Script**: Uses `BattleScript_RaiseStatOnFaintingTarget` for the animation and message

## Related Abilities
- **Moxie**: Raises Attack on KO (same mechanism, different stat)
- **Grim Neigh**: Raises Special Attack on KO  
- **Chilling Neigh**: Raises Attack on KO (from official games)
- **Adrenaline Rush** (ID: 454): Identical effect, shares the same implementation

## Battle Applications
- Excellent for sweeping teams after securing the first knockout
- Synergizes well with Choice Scarf or other speed-boosting items
- Particularly effective on Pokémon with good offensive stats but moderate base Speed
- Can turn slow, powerful attackers into late-game threats