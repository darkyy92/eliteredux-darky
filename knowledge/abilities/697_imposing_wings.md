---
id: 697
name: Imposing Wings
status: ai-generated
character_count: 294
---

# Imposing Wings

**ID**: 697  
**Type**: Combination Ability  
**Breakable**: Yes  

## Effect

Imposing Wings combines the effects of Giant Wings and Levitate, providing both offensive enhancement and ground immunity.

## Extended In-Game Description
Majestic wings grant complete immunity to Ground-type moves and boost the power of airborne attacks by 30%. The Pokemon floats gracefully above the battlefield, untouchable by terrestrial assaults while its precise aerial maneuvers become devastatingly effective against earthbound foes below.

## Technical Details

- **Giant Wings Component**: Increases damage of air-based moves by 30% (1.3x multiplier)
- **Levitate Component**: Provides immunity to Ground-type moves and arena trap effects
- **Breakable**: This ability can be disabled by moves like Gastro Acid or Worry Seed
- **Implementation**: Delegates to both GiantWings.onOffensiveMultiplier and Levitate.onOffensiveMultiplier functions

## Affected Moves

Air-based moves that receive the 30% power boost include:
- Fly, Bounce, Sky Attack
- Aeroblast, Air Slash, Hurricane  
- Gust, Twister, Tailwind
- And other moves with the airBased flag

## Strategic Use

This ability excels on Pokemon that rely on Flying-type attacks while providing crucial Ground immunity. Particularly effective in formats with common Ground-type moves like Earthquake. The combination makes the Pokemon a formidable aerial threat while maintaining defensive utility.