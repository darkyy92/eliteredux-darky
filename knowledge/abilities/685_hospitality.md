---
id: 685
name: Hospitality
status: ai-generated
character_count: 286
---

# Hospitality - Ability ID 685

## In-Game Description
Heals doubles partner for 25% HP on switch-in.  

## Extended In-Game Description
When this Pokemon switches into battle, it immediately heals its doubles partner for 25% of the partner's maximum HP. This welcoming gesture ensures allies stay healthy and battle-ready, embodying true hospitality by prioritizing teammate welfare above all else with consistent healing.

## Detailed Mechanical Explanation

### Technical Details

- **Healing Amount**: 25% (1/4) of partner's max HP
- **Target**: Doubles partner only  
- **Trigger**: Entry into battle
- **Minimum Heal**: 1 HP if calculation results in 0
- **Restrictions**: Partner must be alive and not at full HP
- **Battle Script**: `BattleScript_Hospitality_AfterPopup`

### Competitive Analysis

Hospitality provides consistent team support in doubles formats by offering guaranteed healing upon switch-in. Unlike abilities that require specific conditions, Hospitality activates reliably whenever the Pokemon enters battle with an injured partner present.

**Synergizes with:**
- Pivot moves (U-turn, Volt Switch)
- Entry hazard setters
- Tank Pokemon that frequently switch

**Countered by:**
- Healing-blocking effects
- Single battles (no effect)
- Bleed status condition

### Related Abilities

- **Butter Up** (ID 686): Combines Hospitality with Soothing Aroma effects
- **Healer** (ID 131): Cures partner's status conditions
- **Friend Guard** (ID 132): Reduces damage to partner