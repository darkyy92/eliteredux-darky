#!/usr/bin/env python3
"""
Script to fix and verify corrected character counts - version 2
"""

# Final corrected descriptions
corrected = {
    33: "Swift Swim boosts the Pokémon's Speed by 50% during rain weather. Works with all forms of rain including regular rain, heavy rain, and Primordial Sea. The speed boost applies immediately when rain is active and disappears when rain ends. Stacks with other speed modifiers for sweeping potential.",
    
    36: "Trace copies the ability of an opposing Pokémon when entering battle, replacing itself in the current ability slot. Cannot copy Trace, Wonder Guard, Receiver, or persistent abilities. In doubles, targets the first valid opponent. Does not copy innate abilities. Shows ability popup.",
    
    39: "Inner Focus provides immunity to flinching, Intimidate-like effects (Intimidate, Scare, Fearmonger, etc.), and status conditions from Taunt. Additionally, when this Pokémon uses Focus Blast, it bypasses accuracy checks and always hits the target, improving its battle reliability.",
    
    42: "Magnet Pull prevents Steel-type Pokémon from switching out. Ghost-types are immune to this effect. Pokémon holding Shed Shell can escape. Does not block Teleport, U-turn, Volt Switch, or Baton Pass. Creates magnetic field that traps Steel Pokemon until the user switches out or faints."
}

ability_names = {
    33: "Swift Swim",
    36: "Trace", 
    39: "Inner Focus",
    42: "Magnet Pull"
}

print("Final Character Count Verification")
print("=" * 50)
print(f"{'ID':<3} {'Ability':<15} {'Count':<6} {'Status'}")
print("-" * 50)

all_good = True

for id_num in sorted(corrected.keys()):
    name = ability_names[id_num]
    count = len(corrected[id_num])
    
    if 280 <= count <= 300:
        status = "✅ GOOD"
    else:
        status = f"❌ BAD ({count})"
        all_good = False
    
    print(f"{id_num:<3} {name:<15} {count:<6} {status}")

print("\n" + "=" * 50)

if all_good:
    print("✅ ALL DESCRIPTIONS NOW PERFECT!")
    print("\nFinal corrected descriptions for updating:")
    print("-" * 50)
    for id_num in sorted(corrected.keys()):
        print(f"\nID {id_num}: {ability_names[id_num]} ({len(corrected[id_num])} chars)")
        print(f'"{corrected[id_num]}"')
else:
    print("❌ NEED MORE WORK!")