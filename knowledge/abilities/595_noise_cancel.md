---
id: 595
name: Noise Cancel
status: ai-generated
character_count: 289
---

# Noise Cancel - Ability ID 595

## In-Game Description
"Provides sound-based move immunity to user and allies."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Provides sound-based move immunity to the user and allies on the same side. Functions identically to Soundproof but extends protection to team members, making it invaluable in doubles battles. Blocks all moves with the FLAG_SOUND property, including Hyper Voice, Boomburst, and Bug Buzz.

## Detailed Mechanical Explanation

**Type:** Defensive Ability  
**Breakable:** Yes  

### Mechanics

- **Immunity Scope:** User and all allies on the same side
- **Protected Moves:** All moves with FLAG_SOUND property
- **Breakable:** Yes (can be bypassed by Mold Breaker-type abilities)
- **Self-Targeting:** Does not block sound moves that target the user themselves

### Implementation Details

```cpp
constexpr Ability NoiseCancel = {
    .onImmune = Soundproof.onImmune,
    .onImmuneFor = APPLY_ON_ALLY,
    .breakable = TRUE,
    .isSoundproof = TRUE,
};
```

- Uses the same immunity logic as Soundproof
- `APPLY_ON_ALLY` extends protection to teammates
- `isSoundproof = TRUE` marks it as a soundproofing ability

### Strategic Applications

### Doubles/Multi Battles
- Essential for protecting support Pokemon from opposing sound moves
- Allows safe use of Substitute without fear of sound-based bypass
- Enables team compositions vulnerable to sound moves to function effectively

### Counters Common Threats
- **Exploud/Noivern:** Complete immunity to their signature sound moves
- **Chatot:** Blocks Chatter and other sound-based attacks
- **Seismitoad:** Protects against Hyper Voice variants

### Synergies
- **Substitute Users:** Sound moves normally bypass Substitute, but this ability blocks them entirely
- **Baton Pass Teams:** Protects the entire passing chain from sound disruption
- **Support Pokemon:** Allows safe setup and support without sound move interference

### Common Sound Moves Blocked

- Hyper Voice
- Boomburst
- Bug Buzz
- Uproar
- Chatter
- Metal Sound
- Screech
- Perish Song
- Sing
- Supersonic

### Competitive Viability

**Tier:** Situational but valuable in specific metas
**Usage:** Primarily in doubles/multi battles where sound moves are prevalent
**Niche:** Counter to sound-based strategies and protection for vulnerable team compositions

### Trivia

- The only ability that extends Soundproof immunity to allies
- Particularly effective against teams built around Exploud or other sound-based sweepers
- Does not prevent the user from using sound moves themselves