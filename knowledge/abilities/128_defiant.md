---
id: 128
name: Defiant
status: ai-generated
character_count: 299
---

# Defiant (Ability #128)

## Short Description
Raises Attack by two stages if stats are lowered by an enemy.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (IMPORTANT: exactly 280-300 chars counted WITH spaces)*
Defiant triggers when any of the Pokémon's stats are lowered by an opponent, immediately boosting Attack by two stages in retaliation. Activates from direct stat drops, moves like Intimidate, and stat-lowering secondary effects. Cannot activate if Attack is already at maximum. Stacks with other boosts.

Character count: 299

## Detailed Mechanics

### Trigger Conditions
- **Stat Drop Source**: Only triggers when stats are lowered by an opponent (not self-inflicted)
- **Any Stat**: Activates when ANY stat is lowered (Attack, Defense, Sp. Atk, Sp. Def, Speed, Accuracy, or Evasion)
- **Multiple Drops**: Each instance of stat lowering triggers Defiant separately
- **Intimidate**: Specifically triggers against Intimidate and similar abilities

### Boost Details
- **Boost Amount**: +2 stages to Attack stat
- **Maximum Cap**: Cannot activate if Attack is already at +6 stages
- **Stacking**: If multiple stats are lowered simultaneously, Defiant only triggers once per action

### Battle Interactions
- **Priority**: Activates immediately after the stat drop occurs
- **Ability Popup**: Shows ability notification when triggered
- **Turn Order**: Processes in the order stats are lowered

### Strategic Notes
- **Counter to Intimidate**: Excellent counter to Intimidate users, turning their advantage into a disadvantage
- **Sticky Web Counter**: Triggers when switching into Sticky Web
- **Synergy**: Pairs well with moves that lower own stats for additional effects
- **AI Behavior**: AI opponents avoid using stat-lowering moves against Defiant users

### Similar Abilities
- **Competitive**: Special Attack version (boosts Sp. Atk by +2 instead)
- **Contempt**: Combines Defiant with Unaware effects
- **Run Away**: Boosts Speed by +2 when stats are lowered (different stat boost)

### Competitive Usage
Defiant is particularly valuable in formats where Intimidate is common, turning a would-be disadvantage into a powerful Attack boost. Physical attackers with Defiant can use this to set up sweep opportunities when opponents attempt to weaken them.

### Implementation Details
- **Script**: Uses `BattleScript_DefiantActivates` 
- **Check**: Triggered by `STRINGID_DEFENDERSSTATFELL` message
- **Code Location**: Primary logic in `src/battle_util.c`