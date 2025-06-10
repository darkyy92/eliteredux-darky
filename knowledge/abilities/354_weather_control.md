# Weather Control (Ability #354)

**In-Game Description**: "Negates all weather based moves from enemies."

## Extended In-Game Description (280-300 chars)
Grants complete immunity to 18 specific weather-based moves when used by opponents: Bleakwind Storm, Blizzard, Sheer Cold, Thunder, Wildbolt Storm, Hurricane, Sandsear Storm, Springtide Storm, Ominous Wind, Eerie Spell, Solar Beam, Solar Blade, Weather Ball, Revival Blessing, Depletion Beam, Fire/Water/Grass Pledge. Does not block weather-setting moves or weather-boosted moves.

## Detailed Mechanical Explanation

### Core Mechanics
Weather Control provides complete immunity to moves flagged as `FLAG_WEATHER_BASED` in the game's code. This is a hardcoded list of 18 specific moves, not a dynamic weather interaction.

### Implementation Details
- **Hook**: Uses `onImmune` (same as Delta Stream)
- **Trigger**: When opponent uses a move with `FLAG_WEATHER_BASED` flag
- **Effect**: Complete immunity - move fails with "It doesn't affect [Pokémon]..."
- **Breakable**: Can be bypassed by Mold Breaker and similar abilities

### Complete List of Blocked Moves
1. **Bleakwind Storm** - Ice-type special move
2. **Blizzard** - Ice-type special move (normally gets accuracy boost in hail)
3. **Depletion Beam** - Normal-type special move
4. **Eerie Spell** - Psychic-type special move
5. **Fire Pledge** - Fire-type special pledge move
6. **Grass Pledge** - Grass-type special pledge move
7. **Hurricane** - Flying-type special move (normally gets accuracy boost in rain)
8. **Ominous Wind** - Ghost-type special move with stat boost chance
9. **Revival Blessing** - Normal-type status move (revival)
10. **Sandsear Storm** - Ground-type special move
11. **Sheer Cold** - Ice-type OHKO move
12. **Solar Beam** - Grass-type special move (normally charges faster in sun)
13. **Solar Blade** - Grass-type physical move (physical Solar Beam)
14. **Springtide Storm** - Fairy-type special move
15. **Thunder** - Electric-type special move (normally gets accuracy boost in rain)
16. **Water Pledge** - Water-type special pledge move
17. **Weather Ball** - Normal-type special move (changes type with weather)
18. **Wildbolt Storm** - Electric-type special move

### What It Does NOT Block
- Weather-setting moves (Rain Dance, Sunny Day, etc.)
- Moves that get power boosts from weather (Water moves in rain, Fire moves in sun)
- Moves with weather-dependent secondary effects (Morning Sun healing varies)
- Any moves not in the above list of 18

### Comparison to Similar Abilities
- **Delta Stream**: Also blocks these 18 moves PLUS sets Strong Winds weather
- **Cloud Nine/Air Lock**: Suppress weather effects but don't block specific moves
- **Magic Guard**: Prevents weather damage but doesn't block weather moves

### Strategic Implications
Weather Control is a defensive ability that hard-counters specific moves rather than weather conditions. It's particularly effective against:
- Rain teams relying on Thunder
- Sun teams using Solar Beam/Solar Blade
- Hail teams with Blizzard
- Teams using the powerful Storm moves (Bleakwind, Sandsear, Springtide, Wildbolt)

The ability name is somewhat misleading - it doesn't control weather conditions but rather blocks a specific set of moves that happen to be weather-related in theme or function.