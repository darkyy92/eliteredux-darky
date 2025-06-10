# Fort Knox (Ability ID: 341)

## In-Game Description
"Blocks most damage boosting and multihit abilities."

## Extended In-Game Description (280-300 chars)
Blocks offensive abilities that boost damage or enable multi-hits when defending. Nullifies ~158 damage multipliers like Huge Power, Iron Fist, and type-boosting abilities. Prevents multi-hit abilities from activating extra hits. Only Parental Bond can bypass this defense. Pure defensive ability.

## Detailed Mechanical Explanation
**Fort Knox** is one of the most powerful defensive abilities in Elite Redux, providing comprehensive protection against offensive ability modifiers.

### Core Mechanics
Fort Knox operates by intercepting ability calculations during damage resolution:
1. When a Pokémon with Fort Knox is defending, it prevents the attacker's offensive abilities from applying
2. The ability specifically targets two hooks: `onOffensiveMultiplier` and `onParentalBond`
3. Implementation is remarkably simple: just `.fortKnox = TRUE` in the ability struct

### What Fort Knox Blocks

#### 1. Damage-Boosting Abilities (~158 abilities)
Blocks ALL abilities that use `onOffensiveMultiplier`, including:

**Type-Based Boosts:**
- Overgrow, Blaze, Torrent (1.5x when HP < 1/3)
- Swarm variants for all types
- -ate abilities (Pixilate, Refrigerate, etc.)

**Physical/Special Boosts:**
- Huge Power/Pure Power (2x Attack)
- Hustle (1.4x physical damage)
- Sheer Force (1.3x + removes secondary effects)
- Iron Fist (1.2x punching moves)
- Strong Jaw (1.5x biting moves)
- Mega Launcher (1.5x pulse/aura moves)

**Conditional Boosts:**
- Guts (1.5x physical when statused)
- Solar Power (1.5x special in sun)
- Analytic (1.3x when moving last)
- Tinted Lens (2x on not very effective moves)
- Technician (1.5x on moves ≤60 power)

**Weather/Terrain Boosts:**
- Sand Force (1.3x Rock/Ground/Steel in sand)
- Various weather-specific damage boosts

#### 2. Multi-Hit Abilities
Blocks abilities using `onParentalBond` hook:
- Ice Cold Hunter (2 hits in hail)
- Raging Boxer, Raging Moth, Raging Goddess
- Dual Wield, Dual Hammer
- Multi Headed, Hyper Aggressive
- Steel Beetle, Balloon Blitz
- Minion Control, Devourer
- And many more multi-hit variants

### Critical Exception
**Parental Bond** is the ONLY ability that bypasses Fort Knox:
```cpp
constexpr Ability ParentalBond = {
    .onParentalBond = +[](ON_PARENTAL_BOND) -> MultihitType { 
        return PARENTAL_BOND_HYPER_AGGRESSIVE; 
    },
    .resistsFortKnox = TRUE,  // This allows it to bypass Fort Knox
};
```

### Technical Implementation
The blocking occurs at two key points:

1. **In CalculateAbilityMultipliers()** (battle_util.c):
```cpp
int hasFortKnox = HasFortKnox(battlerDef);
if (!hasFortKnox) {
    // Apply offensive multipliers only if defender lacks Fort Knox
}
```

2. **In GetParentalBondType()** (battle_script_commands.c):
```cpp
int hasFortKnox = HasFortKnox(target);
ON_ABILITY(battler,
    FALSE,
    gAbilities[ability].onParentalBond && 
    (!hasFortKnox || gAbilities[ability].resistsFortKnox),
    // Apply multi-hit only if no Fort Knox OR ability resists it
)
```

### What Fort Knox Does NOT Block
- Defensive abilities (onDefensiveMultiplier)
- Status moves and their effects
- Base stat modifications (like Intimidate)
- Speed modifications
- Accuracy/Evasion changes
- Weather/terrain setup
- Entry hazards
- Priority modifications

### Strategic Implications
Fort Knox essentially neutralizes most offensive ability strategies:
- Shuts down Huge Power sweepers
- Prevents multi-hit spam strategies
- Counters weather-based attackers
- Makes the defender rely purely on base stats and moves

This makes Fort Knox Pokémon excellent defensive pivots and walls, particularly against ability-reliant offensive threats. The Parental Bond exception provides the only reliable way to break through with ability-enhanced attacks.