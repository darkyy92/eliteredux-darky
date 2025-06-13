# Subdue - Ability ID 556

## In-Game Description
"Doubles stat drop effects used by this pokemon."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Subdue enhances all stat-lowering moves used by this Pokémon, doubling their effectiveness. Leer becomes as strong as Screech, while Screech drops Defense by 4 stages. Works on all stat drops including multi-stat moves. Does not affect self-inflicted stat drops or enemy abilities.

*Character count: 281*

## Detailed Mechanical Explanation
*For Discord/reference use*

**SUBDUE** is a stat manipulation ability that doubles the effectiveness of all stat-lowering effects inflicted by the user on opponents.

### Core Mechanics:
- **Effect**: Doubles all negative stat stage changes inflicted on opponents
- **Scope**: Only affects moves used by the Pokémon with Subdue
- **Target**: Only affects stat drops on opposing Pokémon
- **Stacking**: Does not stack with Simple (opponent's Simple is calculated separately)

### Stat Drop Multiplication:
1. **Single Stage Drops → Double**:
   - Growl (-1 Attack) → -2 Attack
   - Leer (-1 Defense) → -2 Defense
   - String Shot (-1 Speed) → -2 Speed
   
2. **Double Stage Drops → Quadruple**:
   - Screech (-2 Defense) → -4 Defense
   - Fake Tears (-2 Sp. Def) → -4 Sp. Def
   - Scary Face (-2 Speed) → -4 Speed

3. **Multi-Stat Moves**:
   - Intimidate-like effects: Each stat doubled independently
   - Memento (-2 Atk/Sp.Atk) → -4 Atk/Sp.Atk
   - Parting Shot (-1 Atk/Sp.Atk) → -2 Atk/Sp.Atk

### Important Interactions:
- **Does NOT affect**:
  - Self-inflicted stat drops (Close Combat, Superpower)
  - Stat drops from opponent's abilities (Intimidate on you)
  - Stat drops from items or status conditions
  - Positive stat changes
  
- **Special Cases**:
  - Clear Body/White Smoke: Still blocks the stat drop entirely
  - Contrary: Reverses the doubled drop into a doubled boost
  - Simple (on target): Calculated after Subdue (can stack to -4 from -1 base)
  - Mist/Clear Body: Prevents the stat drop as normal

### Technical Implementation:
```c
// In battle_script_commands.c - Stat animation handling
if (gBattlerAttacker != gActiveBattler && BATTLER_HAS_ABILITY(gBattlerAttacker, ABILITY_SUBDUE)) 
    flags |= STAT_CHANGE_BY_TWO;

// In battle_script_commands.c - Actual stat modification
if (!affectsUser && BattlerHasAbility(gBattlerAttacker, ABILITY_SUBDUE, FALSE) && statValue <= -1) 
    statValue *= 2;
```

### Competitive Applications:
1. **Lead Strategies**:
   - Powerful with Intimidate users for -2 Attack on switch
   - Memento becomes devastating at -4/-4
   - Parting Shot pivot strategies enhanced

2. **Support Role**:
   - Makes weak stat drops viable (Growl, Leer)
   - Excellent for setting up sweepers
   - Synergizes with Prankster for priority stat drops

3. **Move Synergies**:
   - Icy Wind: -2 Speed to all opponents
   - Snarl: -2 Sp. Attack + damage
   - Bulldoze: -2 Speed + Ground damage
   - Rock Tomb: -2 Speed + Rock damage

### Counters and Limitations:
- Clear Body/White Smoke users immune
- Defiant/Competitive punish harder (+4 instead of +2)
- Cannot affect allies (no doubles support tricks)
- No effect on status moves that don't lower stats

### Elite Redux Notes:
- Particularly powerful in Elite Redux due to increased importance of stat manipulation
- Many trainers use stat-dropping strategies that can be enhanced
- Combines well with Elite Redux's multi-ability system for additional utility