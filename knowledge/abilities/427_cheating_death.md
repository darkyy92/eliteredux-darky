# Cheating Death

**Ability ID**: 427
**Type**: Regular Ability

**In-Game Description**: "Gets no damage for the first two hits."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Negates all damage for the first 2 hits received. Works like Substitute - moves still connect and secondary effects (stat boosts, status) apply normally. Damage is simply reduced to 0. Counter decrements per hit, not per turn. Does not block non-damaging moves or entry hazards.

*Character count: 298*

## Detailed Mechanical Explanation (Discord/Reference)

**Damage Type: Substitute-style "no damage"**
- The ability blocks damage completely but does NOT prevent secondary effects
- It works like a Substitute - the move still "hits" and can trigger secondary effects, but deals 0 damage
- This is implemented in `Cmd_datahpupdate()` where it checks `RemainingNoDamageHits(gActiveBattler) > 0` and prevents the HP reduction while still allowing the move to connect

**Implementation Details:**

Counter Management:
```cpp
// In abilities.cc - CheatingDeath definition
.noDamageHits = 2,
.persistent = TRUE,

// Counter calculation
int uses = 2 - GetSingleUseAbilityCounter(battler, ability);
```

Damage Blocking Logic:
```cpp
// In battle_script_commands.c - Cmd_datahpupdate()
else if (gBattleMoveDamage > 0 && !(gHitMarker & HITMARKER_PASSIVE_DAMAGE) && RemainingNoDamageHits(gActiveBattler) > 0) {
    IncrementSingleUseAbilityCounter(gActiveBattler, GetNoDamageAbility(gActiveBattler), 1);
    if (RemainingNoDamageHits(gActiveBattler) <= 0) {
        BattleScriptCall(BattleScript_BattlerCanNoLongerEndureHits);
    }
}
```

## Trigger Conditions

- Activates when the Pokémon would take damage from an attack
- Only blocks the first 2 hits received in battle per Pokémon
- Does not activate on passive damage (poison, burn, etc.)
- Does not activate on entry hazards

## Numerical Effects

- **Hits Blocked**: Exactly 2 hits per battle
- **Damage Reduction**: 100% (damage becomes 0)
- **Counter Storage**: Persistent across switches

## Interactions

**Key Differences from Immunity:**
1. **Move still connects** - accuracy checks pass, contact effects trigger
2. **Secondary effects can still occur** - status conditions, stat changes, etc. can still happen
3. **No "immune" message** - shows hit animation but 0 damage
4. **Works against all physical damage** - not type-specific like immunities

**With Other Abilities:**
- Cannot be suppressed by Mold Breaker (no `.breakable = TRUE`)
- Works with contact-based abilities (move still makes contact)

## Special Cases

- **Entry Messages:**
  - When entering with 2 hits remaining: "X has N no damage hits!" 
  - When entering with 1 hit remaining: "X has a single no damage hit!"
  - When the last hit is used: "X can no longer endure hits!"

## Notes

- **Does NOT reset on switching** because the ability has `.persistent = TRUE`
- The counter is stored per Pokemon in the party, not per battle slot
- Once a Pokemon has used up its 2 hits, it's permanent for that battle
- This makes Cheating Death a powerful defensive ability that provides guaranteed damage immunity for exactly 2 attacks per battle, while still allowing the opponent's moves to have their secondary effects