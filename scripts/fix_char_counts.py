#!/usr/bin/env python3
"""
Script to fix and verify corrected character counts for extended ability descriptions
"""

# Original descriptions that need fixing
originals = {
    33: "Swift Swim boosts the Pokémon's Speed by 50% during rain weather. Works with all forms of rain including regular rain, heavy rain, and Primordial Sea. The speed boost applies immediately when rain is active and disappears when rain ends. Stacks with other speed modifiers for powerful sweeping potential.",
    36: "Trace copies the ability of an opposing Pokémon when entering battle, replacing itself in the current ability slot. Cannot copy Trace, Wonder Guard, Receiver, or any persistent/unsuppressable abilities. In doubles, targets the first valid opponent. Does not copy innate abilities. Shows ability popup for copied ability.",
    39: "Inner Focus provides immunity to flinching, Intimidate-like effects (Intimidate, Scare, Fearmonger, etc.), and status conditions from Taunt. Additionally, when this Pokémon uses Focus Blast, it bypasses accuracy checks and always hits the target, improving its reliability.",
    42: "Magnet Pull prevents Steel-type Pokémon from switching out or fleeing from battle. Ghost-type Pokémon are immune to this trapping effect. Pokémon holding Shed Shell can still escape. Does not affect Teleport, U-turn, Volt Switch, or Baton Pass moves."
}

# Corrected descriptions
corrected = {
    33: "Swift Swim boosts the Pokémon's Speed by 50% during rain weather. Works with all forms of rain including regular rain, heavy rain, and Primordial Sea. The speed boost applies immediately when rain is active and disappears when rain ends. Stacks with other speed modifiers for sweeping potential.",
    
    36: "Trace copies the ability of an opposing Pokémon when entering battle, replacing itself in the current ability slot. Cannot copy Trace, Wonder Guard, Receiver, or persistent abilities. In doubles, targets the first valid opponent. Does not copy innate abilities. Shows ability popup.",
    
    39: "Inner Focus provides immunity to flinching, Intimidate-like effects (Intimidate, Scare, Fearmonger, etc.), and status conditions from Taunt. Additionally, when this Pokémon uses Focus Blast, it bypasses accuracy checks and always hits the target, improving its battle reliability.",
    
    42: "Magnet Pull creates a magnetic field that prevents Steel-type Pokémon from switching out or fleeing from battle. Ghost-type Pokémon are immune to this trapping effect due to their incorporeal nature. Pokémon holding Shed Shell can still escape the magnetic trap. Does not affect special switching moves like Teleport, U-turn, Volt Switch, or Baton Pass."
}

ability_names = {
    33: "Swift Swim",
    36: "Trace", 
    39: "Inner Focus",
    42: "Magnet Pull"
}

print("Fixed Character Count Verification")
print("=" * 60)
print(f"{'ID':<3} {'Ability':<15} {'Original':<9} {'Fixed':<6} {'Status'}")
print("-" * 60)

all_good = True

for id_num in sorted(corrected.keys()):
    name = ability_names[id_num]
    orig_count = len(originals[id_num])
    fixed_count = len(corrected[id_num])
    
    if 280 <= fixed_count <= 300:
        status = "✅ FIXED"
    else:
        status = "❌ STILL BAD"
        all_good = False
    
    print(f"{id_num:<3} {name:<15} {orig_count:<9} {fixed_count:<6} {status}")

print("\n" + "=" * 60)

if all_good:
    print("✅ ALL DESCRIPTIONS NOW FIXED AND WITHIN 280-300 RANGE!")
    print("\nCorrected descriptions:")
    print("-" * 60)
    for id_num in sorted(corrected.keys()):
        print(f"\nID {id_num}: {ability_names[id_num]} ({len(corrected[id_num])} chars)")
        print(f'"{corrected[id_num]}"')
else:
    print("❌ SOME DESCRIPTIONS STILL NEED WORK!")
