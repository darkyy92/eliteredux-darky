---
id: 133
name: Weak Armor
status: ai-generated
character_count: 290
---

# Weak Armor - Ability ID 133

## In-Game Description
"If hit by a contact attack: -1 Defense and +2 Speed."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When hit by a physical move, this ability activates automatically, lowering Defense by 1 stage but raising Speed by 2 stages. The stat changes help the Pokemon become a faster sweeper at the cost of reduced physical bulk. Triggers even if Defense or Speed stats are already at minimum or maximum limits.

## Detailed Mechanical Explanation
Weak Armor is a defensive ability that transforms physical hits into speed boosts:

**Trigger Conditions:**
- Must be hit by a physical move (checks IS_MOVE_PHYSICAL)
- Does not require the move to make contact, despite the in-game description saying "contact attack"
- Activates after taking damage from the move
- Works even if the Pokemon faints from the attack (stat changes apply before fainting)

**Effects:**
- Lowers Defense by 1 stage (-1)
- Raises Speed by 2 stages (+2)
- Both stat changes happen in sequence (Defense drop first, then Speed boost)

**Special Interactions:**
- The ability will trigger if either stat can be changed (doesn't require both to be changeable)
- If Defense is already at -6, the Speed boost will still apply
- If Speed is already at +6, the Defense drop will still apply
- Against moves with the hit-and-run effect (like U-turn), the ability disables Eject Pack on the Weak Armor user to ensure proper stat change application

**Strategic Considerations:**
- Excellent for Pokemon that want to set up as fast sweepers
- The 2-stage Speed boost often outweighs the Defense drop for offensive strategies
- Pairs well with physical bulk investment to offset the Defense drops
- Can be used strategically with weak physical moves to intentionally trigger the Speed boost