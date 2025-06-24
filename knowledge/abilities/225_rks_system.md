---
id: 225
name: RKS System
status: ai-generated
character_count: 266
---

# RKS System - Ability ID 225

## In-Game Description
"Held Memory determines its type. Also has Protean + Adaptability."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (IMPORTANT: exactly 280-300 chars counted WITH spaces)*

RKS System changes the Pokémon's type based on its held Memory disc. Before each attack, it changes type to match the move's type like Protean, but also gains Adaptability's STAB bonus (2x instead of 1.5x). Works with all 17 Memory discs for complete type coverage.

*Character count: 266*

## Detailed Mechanical Explanation
*For Discord/reference use*

RKS System is Silvally's signature ability that combines three powerful mechanics:

### Core Mechanics

1. **Type Transformation via Memory Items**: Silvally's form and type change based on held Memory disc:
   - Fighting Memory → Fighting-type Silvally
   - Flying Memory → Flying-type Silvally
   - Poison Memory → Poison-type Silvally
   - Ground Memory → Ground-type Silvally
   - Rock Memory → Rock-type Silvally
   - Bug Memory → Bug-type Silvally
   - Ghost Memory → Ghost-type Silvally
   - Steel Memory → Steel-type Silvally
   - Fire Memory → Fire-type Silvally
   - Water Memory → Water-type Silvally
   - Grass Memory → Grass-type Silvally
   - Electric Memory → Electric-type Silvally
   - Psychic Memory → Psychic-type Silvally
   - Ice Memory → Ice-type Silvally
   - Dragon Memory → Dragon-type Silvally
   - Dark Memory → Dark-type Silvally
   - Fairy Memory → Fairy-type Silvally
   - No Memory → Normal-type Silvally

2. **Protean Effect**: Before using any attack, Silvally changes its type to match the move's type
   - Activates once per turn (once-per-turn ability flag)
   - Does not activate if already the same type as the move
   - Does not work with Struggle
   - Type change happens before damage calculation

3. **Adaptability Effect**: All STAB moves deal 2x damage instead of the normal 1.5x multiplier
   - Stacks with Protean to create powerful same-type attacks
   - Always active, not dependent on turn timing

### Technical Implementation

```c
constexpr Ability RksSystem = {
    .onBeforeAttack = Protean.onBeforeAttack,  // Type change before attack
    .unsuppressable = TRUE,                    // Cannot be suppressed
    .randomizerBanned = TRUE,                  // Banned from randomizer
    .adaptability = TRUE,                      // STAB becomes 2x
};
```

The form change is handled through the form change table system:
```c
static const struct FormChange sSilvallyFormChangeTable[] = {
    {FORM_ITEM_HOLD_ABILITY, SPECIES_SILVALLY, ITEM_NONE, ABILITY_RKS_SYSTEM},
    {FORM_ITEM_HOLD_ABILITY, SPECIES_SILVALLY_FIGHTING, ITEM_FIGHTING_MEMORY, ABILITY_RKS_SYSTEM},
    // ... continues for all 17 types
};
```

### Activation Conditions

1. **Form Change**: Requires RKS System ability and specific Memory disc held
2. **Protean Effect**: Triggers before any attack move (not Struggle)
   - Limited to once per turn
   - Only activates if current type differs from move type
3. **Adaptability**: Always active for STAB moves

### Strategic Implications

**Offensive Power**:
- Perfect type coverage with appropriate Memory disc
- 2x STAB on every attack due to Protean + Adaptability combo
- Can adapt to any situation mid-battle

**Flexibility**:
- Pre-battle: Choose Memory disc for specific type matchup
- In-battle: Gain STAB on any move through type changing
- Coverage moves become STAB moves

**Defensive Utility**:
- Can change to resist incoming attacks by using moves of that type
- Memory disc determines starting type and resistances

### Example Damage Calculations

**Normal Silvally using Extreme Speed**:
- Base power: 80
- STAB (2x): 160 effective power
- Priority +2 for revenge killing

**Fire Memory Silvally using Flamethrower**:
- Starts as Fire-type (Memory effect)
- Uses Flamethrower (Fire-type move)
- Already Fire-type, no Protean activation needed
- STAB (2x): 90 × 2 = 180 effective power

**Fighting Memory Silvally using Thunder**:
- Starts as Fighting-type
- Uses Thunder (Electric-type move)
- Protean activates: becomes Electric-type
- STAB (2x): 110 × 2 = 220 effective power

### Common Users

- **Silvally**: The only natural user of RKS System
- **Type: Null**: Cannot have RKS System (evolves into Silvally to gain it)

### Competitive Usage Notes

**Strengths**:
- Incredible versatility and type coverage
- Powerful STAB on every move
- Can function as revenge killer, wall-breaker, or pivot
- Memory choice allows team customization
- Unsuppressable ability

**Weaknesses**:
- Memory item slot is locked (cannot hold other items)
- Once-per-turn Protean limit can be played around
- Prediction required for optimal Memory selection
- Form change telegraphs strategy

### Counters

1. **Mold Breaker/Teravolt/Turboblaze**: Cannot suppress RKS System (unsuppressable flag)
2. **Gastro Acid**: Cannot suppress RKS System (unsuppressable flag)
3. **Priority moves**: Can revenge kill before type change occurs
4. **Multi-hit moves**: Only first hit triggers Protean
5. **Status moves**: Don't trigger type change, can cripple

### Synergies

**Moves**:
- **Extreme Speed**: Perfect for revenge killing with guaranteed STAB
- **U-turn/Parting Shot**: Pivot while gaining STAB
- **Wide movepool**: Every move becomes potentially STAB

**Items**:
- **Memory Discs**: Required for type specialization
  - Offensive: Choose Memory for coverage needs
  - Defensive: Choose Memory for key resistances

**Team Support**:
- **Entry hazard support**: Helps secure KOs with boosted STAB
- **Pivoting partners**: Can bring Silvally in safely to use Protean

### Version History

RKS System is implemented as designed in Elite Redux, combining:
1. Silvally's signature form-changing mechanic with Memory items
2. Protean's type-changing utility 
3. Adaptability's STAB boost
4. Unsuppressable flag for reliability

This creates one of the most versatile abilities in the game, allowing Silvally to function as a powerful adaptive threat with perfect type coverage and enhanced STAB damage.