---
id: 115
name: Ice Body
status: ai-generated
character_count: 289
---

# Ice Body - Ability ID 115

## In-Game Description
"Heals 1/8 of max HP every turn in hail."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Ice Body restores 1/8 of max HP at the end of each turn during hailstorms. The healing occurs during any hail weather including natural hail, Snow Warning hail, and extended hail from Icy Rock. Provides complete immunity to hail damage. Does not heal on the first turn after switching in.

## Detailed Mechanical Explanation
*For Discord/reference use*

Ice Body is a weather-based healing ability that turns the traditionally damaging hail weather into a powerful regeneration tool, providing consistent HP recovery throughout hailstorms.

**Core Mechanics:**
- Heals 1/8 (12.5%) of maximum HP at the end of each turn during hail weather
- Provides complete immunity to hail damage (indicated by `.hailImmune = TRUE`)
- Healing is calculated as `maxHP / 8`, with a minimum of 1 HP if the calculation rounds to 0
- Uses negative damage value (`gBattleMoveDamage *= -1`) to trigger healing instead of damage
- Does not activate on the first turn after switching in (`gVolatileStructs[battler].isFirstTurn != 2`)

**Activation Requirements:**
- Must be affected by hail weather (`IsBattlerWeatherAffected(battler, WEATHER_HAIL_ANY)`)
- Cannot be at maximum HP (`CHECK_NOT(BATTLER_MAX_HP(battler))`)
- Must be able to heal (passes `CanBattlerHeal(battler)` check)
- Cannot be the first turn after switching in

**Weather Compatibility:**
- Works with all forms of hail weather:
  - Natural hail from the Hail move (8 turns base, 12 with Icy Rock)
  - Snow Warning ability hail (8 turns base, 12 with Icy Rock)
  - Any other hail-inducing effects
- Healing continues for the entire duration of the hailstorm

**Strategic Applications:**
- Transforms hail from a liability into a major advantage
- Provides excellent sustain for Ice-type Pokemon and others in hail teams
- Synergizes perfectly with Snow Warning for immediate healing setup
- Can outlast opponents through consistent recovery in extended hail battles
- Pairs well with hail-based offensive strategies for both offense and defense

**Technical Implementation:**
- Uses the `onEndTurn` hook to trigger healing at turn end
- Executes `BattleScript_RainDishActivates` for healing animation/message
- Classified as a non-breakable ability (cannot be suppressed by Mold Breaker)
- Healing amount is always positive and bypasses most healing prevention effects

**Interaction Notes:**
- The healing occurs even if the Pokemon would normally resist Ice-type moves
- Healing is blocked by standard healing prevention (Heal Block, etc.)
- Does not stack with other end-of-turn healing abilities
- The switch-in restriction prevents immediate healing exploitation