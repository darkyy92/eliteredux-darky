#!/usr/bin/env python3
"""
Script to fix ALL CAPS ability names in markdown files.
Converts titles like "PERFECTIONIST - Ability ID 288" to "Perfectionist - Ability ID 288"
"""

import os
import re
import glob

def fix_ability_name_caps():
    abilities_folder = "/Users/joel/Github/eliteredux/eliteredux-source/eliteredux-darky/knowledge/abilities"
    
    # Pattern to match titles with ALL CAPS ability names
    # Matches: "# ALL_CAPS_NAME - Ability ID XXX" or "# ALL CAPS NAME - Ability ID XXX"
    pattern = re.compile(r'^# ([A-Z][A-Z\s_]+) - (Ability ID \d+)$', re.MULTILINE)
    
    # Get all .md files except README.md
    md_files = glob.glob(os.path.join(abilities_folder, "*.md"))
    md_files = [f for f in md_files if not f.endswith("README.md")]
    
    fixed_count = 0
    
    for file_path in md_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            def fix_match(match):
                ability_name = match.group(1)
                rest = match.group(2)
                
                # Convert to title case (handles both underscores and spaces)
                # Replace underscores with spaces, then convert to title case
                fixed_name = ability_name.replace('_', ' ').title()
                
                return f"# {fixed_name} - {rest}"
            
            # Apply the fix
            content = pattern.sub(fix_match, content)
            
            # Only write if changes were made
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                # Extract filename for reporting
                filename = os.path.basename(file_path)
                print(f"Fixed: {filename}")
                fixed_count += 1
        
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
    
    print(f"\nFixed {fixed_count} files total.")

if __name__ == "__main__":
    fix_ability_name_caps()