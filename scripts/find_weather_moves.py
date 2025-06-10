#!/usr/bin/env python3
"""Find all moves with FLAG_WEATHER_BASED flag"""

import re

def find_weather_moves():
    with open('/Users/joel/Github/eliteredux/eliteredux-source/include/generated/data/battle_moves.h', 'r') as f:
        content = f.read()
    
    # Pattern to match move entries with FLAG_WEATHER_BASED
    pattern = r'\[MOVE_(\w+)\]\s*=\s*\{[^}]*FLAG_WEATHER_BASED[^}]*\}'
    
    matches = re.findall(pattern, content, re.DOTALL)
    
    # Sort and print results
    weather_moves = sorted(set(matches))
    
    print(f"Found {len(weather_moves)} moves with FLAG_WEATHER_BASED:\n")
    
    for move in weather_moves:
        # Convert from MOVE_NAME to proper formatting
        move_name = move.replace('_', ' ').title()
        print(f"- {move_name} (MOVE_{move})")

if __name__ == "__main__":
    find_weather_moves()