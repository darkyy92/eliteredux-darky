# Terrify

---
id: 632
name: Terrify
status: ai-generated
character_count: 295
---

## Extended Description

Terrify intimidates opposing Pokemon upon switching in, drastically reducing their special attacking capabilities. When the Pokemon with this ability enters battle, all enemies suffer a severe two-stage drop to their Special Attack stat, making their special moves significantly weaker.

## Original Description

Lowers foes' Sp. Atk by two stages on entry.

## Implementation Details

- **Trigger**: On entry (switching in or battle start)
- **Target**: All opposing Pokemon
- **Effect**: Lowers Special Attack by 2 stages (-50% damage)
- **Type**: Intimidate clone using `UseIntimidateClone` function
- **Blockable**: Yes, by abilities like Clear Body or White Smoke

## Code Location

Located in `src/abilities.cc` as:
```cpp
constexpr Ability Terrify = {
    .onEntry = UseIntimidateClone,
};
```

The actual implementation uses the `UseIntimidateClone` function from `src/battle_util.c` which handles intimidate-like effects through the intimidate clone data system.