---
id: 678
name: Fluffiest
status: ai-generated
character_count: 299
---

# Fluffiest

**ID:** 678  
**Type:** Defensive  
**Breakable:** Yes  

## Short Description
Quarters contact damage taken. 4x weak to fire.

## Extended Description
This ability makes the Pokemon extremely fluffy and soft, providing exceptional protection against physical contact moves by reducing contact damage by 75%. However, this incredible fluffiness comes with a significant drawback - the Pokemon becomes vulnerable to fire attacks, taking double damage.

## Technical Implementation
- `onDefensiveMultiplier`: Applies 0.5x multiplier to contact damage and 2.0x multiplier to Fire-type moves
- Breakable ability that can be suppressed by Mold Breaker and similar effects