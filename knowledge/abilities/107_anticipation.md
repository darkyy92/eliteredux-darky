---
id: 107
name: Anticipation
status: ai-generated
character_count: 285
---

# Anticipation - Ability ID 107

## In-Game Description
"Senses Super-effective moves. Dodges one Super-effective hit."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (IMPORTANT: exactly 280-300 chars counted WITH spaces)*

Anticipation alerts the Pokémon when facing opponents with super-effective moves on switch-in. This heightened awareness grants the ability to automatically dodge the first super-effective hit received in battle. After dodging once, the effect is used up. Works against all damage types.

*Character count: 285*

## Detailed Mechanical Explanation

Anticipation functions as both a detection and defensive ability in Elite Redux:

### Detection Phase (On Entry)
- When the Pokémon enters battle, it scans all opposing Pokémon's movesets
- Checks each move for type effectiveness against the user
- If any opponent has a move that would deal 2x or greater damage, triggers an alert
- The alert is displayed as a switch-in message to inform the player

### Defensive Phase
- Grants a one-time automatic dodge against the first super-effective move
- This dodge effect persists until used (marked as `persistent = TRUE` in code)
- Works against both physical and special super-effective moves
- The dodge completely negates all damage from that one attack
- After successfully dodging once, the protective effect is consumed

### Technical Implementation Details
- The ability is marked as `breakable = TRUE`, meaning it can be suppressed by abilities like Mold Breaker
- The detection checks type effectiveness multipliers of 2.0 or greater (using `UQ_4_12(2.0)` fixed-point math)
- Scans moves from all living opponents on the opposing side
- The switch-in announcement uses the message `B_MSG_SWITCHIN_ANTICIPATION`

### Strategic Implications
- Provides valuable scouting information about opponent movesets
- Offers a safety net against one super-effective hit
- Particularly useful for Pokémon with multiple weaknesses
- The dodge mechanic makes it a hybrid informational/defensive ability
- Unlike vanilla Pokémon's version, Elite Redux's Anticipation provides actual battle protection