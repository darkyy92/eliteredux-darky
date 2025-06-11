# Low Blow (ID: 384)

## Description
"Attacks with 40BP Feint Attack on switch-in."

## Extended Description
"Uses 40 BP Feint Attack on switch-in (reduced from 80 BP). Dark-type, never misses, can't KO (falseSwipe). Provides guaranteed chip damage when entering battle. Targets random foe automatically. Good for pivot strategies and entry hazard synergy."

## Implementation Details

### Mechanics
- Triggers automatically when Pokemon switches in
- Uses Feint Attack (normally 80 BP) reduced to 40 BP
- Dark-type physical move that never misses
- Has `falseSwipe` property - cannot knock out opponents
- Targets selected automatically (first available opposing Pokemon)

### Code Implementation
```cpp
onEntry = +[](ENTRY_ARGS)
{ 
    UseEntryMove(battler, ability, MOVE_FEINT_ATTACK, 40);
}
```

### Strategic Applications
- Free chip damage on every switch-in
- Dark-type provides good neutral coverage
- Cannot miss ensures consistent damage
- Cannot KO makes it safe to use without accidentally eliminating setup fodder
- Excellent for pivot strategies with U-turn/Volt Switch
- Synergizes with entry hazards for cumulative switch punishment

### Known Pokemon
- Persian (Alolan form) - as innate ability
- Psyduck Redux - as changeable ability  
- Froslass Redux - as innate ability
- Froslass Redux Mega - as innate ability
- Pansear Redux - as innate ability
- Simisear Redux - as innate ability
- Greninja Battle Bond - as changeable ability

### Character Count: 246

## Notes
- Functions as an automatic offensive entry hazard
- The 40 BP is enough to break Focus Sash/Sturdy
- Works well on offensive pivot Pokemon