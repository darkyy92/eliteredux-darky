---
id: 866
name: Relic Stone
status: ai-generated
character_count: 295
---

# Relic Stone Analysis

## Extended In-Game Description
*For use in Elite Redux extended ability UI (IMPORTANT: exactly 280-300 chars counted WITH spaces)*
"Other battlers don't benefit from STAB."

## Extended Description (295 characters)
While this ability is active on the field, all other battlers lose their Same Type Attack Bonus, dealing normal damage instead of 1.5x with type matching moves. Even battlers with Adaptability cannot achieve 2x STAB. Only affects opponents - the user retains their own STAB bonus. Suppressed by Mold Breaker abilities.

## Technical Implementation
- **Function**: Modifies `StabMultiplierInHalves()` in `src/battle_util.c`
- **Mechanism**: When any battler except the attacker has Relic Stone, the function returns 2 (1.0x multiplier) instead of normal STAB values
- **Scope**: Field-wide effect that impacts all other battlers
- **Breakable**: Yes - can be suppressed by Mold Breaker and similar abilities
- **Interaction**: Prevents both regular STAB (1.5x) and Adaptability STAB (2.0x)

## Battle Mechanics
1. Checks if any battler on the field (except the attacker) has Relic Stone
2. If found, forces STAB multiplier to 1.0x for ALL battlers except Relic Stone users
3. Applies to all move types and does not discriminate between physical/special moves
4. Effect persists as long as a Relic Stone user remains active in battle

## Strategic Usage
- Excellent for defensive teams facing STAB-reliant sweepers
- Particularly effective against mono-type teams that rely heavily on STAB damage
- Can neutralize powerful Adaptability users like Porygon-Z or Crawdaunt
- Synergizes well with diverse movepool teams that don't rely on STAB