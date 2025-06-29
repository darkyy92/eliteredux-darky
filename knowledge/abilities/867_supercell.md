---
id: 867
name: Supercell
status: ai-generated
character_count: 294
---

# Supercell - Ability ID 867

## In-Game Description
Drizzle + Electro Surge.

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*
Combines Drizzle and Electric Surge. Summons rain (boosts Water moves 20%, weakens Fire 50%) and Electric Terrain (boosts Electric moves 30%, prevents sleep) simultaneously on entry. Provides dual field control for weather and terrain strategies.

## Detailed Mechanical Explanation

### Code Implementation
Located in `src/abilities.cc`:
```cpp
constexpr Ability Supercell = {
    .onEntry = +[](ON_ENTRY) -> int { 
        return ElectricSurge.onEntry(DELEGATE_ENTRY) | Drizzle.onEntry(DELEGATE_ENTRY); 
    },
    .allowTerrainIfAirborne = TERRAIN_ELECTRIC,
};
```

### Mechanical Effects

#### Rain (Drizzle Component)
- **Water Move Boost**: +20% damage to Water-type moves in rain
- **Fire Move Reduction**: -50% damage to Fire-type moves in rain  
- **Duration**: 5 turns (8 turns with Damp Rock)
- **Weather Message**: "It started to rain!" / "Rain continues to fall."

#### Electric Terrain (Electric Surge Component)  
- **Electric Move Boost**: +30% damage to Electric-type moves on terrain
- **Sleep Prevention**: Grounded Pokemon cannot be put to sleep
- **Duration**: 5 turns (8 turns with Terrain Extender)
- **Terrain Message**: "An electric current ran across the battlefield!"

### Unique Properties
- **Simultaneous Activation**: Both weather and terrain activate at the same time on switch-in
- **Airborne Terrain Access**: Pokemon with Supercell can benefit from Electric Terrain even when airborne (Flying-type, Levitate, Air Balloon, etc.)
- **Ability Disruption**: Electric Surge component disables Generator and Energized abilities on switch-in

### Interactions
- **Weather Priority**: Rain can be overridden by other weather conditions
- **Terrain Priority**: Electric Terrain can be overridden by other terrain effects  
- **Primal Weather**: Cannot override Primal weather conditions
- **Utility Umbrella**: Blocks rain effects but not Electric Terrain effects

### Strategic Applications
- **Dual Type Coverage**: Supports both Water and Electric attackers simultaneously
- **Weather/Terrain Control**: Establishes field conditions for team support
- **Sleep Immunity**: Provides sleep protection for grounded allies
- **Fire Counter**: Significantly weakens opposing Fire-type attacks

This ability combines two of the most powerful field-setting abilities in the game, making it exceptionally valuable for teams built around weather and terrain synergy.