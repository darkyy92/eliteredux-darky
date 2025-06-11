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
    # Matches various formats:
    # "# ALL_CAPS_NAME - Ability ID XXX"
    # "# ALL CAPS NAME (Ability ID: XXX)"
    # "# ALL CAPS NAME (ID: XXX)"
    patterns = [
        re.compile(r'^# ([A-Z][A-Z\s_]+) - (Ability ID \d+)$', re.MULTILINE),
        re.compile(r'^# ([A-Z][A-Z\s_]+) \((Ability ID: \d+)\)$', re.MULTILINE),
        re.compile(r'^# ([A-Z][A-Z\s_]+) \((ID: \d+)\)$', re.MULTILINE)
    ]
    
    # Get all .md files except README.md
    md_files = glob.glob(os.path.join(abilities_folder, "*.md"))
    md_files = [f for f in md_files if not f.endswith("README.md")]
    
    fixed_count = 0
    
    for file_path in md_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Apply the fix for all patterns
            for i, pattern in enumerate(patterns):
                if i == 0:
                    # Format: "# Name - Ability ID XXX"
                    content = pattern.sub(lambda m: f"# {m.group(1).replace('_', ' ').title()} - {m.group(2)}", content)
                elif i == 1:
                    # Format: "# Name (Ability ID: XXX)"
                    content = pattern.sub(lambda m: f"# {m.group(1).replace('_', ' ').title()} ({m.group(2)})", content)
                elif i == 2:
                    # Format: "# Name (ID: XXX)"
                    content = pattern.sub(lambda m: f"# {m.group(1).replace('_', ' ').title()} ({m.group(2)})", content)
            
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