---
id: 857
name: Royal Decree
status: ai-generated
character_count: 285
---

# Royal Decree (Ability ID: 857)

## Base Description
"Queenly Majesty + Glare on entry once per battle."

## Extended In-Game Description
"Automatically uses Glare on entry once per battle, paralyzing a random opponent. Additionally, provides royal protection that blocks all enemy priority moves targeting this Pokémon or its allies, similar to Queenly Majesty's regal authority over the battlefield."

Character count: 285

## Mechanical Analysis

### Primary Effects
1. **Entry Move**: Uses Glare automatically when entering battle
   - Targets a random opponent
   - Paralysis effect that ignores type immunity (Normal-type move that can paralyze Electric-types)
   - Only triggers once per battle via SingleUseAbilityCounter mechanism
   - 100% accuracy, 20 PP equivalent

2. **Priority Move Blocking**: Inherited from Queenly Majesty
   - Blocks all enemy priority moves (moves with priority > 0)
   - Protection extends to allies (onImmuneFor = APPLY_ON_ALLY)
   - Only blocks moves from opposing team, not allies
   - Does not activate during extra attacks (gProcessingExtraAttacks check)

### Implementation Details
- **Breakable**: Yes - can be suppressed by Mold Breaker and similar abilities
- **Immunity Script**: Uses BattleScript_DazzlingProtected for priority move blocking
- **Single Use Counter**: Prevents multiple Glare uses if the Pokémon switches out and back in during the same battle
- **Code Structure**: Combination ability that delegates priority blocking to QueenlyMajesty implementation

## Battle Applications
- **Lead Pokémon Utility**: Excellent for lead positions to immediately cripple fast threats
- **Support Role**: Protects team from priority moves like Quick Attack, Bullet Punch, Sucker Punch
- **Speed Control**: Paralysis provides long-term speed control beyond the initial entry
- **Anti-Priority Meta**: Hard counters priority-based strategies and revenge killers

## Interactions
- **Type Immunity Bypass**: Glare can paralyze Electric-types due to EFFECT_PARALYZE_IGNORE_TYPE
- **Substitute Interaction**: Priority move blocking works through Substitute
- **Multi-Battle Persistence**: Single-use counter may reset between different battle formats
- **Team Protection**: Allies benefit from priority move immunity while this Pokémon is active

This ability combines immediate battlefield control through guaranteed paralysis with ongoing strategic value via priority move denial, making it exceptionally powerful for both offensive and defensive team compositions.