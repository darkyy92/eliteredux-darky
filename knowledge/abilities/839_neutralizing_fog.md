---
id: 839
name: Neutralizing Fog
status: ai-generated
character_count: 290
---

# Neutralizing Fog

## Basic Description
Uses Defog on entry.

## Detailed Description
When this Pokemon switches in, it automatically uses Defog without consuming a turn. This removes all entry hazards from both sides (Spikes, Stealth Rock, Toxic Spikes, Sticky Web, Caltrops) and clears opponent's screens (Reflect, Light Screen, Aurora Veil, Mist, Safeguard, Smokescreen).

## Key Mechanics
- **Trigger**: Activates immediately upon switching in
- **Effect**: Uses the move Defog automatically
- **Cost**: No turn or PP consumed
- **Target**: Affects both sides of the field
- **Removes Hazards**: Clears all entry hazards from both sides:
  - Spikes (all layers)
  - Stealth Rock (all types)
  - Toxic Spikes (all layers)
  - Sticky Web
  - Caltrops
- **Removes Screens**: Clears opponent's protective barriers:
  - Reflect
  - Light Screen
  - Aurora Veil
  - Mist
  - Safeguard
  - Smokescreen
- **Does NOT Remove**: Your own team's screens remain intact

## Competitive Analysis
This ability provides excellent hazard control without consuming a moveslot or turn. It's particularly valuable on pivot Pokemon that switch frequently, as each switch-in clears the field. However, it also removes your own hazards, making it a double-edged sword in hazard-stacking strategies.

## Synergies
- Works well on defensive pivots that switch often
- Pairs nicely with U-turn/Volt Switch/Flip Turn users
- Complements teams that don't rely on their own hazards
- Useful on leads to clear opposing hazards immediately

## Counterplay
- Set hazards after this Pokemon switches out
- Use abilities like Magic Bounce to prevent hazard removal
- Minimize switching to reduce Defog activations
- Take advantage of the fact it clears user's hazards too

## Notes
- Based on the UseEntryMove function in abilities.cc
- The Defog move normally also lowers target's evasion, but this effect doesn't apply when used via ability
- The ability cannot be suppressed or negated by typical means