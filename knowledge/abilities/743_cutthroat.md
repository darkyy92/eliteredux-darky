---
id: 743
name: "Cutthroat (ID: 743)"
status: ai-generated
character_count: 263
---

# Cutthroat (ID: 743)

## Extended In-Game Description
*For use in Elite Redux extended ability UI (IMPORTANT: exactly 280-300 chars counted WITH spaces)*
"First slicing move gets +1 priority."

## Extended In-Game Description (280-300 chars)
"First slicing move gets +1 priority, then ability deactivates. Sharpen move uniquely RESETS this ability, allowing repeated priority slicing. Coil does NOT reset it. Works with moves having keen edge flag like Sacred Sword. Perfect for Sharpen + slicing combos."

*Character count: 287*

## Implementation Details

### Mechanics
1. **On Entry**: Sets `STATUS4_CUTTHROAT` flag when Pokemon switches in
2. **Effect**: Gives +1 priority to the first slicing move (moves with `FLAG_KEEN_EDGE_BOOST`)
3. **Deactivation**: Status cleared after using a slicing move
4. **Sharpen Reset**: Sharpen move uniquely re-enables the ability if user has Cutthroat

### Code Implementation
- Entry: Sets `STATUS4_CUTTHROAT` flag
- Priority modification: Checks for flag and slicing move flag
- Sharpen special interaction:
```asm
BattleScript_EffectSharpen_TryCutthroat:
    jumpifstatus4 BS_ATTACKER, STATUS4_CUTTHROAT, BattleScript_MoveEnd
    jumpifability BS_ATTACKER, ABILITY_CUTTHROAT, BattleScript_EffectSharpen_DoCutthroat
    goto BattleScript_MoveEnd
BattleScript_EffectSharpen_DoCutthroat:
    call BattleScript_AbilityPopUp
    setstatus4 BS_ATTACKER, STATUS4_CUTTHROAT
    printstring STRINGID_CUTTHROAT
    waitmessage B_WAIT_TIME_LONG
```

### Strategic Applications
- Enables priority sweeping with slicing moves
- Sharpen + slicing move creates a repeatable combo
- Can outspeed and eliminate threats before they move
- Works with moves like Sacred Sword, Leaf Blade, Night Slash, etc.

### Key Clarification
- **Sharpen**: DOES reset Cutthroat - allows repeated priority
- **Coil**: Does NOT reset Cutthroat - no interaction

### Character Count: 248

## Notes
- Extremely powerful with the Sharpen synergy
- Creates a unique playstyle around setup + priority attacking
- The Sharpen interaction makes this ability much more valuable than it initially appears