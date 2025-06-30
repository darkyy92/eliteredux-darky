---
id: 698
name: Pinnacle Blade
status: ai-generated
character_count: 298
---

# Pinnacle Blade - Ability ID 698

## In-Game Description
Slashing moves always hit and break protection and barriers.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

This elite ability makes the user an unstoppable blade master. All slashing moves bypass accuracy checks for guaranteed hits and ignore protective measures, shattering screens like Reflect and Light Screen, destroying Substitutes, and penetrating Protect. Only affects moves with the slashing flag.

## Detailed Mechanical Explanation

### Mechanics
- **Accuracy Override**: Slashing moves never miss regardless of accuracy modifiers or evasion
- **Barrier Breaking**: Destroys Light Screen, Reflect, and Aurora Veil when using slashing moves  
- **Substitute Destruction**: Removes target's Substitute immediately upon hit
- **Protection Bypass**: Ignores Protect, Detect, and similar defensive moves
- **Move Requirement**: Only works with moves that have the FLAG_KEEN_EDGE_BOOST flag

### Code Implementation
The ability works through two main mechanisms:
1. **onInfiltrate**: Returns INFILTRATE_BREAK_SCREENS | INFILTRATE_SUBSTITUTE for slashing moves
2. **onAttacker**: Triggers after hit to remove barriers and protection effects
3. **IsBattlerProtected**: Returns FALSE for slashing moves, bypassing protection entirely