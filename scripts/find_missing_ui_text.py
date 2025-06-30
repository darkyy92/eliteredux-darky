#!/usr/bin/env python3
"""
Find ability files missing the UI description text.
This script safely scans ability files and reports which ones are missing
the specific text about Elite Redux extended ability UI character count.
"""

import os
import re

def check_file_for_missing_text(filepath):
    """
    Check if a file has "Extended In-Game Description" but is missing
    the specific UI text about character count.
    Returns tuple: (has_extended_description, missing_ui_text)
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file has "Extended In-Game Description"
        has_extended_desc = "Extended In-Game Description" in content
        
        # Check if it has the CORRECT UI text format
        correct_ui_text = "For use in Elite Redux extended ability UI (280-300 chars max)"
        has_correct_ui_text = correct_ui_text in content
        
        # Only report as missing if it has Extended desc but lacks the correct text
        return has_extended_desc, has_extended_desc and not has_correct_ui_text
    
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return False, False

def main():
    abilities_dir = "/Users/joel/Github/eliteredux/eliteredux-source/eliteredux-darky/knowledge/abilities"
    
    if not os.path.exists(abilities_dir):
        print(f"Error: Directory {abilities_dir} does not exist!")
        return
    
    files_missing_text = []
    files_with_extended_desc = 0
    total_files = 0
    
    # Scan all .md files in the abilities directory
    for filename in os.listdir(abilities_dir):
        if filename.endswith('.md'):
            filepath = os.path.join(abilities_dir, filename)
            total_files += 1
            
            has_extended, missing_ui = check_file_for_missing_text(filepath)
            
            if has_extended:
                files_with_extended_desc += 1
                if missing_ui:
                    files_missing_text.append(filename)
    
    # Report results
    print(f"Scanned {total_files} ability files")
    print(f"Files with 'Extended In-Game Description': {files_with_extended_desc}")
    print(f"Files missing the UI text: {len(files_missing_text)}")
    
    if files_missing_text:
        print("\nFiles missing the UI description text:")
        for filename in sorted(files_missing_text):
            print(f"  - {filename}")
        
        # Save to output file for reference
        output_file = "/Users/joel/Github/eliteredux/eliteredux-source/eliteredux-darky/scripts/missing_ui_text_files.txt"
        with open(output_file, 'w') as f:
            f.write("Files missing the correct UI description text:\n")
            f.write("Expected text: For use in Elite Redux extended ability UI (280-300 chars max)\n\n")
            for filename in sorted(files_missing_text):
                f.write(f"{filename}\n")
        print(f"\nList saved to: {output_file}")
    else:
        print("\nAll files with 'Extended In-Game Description' have the UI text!")

if __name__ == "__main__":
    main()