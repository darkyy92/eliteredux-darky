---
id: 612
name: Rejection
status: ai-generated
character_count: 288
---

# Rejection - Ability ID 612

## In-Game Description
"On switch-in, applies the Quash field effect for 5 turns."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Upon switch-in, creates a temporal distortion field lasting 5 turns that reduces all move priorities to -4, effectively neutralizing speed-based strategies and priority moves. This battlefield-wide effect forces predictable turn order and counters rush tactics, making battles methodical.

## Detailed Mechanical Explanation

**Ability Effect:** On switch-in, applies the Quash field effect for 5 turns if not already active.

**Implementation Details:**
- Activates only if `gFieldTimers.quashTimer` is not already set
- Sets `gFieldTimers.quashTimer = QUASH_DURATION` (5 turns)
- Sets `gFieldTimers.started.quash = TRUE`
- Displays message: "The timeline can no longer be distorted!"

### Quash Field Effect

The Quash field effect fundamentally alters turn order and priority mechanics:

1. **Priority Suppression:** All moves have their priority reduced to minimum -4 (via `min(-4, priority)`)
2. **Speed Order Disabled:** Disables `afterYou`, `dazed` negation, and other speed-based mechanics
3. **Universal Effect:** Affects all battlers on the field
4. **Duration:** Lasts 5 turns, counting down each turn
5. **End Message:** "The normalization of time comes to an end!"

### Strategic Applications

- **Speed Control Neutralization:** Completely negates speed-based strategies and priority moves
- **Turn Order Equalization:** Forces all moves to ultra-low priority, making turn order more predictable
- **Anti-Priority:** Counters priority-heavy teams and strategies
- **Field Control:** Establishes battlefield tempo control from switch-in

### Interactions

- Cannot reactivate if Quash is already in effect
- Affects all move priorities regardless of source (abilities, items, move effects)
- Works in conjunction with other field effects
- Not prevented by abilities like Magic Bounce or Clear Body

