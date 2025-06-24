---
id: 600
name: Brawling Wyvern
status: ai-generated
character_count: 280
---

## Brawling Wyvern (Ability ID: 600)

### Core Mechanics
Brawling Wyvern combines No Guard's perfect accuracy with Dragon-type move enhancement. All moves used by and against this Pokémon will never miss, ignoring accuracy and evasion modifiers. Dragon-type moves gain Iron Fist treatment, boosting power by 30% and enabling interactions with punching-move mechanics like Punching Glove's contact negation.

### Extended Description (280 characters)
Guarantees perfect accuracy for all moves used by and against this Pokémon. Dragon-type moves are treated as punching moves, gaining 30% power boost and punch-item interactions. This transforms Dragon moves into powerful offensive options while maintaining tactical reliability.

### Strategic Applications
- **Offensive Enhancement**: Dragon-type moves receive significant power boost
- **Accuracy Guarantee**: High-power, low-accuracy moves become reliable
- **Item Synergy**: Dragon moves work with Punching Glove for contactless attacks
- **Defensive Vulnerability**: Opponent's moves also gain perfect accuracy
- **Type Coverage**: Makes Dragon STAB more threatening

### Technical Implementation
- **No Guard Effect**: `.onAccuracy = NoGuard.onAccuracy`
- **Dragon-Punch Conversion**: `IsIronFistBoosted()` returns TRUE for Dragon-type moves
- **Power Multiplier**: Iron Fist applies 1.3x damage multiplier
- **Item Interactions**: Compatible with Punching Glove effects

### Competitive Viability
High-tier ability that transforms Dragon-type attackers into formidable threats. The accuracy guarantee eliminates risk from powerful but inaccurate moves, while the Dragon-punch conversion provides consistent damage boost. Excellent for mixed attackers utilizing both physical and special Dragon moves.