# Pure Love

**Ability ID**: 508
**Type**: Regular Ability

**In-Game Description**: "Infatuates on contact. Heal 25% damage vs infatuated."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Infatuates on contact ignoring all gender requirements. Can infatuate genderless, same-gender, or any Pokemon unlike regular infatuation. Heals 25% of damage dealt when attacking infatuated targets. One of only two abilities (with Beautiful Music) that bypasses gender restrictions for infatuation.

*Character count: 298*

## Detailed Mechanical Explanation (Discord/Reference)

Pure Love is defined in abilities.cc (lines 5386-5400):

```cpp
constexpr Ability PureLove = {
    .onAttacker = +[](ON_ATTACKER) -> int {
        CHECK(ShouldApplyOnHitAffect(battler))
        CHECK_NOT(BATTLER_MAX_HP(battler))
        CHECK(CanBattlerHeal(battler))
        CHECK(gBattleMons[target].status2 & STATUS2_INFATUATION)

        gBattleMoveDamage = -gHpDealt / 4;  // Heal 25% of damage dealt
        if (!gBattleMoveDamage) gBattleMoveDamage = -1;
        BattleScriptCall(BattleScript_HydroCircuitAbsorbEffectActivated);
        return TRUE;
    },
    .onDefender = CuteCharm.onDefender,  // 50% chance to infatuate on contact
    .canInfatuateAny = TRUE,  // Bypasses gender restrictions
};
```

**Key Features:**
1. **Bypasses Gender Restrictions**: The `canInfatuateAny = TRUE` flag allows infatuation of any Pokémon
2. **Contact-Based Infatuation**: 50% chance to infatuate attacker on contact (like Cute Charm)
3. **Healing from Infatuated Targets**: Heals 25% of damage dealt when attacking infatuated Pokémon

## Trigger Conditions

**Infatuation Component:**
- Triggers when hit by a contact move
- 50% chance to infatuate the attacker
- Works regardless of gender compatibility

**Healing Component:**
- Triggers when Pure Love user attacks an **already infatuated** target
- Only works if the user isn't at maximum HP and can heal
- Must deal damage to trigger healing

## Numerical Effects

**Infatuation Chance:**
- **Probability**: 50% on contact moves
- **Gender Bypass**: Works on any Pokémon regardless of gender

**Healing Amount:**
- **Formula**: 25% of damage dealt to infatuated target
- **Minimum**: 1 HP if calculation results in 0
- **Type**: Healing (negative damage value)

## Interactions

**Gender Bypass Mechanics:**
The `CanInfatuate()` function in battle_util.c has this key check:
```c
if (BATTLER_HAS_ABILITY(battlerAtk, ABILITY_PURE_LOVE)) return TRUE;  // Bypasses all other checks
```

**Normal infatuation fails if:**
- Either Pokémon is genderless
- Both Pokémon have the same gender
- Target is already infatuated
- Various protections apply

**Pure Love bypasses ALL of these restrictions.**

**Comparison to Standard Cute Charm:**
- Same 50% contact infatuation chance
- BUT Pure Love can infatuate any target (gender-independent)
- Plus additional healing mechanic

## Special Cases

**The "25% damage vs infatuated" description is misleading:**
- It's actually **HEALING** 25% of damage dealt, not dealing extra damage
- The line `gBattleMoveDamage = -gHpDealt / 4;` creates negative damage (healing)
- Only triggers when attacking targets that are already infatuated

**Other Abilities with Gender-Bypass:**
- **Beautiful Music**: Also has `canInfatuateAny = TRUE` for sound moves

## Notes

**Answer to User Question: "Does the opposing mon have to be the opposite gender?"**

**For Pure Love: NO!** Pure Love can infatuate literally any Pokémon regardless of gender. This includes:
- Same-gender Pokémon
- Opposite-gender Pokémon  
- Genderless Pokémon (Magnezone, Rotom, etc.)

**For standard infatuation: YES!** Normal Attract, regular Cute Charm, etc. still require opposite genders.

This makes Pure Love significantly more powerful than regular Cute Charm, as it provides universal infatuation capability plus sustain when fighting infatuated opponents.