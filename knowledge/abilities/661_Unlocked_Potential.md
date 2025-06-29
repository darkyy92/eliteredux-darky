---
id: 661
name: Unlocked Potential
status: ai-generated
character_count: 279
---

# Unlocked Potential - Ability ID 661

## In-Game Description
Inner Focus + Berserk.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*
This hybrid ability combines Inner Focus precision with Berserk fury. When hit below half HP, raises the highest attacking stat by one stage. Also provides taunt immunity and makes Focus Blast always hit, perfect for Pokemon seeking defensive resilience and offensive precision.

## Detailed Mechanical Explanation

### Technical Implementation
- **onDefender**: When hit and HP falls to 50% or below, raises highest attacking stat (Attack or Special Attack) by 1 stage (inherited from Berserk)
- **onAccuracy**: Focus Blast bypasses accuracy checks and always hits (inherited from Inner Focus)  
- **tauntImmune**: Complete immunity to taunt-based moves
- **breakable**: Not affected by abilities like Mold Breaker

### Synergies
Works exceptionally well with:
- Focus Blast users seeking guaranteed accuracy
- Mixed attackers benefiting from situational stat boosts
- Pokemon with naturally high HP pools to safely reach the activation threshold
- Defensive sets that can survive to low HP consistently