#!/usr/bin/env python3
"""
Script to verify character counts for extended ability descriptions
"""

# Extended descriptions from the 10 new abilities
descriptions = {
    33: "Swift Swim boosts the Pokémon's Speed by 50% during rain weather. Works with all forms of rain including regular rain, heavy rain, and Primordial Sea. The speed boost applies immediately when rain is active and disappears when rain ends. Stacks with other speed modifiers for powerful sweeping potential.",
    
    34: "Chlorophyll harnesses solar energy to boost Speed by 50% in harsh sunlight. Works with all sun forms: regular (8 turns), permanent (Drought), and primal (Desolate Land). This ability excels in sun teams, enabling fast Solar Beam sweeps and outpacing threats. Pairs perfectly with Drought setters.",
    
    35: "Illuminate increases the accuracy of all moves used by the Pokémon by 20% (1.2x multiplier). Additionally, when this Pokémon is in the lead position of your party while exploring, it doubles the wild encounter rate, making it easier to find wild Pokémon in tall grass, caves, and water.",
    
    36: "Trace copies the ability of an opposing Pokémon when entering battle, replacing itself in the current ability slot. Cannot copy Trace, Wonder Guard, Receiver, or any persistent/unsuppressable abilities. In doubles, targets the first valid opponent. Does not copy innate abilities. Shows ability popup for copied ability.",
    
    37: "Huge Power doubles the Pokémon's Attack stat before stat stage modifiers are applied. This multiplies the effective Attack by 2.0x, making physical moves significantly more powerful. Works with stat stages, items, and other modifiers that are applied after. Identical effect to Pure Power.",
    
    38: "Poison Point has a 30% chance to poison opponents when making or receiving contact moves. Works both defensively when attacked with contact moves and offensively when using contact moves. The poison inflicts 1/8 max HP damage each turn. Bypasses Safeguard protection when triggered by ability.",
    
    39: "Inner Focus provides immunity to flinching, Intimidate-like effects (Intimidate, Scare, Fearmonger, etc.), and status conditions from Taunt. Additionally, when this Pokémon uses Focus Blast, it bypasses accuracy checks and always hits the target, improving its reliability.",
    
    40: "Magma Armor grants complete immunity to the frostbite status condition and reduces damage from Water and Ice-type moves by 30%. This defensive ability is particularly effective against Ice-type Pokemon and moves that inflict frostbite. The resistance helps mitigate common weaknesses.",
    
    41: "Water Veil prevents burn status completely and automatically casts Aqua Ring upon entering battle. The Aqua Ring effect heals 1/16 max HP each turn. Big Root boosts healing by 50%. The healing stacks with other recovery effects and continues until the Pokémon switches out or faints.",
    
    42: "Magnet Pull prevents Steel-type Pokémon from switching out or fleeing from battle. Ghost-type Pokémon are immune to this trapping effect. Pokémon holding Shed Shell can still escape. Does not affect Teleport, U-turn, Volt Switch, or Baton Pass moves."
}

ability_names = {
    33: "Swift Swim",
    34: "Chlorophyll", 
    35: "Illuminate",
    36: "Trace",
    37: "Huge Power",
    38: "Poison Point",
    39: "Inner Focus",
    40: "Magma Armor",
    41: "Water Veil",
    42: "Magnet Pull"
}

print("Character Count Verification for Extended Ability Descriptions")
print("=" * 70)
print(f"{'ID':<3} {'Ability':<15} {'Count':<6} {'Status':<10} {'Range Check'}")
print("-" * 70)

needs_update = []

for id_num in sorted(descriptions.keys()):
    desc = descriptions[id_num]
    name = ability_names[id_num]
    count = len(desc)
    
    if 280 <= count <= 300:
        status = "✅ OK"
        range_check = "PASS"
    else:
        status = "❌ BAD"
        range_check = "FAIL"
        needs_update.append((id_num, name, count, desc))
    
    print(f"{id_num:<3} {name:<15} {count:<6} {status:<10} {range_check}")

print("\n" + "=" * 70)

if needs_update:
    print(f"\n🚨 FOUND {len(needs_update)} DESCRIPTIONS OUTSIDE 280-300 RANGE:")
    for id_num, name, count, desc in needs_update:
        print(f"\nID {id_num}: {name} ({count} chars)")
        print(f"Description: {desc}")
        if count < 280:
            print(f"❌ TOO SHORT: Need {280 - count} more characters")
        else:
            print(f"❌ TOO LONG: Need to remove {count - 300} characters")
else:
    print("\n✅ ALL DESCRIPTIONS ARE WITHIN 280-300 CHARACTER RANGE!")

print(f"\nTotal abilities checked: {len(descriptions)}")