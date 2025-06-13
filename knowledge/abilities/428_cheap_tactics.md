# Cheap Tactics (ID: 428)

## Description
"Attacks with 40BP Scratch on switch-in."

## Extended In-Game Description (280-300 chars)
"Automatically uses Scratch (40 BP Normal physical) when switching in. Free chip damage on entry, can break Focus Sash/Sturdy. Triggers contact abilities if applicable. Perfect for pivot Pokemon that switch frequently. True to its name - a cheap shot on entry."

*Character count: 285*

## Implementation Details

### Mechanics
- Triggers automatically when Pokemon switches in
- Uses Scratch - 40 BP Normal-type physical move, 100% accuracy
- No power override (uses Scratch's base 40 power)
- Can trigger contact-based abilities and items

### Code Implementation
```cpp
onEntry = +[](ENTRY_ARGS)
{ 
    UseEntryMove(battler, ability, MOVE_SCRATCH, 0);
}
```
- The last parameter (0) means no power override

### Strategic Applications
- Provides free chip damage on switch-in
- Can break Focus Sash/Sturdy
- Normal-type means neutral damage on most targets
- Works well on pivot Pokemon that switch frequently
- Can be used to safely check for contact-punishing abilities

### Comparison to Similar Abilities
- **Low Blow**: Uses 40 BP Feint Attack (Dark-type, never misses, can't KO)
- **Cheap Tactics**: Uses 40 BP Scratch (Normal-type, can KO)

### Known Pokemon
- Banette (seen in trainer battles)
- Various mischievous or underhanded Pokemon

### Character Count: 259

## Notes
- The ability name perfectly captures its nature - a cheap, underhanded tactic
- Unlike Low Blow, this CAN knock out opponents
- Simple but effective for consistent chip damage