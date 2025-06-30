#!/usr/bin/env python3
"""
Fix ability files that have the WRONG UI text format.
This script replaces incorrect formats with the correct one.
"""

import os
import re

def fix_wrong_format(filepath):
    """
    Fix files that have wrong UI text format.
    Returns True if file was fixed, False otherwise.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Correct format
        correct_format = "*For use in Elite Redux extended ability UI (280-300 chars max)*"
        
        # List of wrong formats to replace
        wrong_formats = [
            "*For use in Elite Redux extended ability UI (IMPORTANT: exactly 280-300 chars counted WITH spaces)*",
            "For use in Elite Redux extended ability UI (IMPORTANT: exactly 280-300 chars counted WITH spaces)",
            "*For use in Elite Redux extended ability UI (exactly 280-300 chars)*",
            "*For use in Elite Redux extended ability UI (280-300 chars)*",
            "For use in Elite Redux extended ability UI (280-300 chars max)",  # Missing asterisks
            "*For use in Elite Redux extended ability UI*",
            "For use in Elite Redux extended ability UI"
        ]
        
        # Check if already has correct format
        if correct_format in content:
            return False
        
        # Replace wrong formats
        fixed = False
        for wrong in wrong_formats:
            if wrong in content:
                content = content.replace(wrong, correct_format)
                fixed = True
                break
        
        # If no exact match found, try regex for more flexible matching
        if not fixed:
            # Pattern to match various UI text formats
            pattern = r'\*?For use in Elite Redux extended ability UI[^*\n]*\*?'
            if re.search(pattern, content):
                content = re.sub(pattern, correct_format, content)
                fixed = True
        
        # Write back if changed
        if fixed and content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
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
    error_files = []
    
    # Process all .md files
    for filename in os.listdir(abilities_dir):
        if filename.endswith('.md') and not filename.startswith('CLAUDE'):
            filepath = os.path.join(abilities_dir, filename)
            
            # Only process if file has Extended In-Game Description
            with open(filepath, 'r', encoding='utf-8') as f:
                if "## Extended In-Game Description" not in f.read():
                    continue
            
            if fix_wrong_format(filepath):
                fixed_files.append(filename)
                print(f"Fixed: {filename}")
            else:
                # Check if it needs fixing but wasn't fixed
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    correct = "*For use in Elite Redux extended ability UI (280-300 chars max)*"
                    if correct not in content and "For use in Elite Redux" in content:
                        error_files.append(filename)
                    else:
                        skipped_files.append(filename)
    
    # Report results
    print(f"\n=== Fix Wrong UI Format Results ===")
    print(f"Files fixed: {len(fixed_files)}")
    print(f"Files skipped (already correct or no UI text): {len(skipped_files)}")
    print(f"Files with errors: {len(error_files)}")
    
    # Save results
    output_file = "/Users/joel/Github/eliteredux/eliteredux-source/eliteredux-darky/scripts/fix_wrong_format_results.txt"
    with open(output_file, 'w') as f:
        f.write("Fix Wrong UI Format Results\n")
        f.write("===========================\n\n")
        f.write(f"Total files fixed: {len(fixed_files)}\n\n")
        if fixed_files:
            f.write("Fixed files:\n")
            for filename in sorted(fixed_files):
                f.write(f"  - {filename}\n")
        if error_files:
            f.write("\nFiles that may need manual review:\n")
            for filename in sorted(error_files):
                f.write(f"  - {filename}\n")
    
    print(f"\nResults saved to: {output_file}")

if __name__ == "__main__":
    main()