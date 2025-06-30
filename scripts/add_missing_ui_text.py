#!/usr/bin/env python3
"""
Add UI text line to ability files that are missing it entirely.
This script adds the UI text line after "## Extended In-Game Description" header.
"""

import os
import re

def add_missing_ui_text(filepath):
    """
    Add UI text line to files missing it entirely.
    Returns True if file was fixed, False otherwise.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file has Extended In-Game Description section
        if "## Extended In-Game Description" not in content:
            return False
        
        # Correct format
        correct_format = "*For use in Elite Redux extended ability UI (280-300 chars max)*"
        
        # Check if already has some form of UI text
        if "For use in Elite Redux extended ability UI" in content:
            return False  # This should be handled by the other script
        
        # Find the Extended In-Game Description section and add the UI text line
        lines = content.split('\n')
        new_lines = []
        added = False
        
        for i, line in enumerate(lines):
            new_lines.append(line)
            
            # Add UI text line after the Extended In-Game Description header
            if line == "## Extended In-Game Description" and not added:
                # Check if next line is empty or has content
                if i + 1 < len(lines):
                    if lines[i + 1].strip() == "":
                        # Next line is empty, perfect place to add
                        new_lines.append(correct_format)
                        added = True
                    else:
                        # Next line has content, add UI text and then empty line
                        new_lines.append(correct_format)
                        new_lines.append("")
                        added = True
                else:
                    # At end of file, just add it
                    new_lines.append(correct_format)
                    added = True
        
        if added:
            # Write back the modified content
            new_content = '\n'.join(new_lines)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        
        return False
    
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    abilities_dir = "/Users/joel/Github/eliteredux/eliteredux-source/eliteredux-darky/knowledge/abilities"
    
    if not os.path.exists(abilities_dir):
        print(f"Error: Directory {abilities_dir} does not exist!")
        return
    
    fixed_files = []
    skipped_files = []
    
    # Process all .md files
    for filename in os.listdir(abilities_dir):
        if filename.endswith('.md') and not filename.startswith('CLAUDE'):
            filepath = os.path.join(abilities_dir, filename)
            
            if add_missing_ui_text(filepath):
                fixed_files.append(filename)
                print(f"Added UI text to: {filename}")
            else:
                skipped_files.append(filename)
    
    # Report results
    print(f"\n=== Add Missing UI Text Results ===")
    print(f"Files fixed: {len(fixed_files)}")
    print(f"Files skipped: {len(skipped_files)}")
    
    # Save results
    output_file = "/Users/joel/Github/eliteredux/eliteredux-source/eliteredux-darky/scripts/add_missing_ui_text_results.txt"
    with open(output_file, 'w') as f:
        f.write("Add Missing UI Text Results\n")
        f.write("==========================\n\n")
        f.write(f"Total files fixed: {len(fixed_files)}\n\n")
        if fixed_files:
            f.write("Fixed files:\n")
            for filename in sorted(fixed_files):
                f.write(f"  - {filename}\n")
    
    print(f"\nResults saved to: {output_file}")

if __name__ == "__main__":
    main()