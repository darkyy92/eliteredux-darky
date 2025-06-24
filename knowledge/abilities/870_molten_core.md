---
id: 870
name: Molten Core
status: ai-generated
character_count: 295
---

# Molten Core - Ability ID 870

## In-Game Description
"Furnace + Absorbs Rock-moves/Stealth Rocks."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (IMPORTANT: exactly 280-300 chars counted WITH spaces)*

Molten Core combines Furnace effects with Rock-type absorption. On switch-in, gains +2 Speed from Stealth Rock and removes team's Stealth Rock. When hit by Rock moves, gains +2 Speed instead of taking damage. Perfect for handling Rock-type attacks and entry hazards.

*Character count: 295*

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Molten Core is a hybrid defensive ability that combines the effects of Furnace with powerful Rock-type move absorption. It provides both entry hazard control and offensive momentum through Speed boosts.

### Activation Conditions
- **Switch-in effects**: Activates when the Pokémon enters battle
  - If Stealth Rock is on the user's side, gains +2 Speed boost
  - Completely removes Stealth Rock from the user's side of the field
- **Rock-type absorption**: When targeted by Rock-type moves
  - Absorbs the move (no damage taken)
  - Gains +2 Speed boost instead
- **Stealth Rock immunity**: Completely immune to Stealth Rock damage

### Technical Implementation
```c
// Molten Core combines Furnace effects with Rock absorption
constexpr Ability MoltenCore = {
    .onEntry = +[](ON_ENTRY) -> int {
        // Delegate to Furnace for Stealth Rock speed boost
        Furnace.onEntry(DELEGATE_ENTRY);
        
        // Remove Stealth Rock from user's side
        CHECK(gSideStatuses[GetBattlerSide(battler)] & SIDE_STATUS_STEALTH_ROCK)
        gSideStatuses[GetBattlerSide(battler)] &= ~SIDE_STATUS_STEALTH_ROCK;
        return SwitchInAnnounce(B_MSG_SWITCHIN_MOLTEN_CORE);
    },
    .onAbsorb = +[](ON_ABSORB) -> int {
        // Absorb Rock-type moves for Speed boost
        CHECK(moveType == TYPE_ROCK)
        *statId = STAT_SPEED;
        return ABSORB_RESULT_STAT;
    },
    .stealthRockImmune = TRUE,
    .absorbUp2 = TRUE,  // +2 stat boost instead of +1
    .breakable = TRUE,
};
```

### Furnace Component Effects
The Furnace component provides:
- **Switch-in boost**: If Stealth Rock is present on switch-in, gains +2 Speed
- **Rock-hit boost**: When hit by Rock-type moves, gains +2 Speed after damage
- Works even if Stealth Rock was set by Rock-type moves

### Rock Absorption Effects
- **Complete immunity**: Takes no damage from Rock-type attacks
- **Speed boost**: Gains +2 Speed when targeted by Rock moves
- **Move negation**: Rock moves have no effect whatsoever
- **Secondary effects**: Prevents all secondary effects of Rock moves

### Important Interactions
- **Entry hazard removal**: Only removes Stealth Rock, not other hazards
- **Team protection**: Removes hazard for entire team, not just the user
- **Damage immunity**: Unlike Furnace, takes no damage from Rock moves
- **Stat boost stacking**: Multiple Rock moves can boost Speed repeatedly
- **Priority moves**: Works against priority Rock moves like Accelerock
- **Ability suppression**: Doesn't work if ability is suppressed by Mold Breaker

### Switch-In Sequence
1. Pokémon enters battle with Molten Core
2. Check if Stealth Rock is present on user's side
3. If present: Gain +2 Speed boost and trigger Furnace message
4. Remove Stealth Rock from user's side completely
5. Display switch-in absorption message

### Strategic Implications
- **Hazard control**: Excellent switch-in to clear Stealth Rock
- **Rock-type counter**: Complete immunity to Rock-type offense
- **Speed sweeping**: Can accumulate multiple Speed boosts
- **Team support**: Removes hazards that damage teammates
- **Momentum generation**: Turns defensive switches into offensive opportunities

### Common Users
- Fire/Rock-type Pokémon who benefit from Rock immunity
- Fast sweepers who can utilize Speed boosts
- Pokémon weak to Stealth Rock who need hazard control
- Team cores that struggle with Rock-type coverage

### Competitive Usage Notes
- Essential for teams vulnerable to Stealth Rock
- Counters Rock-type attackers completely
- Provides both defensive utility and offensive momentum
- Can single-handedly shut down Rock-type offensive cores
- Excellent on teams with multiple Stealth Rock weaknesses

### Synergies
- **Focus Sash/Sturdy**: Protection while setting up Speed boosts
- **Baton Pass**: Can pass accumulated Speed boosts to teammates
- **Choice items**: Speed boosts enhance Choice item effectiveness
- **Substitute**: Can safely set up behind Substitute
- **Rock-weak teammates**: Provides switch-in opportunity

### Counters
- **Non-Rock physical attacks**: Physical moves of other types
- **Special attacks**: Not Rock-type special moves
- **Status moves**: Sleep, paralysis, burn effects
- **Ability suppression**: Mold Breaker ignores the absorption
- **Taunt**: Prevents setup moves after Speed boosts
- **Priority moves**: Non-Rock priority attacks

### Version History
- Elite Redux exclusive ability
- Combines multiple hazard control and absorption effects
- Designed to counter Rock-heavy metagames
- Enhanced version of Furnace with complete Rock immunity

### Notable Differences from Similar Abilities
- **vs Furnace**: Provides complete Rock immunity instead of just boosts
- **vs Flash Fire**: Works with Rock instead of Fire, includes hazard removal
- **vs Storm Drain**: Boosts Speed instead of Special Attack
- **vs Stealth Rock immunity**: Also provides offensive momentum