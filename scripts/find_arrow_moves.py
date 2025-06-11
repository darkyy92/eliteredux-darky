#!/usr/bin/env python3
"""Find all arrow-based moves in MoveList.textproto"""

import re

def find_arrow_moves():
    with open('proto/MoveList.textproto', 'r') as f:
        content = f.read()
    
    # Split by move blocks
    moves = content.split('move {')[1:]  # Skip the first empty split
    
    arrow_moves = []
    
    for move in moves:
        if 'arrow: true' in move:
            # Extract move ID
            id_match = re.search(r'id:\s*(MOVE_\w+)', move)
            # Extract move name
            name_match = re.search(r'name:\s*"([^"]+)"', move)
            # Extract type
            type_match = re.search(r'type:\s*TYPE_(\w+)', move)
            # Extract power
            power_match = re.search(r'power:\s*(\d+)', move)
            # Extract split
            split_match = re.search(r'split:\s*SPLIT_(\w+)', move)
            
            if id_match and name_match:
                arrow_moves.append({
                    'id': id_match.group(1),
                    'name': name_match.group(1),
                    'type': type_match.group(1) if type_match else 'UNKNOWN',
                    'power': power_match.group(1) if power_match else '0',
                    'split': split_match.group(1) if split_match else 'UNKNOWN'
                })
    
    print(f"Found {len(arrow_moves)} arrow-based moves:\n")
    for move in arrow_moves:
        print(f"{move['id']:<30} {move['name']:<25} Type: {move['type']:<10} Power: {move['power']:<5} Split: {move['split']}")

if __name__ == "__main__":
    find_arrow_moves()