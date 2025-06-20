# Sturdy - Ability ID 5

## In-Game Description
"At full HP, cannot be KO in one hit, stays at 1 HP instead."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

When at full HP, this Pokémon will survive any single attack with at least 1 HP remaining. Does not protect against multi-hit moves, status damage, or consecutive attacks. Perfect for hazard leads to guarantee Stealth Rock, or Shell Smash users for a safe setup turn at full health.

*Character count: 282*

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Sturdy provides a guaranteed survival mechanism when at full HP:

1. **Activation Conditions**
   - Pokémon must be at exactly 100% HP
   - Incoming attack would normally KO the Pokémon
   - Not already endured through other means (Endure move, Focus Sash)
   - Move is not False Swipe or similar effect

2. **Effect**
   - Damage is reduced to leave the Pokémon at exactly 1 HP
   - Ability popup appears showing "Sturdy"
   - Message displays "[Pokémon] endured the hit!"
   - Sets internal flag `gTurnStructs[gBattlerTarget].sturdied = TRUE`

### Technical Implementation

**Battle Script Commands** (`src/battle_script_commands.c`):
```c
if (gBattleMons[gBattlerTarget].ability == ABILITY_STURDY 
    && BATTLER_MAX_HP(gBattlerTarget)
    && !gTurnStructs[gBattlerTarget].sturdied) {
    // Reduce damage to leave at 1 HP
    RecordAbilityBattle(gBattlerTarget, ABILITY_STURDY);
    gTurnStructs[gBattlerTarget].sturdied = TRUE;
}
```

### Interactions with Other Abilities/Mechanics

**Bypassed by:**
- **Mold Breaker/Teravolt/Turboblaze**: Ignores Sturdy completely
- **Multi-hit moves**: Each hit calculates separately
- **Entry hazards**: Not direct attacks
- **Status damage**: Poison, burn, etc.
- **Recoil/Life Orb**: Self-inflicted damage

**Similar effects:**
- **Focus Sash**: Item version, one-time use
- **Focus Band**: 10% chance version
- **Endure**: Move version, protects at any HP
- **Immovable Object**: Includes Sturdy effect plus Impenetrable

### Strategic Implications

1. **Lead Pokémon**: Guarantees at least one action
2. **Hazard Setting**: Ensures Stealth Rock/Spikes get up
3. **Counter/Mirror Coat**: Survive and retaliate
4. **Shell Smash**: Safe setup at full HP
5. **Explosion/Self-Destruct**: Guaranteed activation

### AI Behavior
- Recognizes Sturdy as high-priority threat
- Will use pivot moves to break Sturdy
- Prioritizes multi-hit moves against Sturdy users
- May switch to preserve Sturdy for later

### Example Usage Patterns

**Offensive Lead**:
- Sturdy → Stealth Rock → Explosion
- Guarantees hazards and damage

**Setup Sweeper**:
- Sturdy → Shell Smash → Sweep
- Safe setup opportunity

**Revenge Killer**:
- Sturdy → Survive hit → Priority move
- Reliable revenge killing

### Common Users
- Forretress (hazard setter)
- Crustle (Shell Smash user)
- Golem (Explosion user)
- Donphan (defensive pivot)
- Various Rock/Steel types

### Competitive Usage Notes
- A-tier ability for specific roles
- Essential for suicide leads
- Enables risky setup strategies
- Less valuable on defensive Pokémon
- Berry Juice combo for double Sturdy in Little Cup

### Counters
- **Multi-hit moves**: Bullet Seed, Rock Blast, etc.
- **Entry hazards**: Break Sturdy on switch-in
- **Sandstorm/Hail**: Weather damage after survival
- **Priority moves**: Finish off after Sturdy activates
- **Mold Breaker**: Completely ignores Sturdy

### Synergies
- **Shell Smash**: Safe setup opportunity
- **Custap Berry**: Priority after Sturdy activation
- **Weakness Policy**: Survive super effective hit
- **Endeavor**: Bring opponent to 1 HP
- **Red Card**: Force switch after surviving

### Version History
- **Gen III-IV**: Only prevented OHKO moves (Sheer Cold, etc.)
- **Gen V+**: Added full HP survival mechanism
- **Elite Redux**: Functions as Gen V+ version with enhanced integration