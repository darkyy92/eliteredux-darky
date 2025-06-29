---
id: 143
name: Poison Touch
status: ai-generated
character_count: 290
---

# Poison Touch - Ability ID 143

## In-Game Description
"30% chance to poison on contact. Also works on offense."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (IMPORTANT: exactly 280-300 chars counted WITH spaces)*

When this Pokemon makes physical contact, either by using contact moves or being hit by them, there's a 30% chance the opposing Pokemon becomes poisoned. This ability functions both offensively and defensively during battle, but cannot poison targets already poisoned or immune to poison.

## Detailed Mechanical Explanation
*For Discord/reference use*

Poison Touch is a contact-based ability that activates in two scenarios:

1. **Offensive**: When the user attacks with a contact move, there's a 30% chance to poison the target
2. **Defensive**: When the user is hit by a contact move, there's a 30% chance to poison the attacker

### Implementation Details
- Uses the same code implementation as Poison Point (`PoisonPoint.onAttacker` and `PoisonPoint.onDefender`)
- Requires physical contact via moves that have the "contact" flag
- 30% activation rate on each contact interaction
- Cannot poison targets that are already poisoned or have poison immunity
- Works with both single-target and multi-target contact moves
- Functions in all battle formats (singles, doubles, etc.)

### Synergies and Interactions
- Combines well with moves that make multiple contact hits (e.g., Fury Swipes, Double Hit)
- Effective against physical attackers that rely on contact moves
- Provides both offensive utility (when attacking) and defensive utility (when being attacked)
- Can be negated by abilities that prevent status conditions or provide poison immunity

### Strategic Applications
- Excellent for tanks and walls that can survive contact moves and potentially cripple attackers
- Useful on offensive Pokemon to weaken defensive walls over time
- Particularly effective in longer battles where poison damage accumulates
- Strong deterrent against physical contact-based attackers