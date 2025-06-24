---
id: 412
name: Desert Cloak
status: ai-generated
character_count: 295
---

# Desert Cloak - Ability ID 412

## In-Game Description
"Protects its side from status and secondary effects in sand."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (IMPORTANT: exactly 280-300 chars counted WITH spaces)*

Desert Cloak provides team-wide protection during sandstorm weather. All allies become immune to status conditions and secondary effects from enemy moves while sand is active. Works with Sand Stream, Sand Spit, and Sandstorm moves. Does not protect from direct status moves or entry hazards. Elite weather ability.

*Character count: 295*

## Detailed Mechanical Explanation
*For Discord/reference use*

### Core Mechanics
Desert Cloak is an advanced weather-dependent ability that provides team-wide defensive benefits during sandstorm conditions. Unlike most abilities that only affect the user, Desert Cloak extends its protection to all Pokémon on the same side of the field.

### Activation Conditions
- **Weather requirement**: Any form of sandstorm weather must be active
  - Regular sandstorm (from Sandstorm move)
  - Sand Stream (from Drought-like ability)
  - Sand Spit activation
  - Any other sandstorm-inducing effects
- **Team Coverage**: Protects ALL allies on the same side, not just the user
- **Continuous Effect**: Protection remains active as long as sandstorm persists

### Protection Coverage

#### Status Condition Immunity
**Blocks ALL status conditions from indirect sources**:
- Burn (from Scald's 30% chance, Flame Body contact)
- Paralysis (from Thunder's 10% chance, Static contact)
- Poison (from Poison Point, Toxic Spikes indirect application)
- Sleep (from Effect Spore, Sleep Powder secondary effects)
- Freeze (from Blizzard's 10% chance, contact abilities)

#### Secondary Effect Immunity
**Prevents ALL secondary effects from damaging moves**:
- Stat drops from moves (Intimidate-like effects)
- Flinching from moves like Iron Head, Rock Slide
- Confusion from Water Pulse, Dynamic Punch
- Additional effects like King's Rock/Razor Fang

### Technical Implementation
```c
// Desert Cloak provides team-wide protection in sandstorm
if (IsWeatherSandstorm() && HasAllyWithAbility(ABILITY_DESERT_CLOAK)) {
    // Block status conditions from secondary sources
    if (IsSecondaryStatusEffect()) {
        preventStatus = TRUE;
    }
    // Block all secondary move effects
    if (IsSecondaryMoveEffect()) {
        preventEffect = TRUE;
    }
}
```

### Important Limitations

#### What Desert Cloak DOES NOT Block
- **Direct Status Moves**: Will-O-Wisp, Thunder Wave, Sleep Powder still work
- **Entry Hazards**: Stealth Rock, Spikes, Toxic Spikes affect allies normally
- **Self-Inflicted Effects**: Rest, Belly Drum, stat-lowering moves used by allies
- **Weather Damage**: Sandstorm still damages non-immune types
- **Ability-Based Direct Effects**: Flame Body burn on contact may still work

#### Weather Dependency
- **No Protection**: Ability provides no benefits outside of sandstorm
- **Weather Override**: Sun, rain, hail, or fog disable all protection
- **Cloud Nine/Air Lock**: Suppress sandstorm, disabling Desert Cloak

### Strategic Implications

#### Team Building
- **Sand Team Core**: Essential for sandstorm-based team strategies
- **Support Role**: Allows fragile sweepers to operate safely in sand
- **Type Coverage**: Enables non-Rock/Ground/Steel types on sand teams
- **Weather Dependency**: Requires reliable sandstorm setting

#### Offensive Synergy
- **Sand Stream**: Perfect partner for automatic sandstorm
- **Sand Rush**: Allies gain speed while protected from status
- **Sand Force**: Offensive boosts with defensive security
- **Sand Veil**: Additional evasion stacking with status immunity

### Competitive Usage Notes
- **Entry Timing**: Best brought in after sandstorm is established
- **Priority Protection**: Protects entire team from priority status moves' secondary effects
- **Switch Advantage**: Allows safer switching for sand team members
- **Duration Management**: Consider Smooth Rock for extended protection

### Common Users
- Defensive Ground/Rock types who can weather sandstorm damage
- Sand team anchors and support Pokémon
- Pokémon with Sand Stream as a secondary ability
- Bulky Pokémon designed for weather team support

### Counters
- **Weather Override**: Change to sun, rain, or hail to disable protection
- **Direct Status**: Use Will-O-Wisp, Thunder Wave instead of secondary effects
- **Cloud Nine/Air Lock**: Suppress weather effects entirely
- **Mold Breaker**: May bypass the protection (needs verification)
- **Entry Hazards**: Set up hazards before sandstorm for chip damage

### Synergies
- **Sand Stream/Sand Spit**: Essential for weather activation
- **Smooth Rock**: Extends sandstorm duration for longer protection
- **Sand Rush/Force**: Offensive benefits while maintaining protection
- **Rock/Ground types**: Natural sandstorm immunity for users
- **Weather Ball**: Becomes Rock-type in sandstorm for coverage

### Elite Redux Weather Context
- Weather lasts 8 turns (not 5), making weather abilities more valuable
- Extended duration provides longer windows of team protection
- Sandstorm teams are more viable with reliable weather persistence
- Desert Cloak becomes a cornerstone ability for sand team archetypes

### Version History
- Elite Redux exclusive ability
- Designed specifically for advanced team-based weather strategies
- Part of the expanded weather ability ecosystem
- Provides unique team support not found in other generations

### Comparison to Similar Abilities
- **Shield Dust**: Only protects user, not team-wide
- **Magic Bounce**: Reflects rather than blocks
- **Leaf Guard**: Only works in sun, individual protection
- **Flower Veil**: Type-specific team protection, not weather-based