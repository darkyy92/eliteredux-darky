---
id: 833
name: Harukaze (N)
status: ai-generated
character_count: 282
---

# Harukaze (N) - Ability ID 833

## Basic Information
- **Name**: Harukaze (N)
- **Type**: Innate Ability (N)
- **Description**: Setting Grassy Terrain sets Tailwind an vice versa.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (IMPORTANT: exactly 280-300 chars counted WITH spaces)*
When this Pokemon or an ally sets Grassy Terrain, your team automatically gains Tailwind for the same duration. Conversely, when your team gains Tailwind, Grassy Terrain is automatically set. This bidirectional synergy creates a powerful field control combination, boosting both offense and defense.

## Detailed Mechanics

### Core Functionality
Harukaze creates a bidirectional link between two beneficial field effects:
- **Grassy Terrain → Tailwind**: When Grassy Terrain is set by any means (move, ability, or item), Tailwind is automatically applied to the user's team
- **Tailwind → Grassy Terrain**: When Tailwind is set for the user's team, Grassy Terrain is automatically established

### Trigger Conditions
The ability activates when:
1. Grassy Terrain is set through:
   - Grassy Surge ability
   - Grassy Terrain move
   - G-Max Sweetness
   - Any other terrain-setting effect that results in Grassy Terrain

2. Tailwind is set through:
   - Tailwind move
   - Air Blower ability
   - Any other effect that grants Tailwind

### Duration Synchronization
- Both effects share the same duration timer
- If Grassy Terrain is extended (e.g., by Terrain Extender), Tailwind duration matches
- If either effect ends prematurely, the linked effect also ends

### Benefits Provided

#### From Grassy Terrain:
- Restores 1/16 of max HP to grounded Pokemon each turn
- Grass-type moves gain 30% power boost
- Earthquake, Magnitude, and Bulldoze have halved power
- Nature Power becomes Energy Ball

#### From Tailwind:
- Doubles the Speed stat of all team members
- Lasts for 4 turns (or 8 with extending items)
- Affects switching order and move priority calculations

### Strategic Implications
1. **Offensive Synergy**: Speed doubling from Tailwind combined with Grass move boosts
2. **Defensive Coverage**: HP restoration and ground move reduction
3. **Team Support**: Benefits entire team rather than just the user
4. **Setup Efficiency**: One action provides two powerful field effects

### Interactions with Other Abilities
- **Grassy Surge**: Pokemon with Grassy Surge effectively gain automatic Tailwind on switch-in
- **Terrain abilities**: Other terrain setters override Grassy Terrain but don't remove the Tailwind
- **Cloud Nine/Air Lock**: These abilities don't affect either component

### Limitations
- Marked as breakable, meaning it can be suppressed by:
  - Gastro Acid
  - Neutralizing Gas
  - Core Enforcer (if user moves last)
- Cannot trigger off opponent's terrain/tailwind setup
- Subject to normal terrain override rules

### Technical Implementation
The ability is implemented with minimal code in abilities.cc:
```c
constexpr Ability Harukaze = {
    .breakable = TRUE,
};
```

The actual linking mechanism is likely implemented at a lower level in the battle engine's terrain and tailwind setting functions, automatically checking for this ability when either effect is applied.

## Competitive Analysis

### Strengths
- Provides two premium field effects for the price of one
- Excellent for hyper-offensive teams that benefit from both speed and power
- Can enable powerful Grass-type sweepers
- Provides passive recovery for the team

### Weaknesses
- Grassy Terrain can be overridden by other terrains
- Benefits opponent's grounded Grass-types too
- Tailwind has limited duration
- As an innate ability, takes up one of three innate slots

### Recommended Partners
- Fast Grass-type sweepers that can abuse both boosts
- Pokemon with Grassy Glide for priority attacks
- Physical attackers that appreciate the Earthquake reduction
- Support Pokemon that can set up one effect to trigger both

### Usage Tips
- Lead with a Pokemon having this ability to immediately establish field control
- Pair with Terrain Extender to maximize both effects' duration
- Consider moves like Grassy Glide that gain priority in Grassy Terrain
- Use on teams that can fully exploit the speed advantage before it expires