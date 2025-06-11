#!/usr/bin/env python3
"""Find all arrow-based moves in MoveList.textproto"""

import re

def find_arrow_moves():
    with open('proto/MoveList.textproto', 'r') as f:
        lines = f.readlines()
    
    arrow_moves = []
    current_move = {}
    in_move = False
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        if line.startswith('moves {'):
            in_move = True
            current_move = {}
        elif line == '}' and in_move:
            if current_move.get('arrow'):
                arrow_moves.append(current_move)
            in_move = False
            current_move = {}
        elif in_move:
            if line.startswith('id:'):
                current_move['id'] = line.split(':', 1)[1].strip()
            elif line.startswith('name:'):
                current_move['name'] = line.split('"')[1] if '"' in line else line.split(':', 1)[1].strip()
            elif line.startswith('type:'):
                current_move['type'] = line.split(':', 1)[1].strip()
            elif line.startswith('power:'):
                current_move['power'] = line.split(':', 1)[1].strip()
            elif line.startswith('split:'):
                current_move['split'] = line.split(':', 1)[1].strip()
            elif line.startswith('arrow:'):
                current_move['arrow'] = 'true' in line
    
    print(f"Found {len(arrow_moves)} arrow-based moves:\n")
    for move in arrow_moves:
        name = move.get('name', 'UNKNOWN')
        id_str = move.get('id', 'UNKNOWN')
        type_str = move.get('type', 'UNKNOWN')
        power = move.get('power', '0')
        split = move.get('split', 'UNKNOWN')
        print(f"{id_str:<30} {name:<25} Type: {type_str:<15} Power: {power:<5} Split: {split}")

if __name__ == "__main__":
    find_arrow_moves()