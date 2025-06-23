---
id: 132
name: Friend Guard
status: ai-generated
character_count: 291
---

# Friend Guard - Ability ID 132

## In-Game Description
"Reduces damage that ally takes by 50% in double battles."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (IMPORTANT: exactly 280-300 chars counted WITH spaces)*

Friend Guard provides powerful team support by reducing damage taken by your ally Pokémon by 50% in double battles. This protective aura only works when both Pokémon are active and conscious on the field. Does not stack with multiple Friend Guard users but combines with other damage reduction.

*Character count: 291*

## Detailed Mechanical Explanation

Friend Guard is a defensive support ability that works exclusively in double battles. When a Pokémon with Friend Guard is on the field, its ally receives a 50% damage reduction from all incoming attacks.

### Key Mechanics:
- **Damage Reduction**: Reduces damage taken by the ally by 50% (0.5x multiplier)
- **Battle Format**: Only functions in double battles
- **Range**: Affects only the direct ally (partner Pokémon on the same side)
- **Passive Effect**: Always active as long as the Friend Guard user is conscious
- **Stacking**: Does not stack with multiple Friend Guard users on the same team
- **Combination**: Can stack multiplicatively with other damage reduction effects like Light Screen, Reflect, or defensive abilities

### Important Notes:
- The ability user (Pokémon with Friend Guard) does not receive any damage reduction themselves
- The protection is lost if the Friend Guard user faints or switches out
- Works against all damage types (physical, special, and fixed damage moves)
- In Elite Redux, this ability also stacks with Caretaker, another ally-protecting ability that provides the same 50% damage reduction

### Competitive Usage:
Friend Guard is highly valuable in double battle formats where protecting key team members is crucial. It's particularly effective when:
- Paired with frail but powerful sweepers who need protection
- Supporting setup sweepers during their boost turns
- Protecting Pokémon with important field effects or support moves
- Combined with redirection moves like Follow Me or Rage Powder for maximum ally protection

### Code Implementation:
The ability is implemented in `battle_util.c` where it applies a 0.5x modifier to damage calculations when the target's ally has Friend Guard. The check occurs during damage calculation and requires the Friend Guard user to be alive and active on the field.