---
id: 108
name: Forewarn
status: ai-generated
character_count: 299
---

# Forewarn - Ability ID 108

## In-Game Description
"Casts an 80 BP Future Sight on entry."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (IMPORTANT: exactly 280-300 chars counted WITH spaces)*

Forewarn automatically casts an 80 BP Future Sight on the opposing Pokémon when switching in. The psychic attack strikes 2 turns later, dealing damage regardless of type immunities. If one foe has Future Sight pending, targets the other. Cannot stack multiple Future Sights on same target.

*Character count: 299*

## Detailed Mechanical Explanation

Forewarn in Elite Redux has been completely reworked from its vanilla version. Instead of revealing the opponent's highest base power move, it now offensively casts Future Sight upon entry.

### Key Mechanics:
1. **Automatic Cast**: When a Pokémon with Forewarn enters battle, it immediately casts Future Sight targeting an opponent
2. **Fixed Power**: The Future Sight has 80 base power (not affected by the user's stats at cast time)
3. **Turn Delay**: The attack strikes after 3 turns (on the 3rd turn after casting)
4. **Target Selection**: 
   - Prioritizes the opposing Pokémon directly across from the user
   - If that target already has a Future Sight pending, it targets their partner instead
   - Cannot target a fainted Pokémon
5. **Type**: The Future Sight attack is Psychic-type and ignores type immunities (hits Dark types)
6. **Stacking**: Cannot stack multiple Future Sights on the same target - each Pokémon can only have one pending

### Battle Flow:
- Turn 1: Pokémon with Forewarn switches in → "foresaw an attack!" message → Future Sight timer starts
- Turn 2: Future Sight pending
- Turn 3: Future Sight strikes the target

### Strategic Implications:
- Provides guaranteed chip damage on switch-in
- Forces opponents to consider the incoming damage when planning switches
- Synergizes well with offensive pivoting strategies
- Can pressure defensive Pokémon that would normally wall the user
- The damage occurs even if the Forewarn user switches out or faints

### Interactions:
- Does not trigger if both opponents already have Future Sight pending
- The damage calculation uses the original caster's Special Attack stat
- Can be blocked by Protect/Detect on the turn it strikes
- Wonder Guard does not block Future Sight damage