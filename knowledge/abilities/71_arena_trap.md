---
id: 71
name: Arena Trap
status: ai-generated
character_count: 280
---

# Arena Trap - Ability ID 71

## In-Game Description
"Enemies can't flee. Ghosts and ungrounded Pokémon are immune."

## Extended In-Game Description
*For use in Elite Redux extended ability UI (280-300 chars max)*

Arena Trap prevents grounded enemy Pokémon from fleeing or switching out. Flying-type Pokémon, Pokémon with Levitate, Magnet Rise, Air Balloon, or Telekinesis are immune. Ghost-type Pokémon are also immune. Shed Shell bypasses this trap. Does not work on allies in double battles.

*Character count: 285*

## Detailed Mechanical Explanation
*For Discord/reference use*

**ARENA TRAP** is a trapping ability that prevents certain opposing Pokémon from fleeing or switching out voluntarily.

### Activation Mechanics:
- **Trigger**: Passive effect while the Pokémon is on the battlefield
- **Target**: Grounded opposing Pokémon only
- **Function**: onTrap hook that checks if the switching Pokémon is grounded

### Trapping Conditions:
Arena Trap prevents escape if ALL of the following are true:
1. **Target is grounded**: Must pass IsBattlerGrounded() check
2. **Target is opposing**: Does not affect allies in double battles
3. **Target is not Ghost-type**: Ghost-types are immune (Gen 6+ behavior)
4. **Target doesn't have Shed Shell**: Shed Shell bypasses all trapping effects

### Immunity Conditions:
The following Pokémon are **immune** to Arena Trap:
- **Flying-type Pokémon**: Always immune due to not being grounded
- **Pokémon with Levitate**: Ability makes them ungrounded
- **Pokémon affected by Magnet Rise**: Temporary levitation
- **Pokémon holding Air Balloon**: Item-based levitation
- **Pokémon affected by Telekinesis**: Move-based levitation
- **Ghost-type Pokémon**: Type-based immunity (Gen 6+ rule)
- **Pokémon with Shed Shell**: Item bypasses all trapping

### Interaction Rules:
- **vs Double Battles**: Only affects opposing Pokémon, not allies
- **vs Grounding Effects**: Iron Ball, Gravity, Ingrain, etc. can make Flying-types vulnerable
- **vs Run Away**: Shed Shell and Ghost-type immunity override Run Away ability
- **vs Wild Battles**: Prevents fleeing from wild Pokémon battles

### Technical Implementation:
```c
constexpr Ability ArenaTrap = {
    .onTrap = +[](ABILITY_ON_TRAP) -> int { 
        return IsBattlerGrounded(switchingBattler); 
    },
};
```

The ability simply checks if the Pokémon trying to switch is grounded. All other immunity checks (Ghost-type, Shed Shell, etc.) are handled by the battle system's escape logic.

### Competitive Notes:
- Extremely powerful for revenge killing and trapping setup sweepers
- Pairs well with fast attackers that can KO trapped Pokémon
- Countered by switching to Ghost-types or Flying-types
- Air Balloon is a common item specifically to counter trapping abilities
- Shed Shell is the universal counter to all trapping abilities

### Related Abilities:
- **Shadow Tag**: Traps all Pokémon except those with Shadow Tag
- **Magnet Pull**: Traps Steel-type Pokémon specifically
- **Mean Look/Block**: Move-based trapping with different rules

### Version History:
- Gen 3-5: Worked on all non-Flying, non-Levitate Pokémon
- Gen 6+: Ghost-types became immune (Elite Redux follows this rule)
- Elite Redux: Full Gen 6+ implementation with Ghost immunity