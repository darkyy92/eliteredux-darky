---
id: 688
name: Huge Wings
status: ai-generated
character_count: 286
---

# Huge Wings - Ability ID 688

## In-Game Description
Huge Wings ability effects.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Combines the flight mastery of giant wings with magical levitation. Boosts all Flying-type moves by 25% and grants a 30% power increase to air-based moves like Fly, Bounce, and Sky Attack. Provides complete immunity to Ground-type moves and hazards while floating above the battlefield.

## Detailed Mechanical Explanation

### Mechanics
- **Flying-type moves:** 1.25x damage multiplier
- **Air-based moves:** 1.3x damage multiplier  
- **Ground immunity:** Cannot be hit by Ground-type moves
- **Hazard immunity:** Unaffected by Spikes, Toxic Spikes, and Sticky Web
- **Breakable:** Can be suppressed by Mold Breaker, Turboblaze, and Teravolt
- **Levitate flag:** Grants full Ground-type immunity and hazard protection

### Implementation Notes
This ability combines two separate effects:
1. **Giant Wings component:** Provides 1.3x damage to air-based moves
2. **Levitate component:** Provides 1.25x damage to Flying-type moves and immunity to Ground-type attacks

The ability is breakable, meaning it can be suppressed by abilities that ignore other abilities.