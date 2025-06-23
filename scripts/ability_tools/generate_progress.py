#!/usr/bin/env python3
"""
Generate progress.md from frontmatter in individual ability files.
This script reads all ability markdown files and builds the progress tracking table.
"""

import os
import re
from pathlib import Path
import yaml

def extract_frontmatter(content):
    """Extract YAML frontmatter from markdown content."""
    if not content.startswith('---'):
        return None
    
    # Find the closing --- for frontmatter
    match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL | re.MULTILINE)
    if match:
        try:
            return yaml.safe_load(match.group(1))
        except yaml.YAMLError as e:
            print(f"Error parsing YAML: {e}")
            return None
    return None

def main():
    # Paths
    abilities_dir = Path(__file__).parent.parent.parent / "knowledge" / "abilities"
    progress_file = abilities_dir.parent / "extended_ability_descriptions" / "progress.md"
    
    # Ensure abilities directory exists
    if not abilities_dir.exists():
        print(f"Error: Abilities directory not found at {abilities_dir}")
        return
    
    # Collect all ability data
    abilities = []
    
    # Read all markdown files in the abilities directory
    for file_path in sorted(abilities_dir.glob("*.md")):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract frontmatter
            frontmatter = extract_frontmatter(content)
            
            if frontmatter:
                abilities.append(frontmatter)
            else:
                # If no frontmatter, try to extract ID from filename
                match = re.match(r'^(\d+)_(.+)\.md$', file_path.name)
                if match:
                    ability_id = int(match.group(1))
                    ability_name = match.group(2).replace('_', ' ').title()
                    
                    # Try to extract character count from content
                    char_count_match = re.search(r'\*Character count: (\d+)', content)
                    char_count = int(char_count_match.group(1)) if char_count_match else None
                    
                    abilities.append({
                        'id': ability_id,
                        'name': ability_name,
                        'status': 'ai-generated',  # Default for legacy files
                        'character_count': char_count
                    })
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
    
    # Sort by ID
    abilities.sort(key=lambda x: x.get('id', 999999))
    
    # Count statistics
    total_abilities = 869  # Known total
    completed = len(abilities)
    reviewed = sum(1 for a in abilities if a.get('status') == 'reviewed')
    
    # Generate progress.md content
    content = ["# Extended Ability Descriptions Progress\n"]
    content.append(f"Total Abilities: {total_abilities}")
    content.append(f"Completed: {completed}")
    content.append(f"In Progress: 0")
    content.append("\n## Progress Tracking\n")
    content.append("| ID  | Ability Name               | Researched | Written | Reviewed | Character Count |")
    content.append("|-----|----------------------------|------------|---------|----------|-----------------|")
    
    # Track which IDs we've seen
    seen_ids = set()
    
    # Add entries for all 869 abilities
    for i in range(870):  # 0-869
        ability_data = None
        
        # Find matching ability data
        for a in abilities:
            if a.get('id') == i:
                ability_data = a
                seen_ids.add(i)
                break
        
        if ability_data:
            # Ability has been analyzed
            name = ability_data.get('name', 'Unknown')
            status = ability_data.get('status', 'ai-generated')
            char_count = ability_data.get('character_count', '-')
            
            researched = "✅"
            written = "✅"
            reviewed = "✅" if status == 'reviewed' else "❌"
        else:
            # Ability not yet analyzed
            # Try to get name from AbilityEnum or default to placeholder
            name = f"Ability {i}" if i > 0 else "None"
            researched = "❌"
            written = "❌"
            reviewed = "❌"
            char_count = "-"
        
        # Format the row
        row = f"| {i:3d} | {name:26s} | {researched:10s} | {written:7s} | {reviewed:8s} | {str(char_count):15s} |"
        content.append(row)
    
    # Write the file
    with open(progress_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(content) + '\n')
    
    print(f"✅ Generated progress.md")
    print(f"   Total abilities: {total_abilities}")
    print(f"   Completed: {completed}")
    print(f"   Reviewed: {reviewed}")
    print(f"   Remaining: {total_abilities - completed}")

if __name__ == "__main__":
    main()