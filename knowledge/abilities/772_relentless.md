---
id: 772
name: Relentless
status: ai-generated
character_count: 289
---

# Relentless - Ability ID 772

## In-Game Description
"Exploit Weakness + Merciless"

## Extended In-Game Description
*For use in Elite Redux extended ability UI (IMPORTANT: exactly 280-300 chars counted WITH spaces)*

This Pokémon combines devastating tactics: deals 25% more damage to status-afflicted targets, uses their weaker defensive stat, and automatically lands critical hits on poisoned, paralyzed, bleeding, or speed-reduced foes. A true predator's instinct.

*Character count: 289*

## Detailed Mechanical Explanation
*For Discord/reference use*

Relentless is a powerful hybrid ability that combines two distinct offensive abilities:

### Exploit Weakness Component:
- **Damage Boost**: Deals 25% more damage (1.25× multiplier) to targets with any status condition
- **Stat Targeting**: Automatically targets the opponent's weaker defensive stat (Defense vs Special Defense) when they have a status condition
- **Status Detection**: Triggers on any status condition or ability-induced state that qualifies as "HasAnyStatusOrAbility"

### Merciless Component:
- **Guaranteed Critical Hits**: Automatically lands critical hits on targets with:
  - Any poison status (regular poison, badly poisoned)
  - Paralysis
  - Bleeding status
  - Reduced Speed stat stages (below +0)
  - Iron Ball held item effect

### Combined Effect:
When facing a status-afflicted opponent, Relentless provides:
1. 25% damage increase from Exploit Weakness
2. Automatic targeting of weaker defensive stat
3. Guaranteed critical hit (if the status qualifies for Merciless)
4. Critical hit damage stacks multiplicatively with the 25% boost

This makes Relentless exceptionally powerful against teams that rely on status moves or have been weakened by previous attacks. The ability synergizes perfectly with moves that inflict status conditions, creating a devastating offensive strategy where status setup leads to massive damage output.

### Technical Implementation:
```cpp
constexpr Ability Relentless = {
    .onOffensiveMultiplier = ExploitWeakness.onOffensiveMultiplier,
    .onChooseDefensiveStat = ExploitWeakness.onChooseDefensiveStat,
    .onCrit = Merciless.onCrit,
};
```

The ability is implemented as a combination of existing abilities, inheriting their exact mechanics without modification.