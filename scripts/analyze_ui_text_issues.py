#!/usr/bin/env python3
"""
Analyze ability files to categorize UI text issues.
This script identifies which files have wrong format vs missing UI text entirely.
"""

import os
import re

def analyze_file(filepath):
    """
    Analyze a file to determine UI text status.
    Returns: (has_extended_desc, status)
    Where status is one of: 'correct', 'wrong_format', 'missing_line', 'no_extended_section'
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file has "Extended In-Game Description" section
        if "## Extended In-Game Description" not in content:
            return False, 'no_extended_section'
        
        # Correct format
        correct_format = "*For use in Elite Redux extended ability UI (280-300 chars max)*"
        
        # Common wrong formats
        wrong_formats = [
            "*For use in Elite Redux extended ability UI (IMPORTANT: exactly 280-300 chars counted WITH spaces)*",
            "For use in Elite Redux extended ability UI (IMPORTANT: exactly 280-300 chars counted WITH spaces)",
            "*For use in Elite Redux extended ability UI (exactly 280-300 chars)*",
            "*For use in Elite Redux extended ability UI (280-300 chars)*"
        ]
        
        # Check for correct format
        if correct_format in content:
            return True, 'correct'
        
        # Check for wrong formats
        for wrong in wrong_formats:
            if wrong in content:
                return True, 'wrong_format'
        
        # Check if there's any UI text line at all (more flexible pattern)
        ui_pattern = r'\*?For use in Elite Redux extended ability UI.*\*?'
        if re.search(ui_pattern, content):
            return True, 'wrong_format'  # Has some UI text but not correct format
        
        # Has Extended section but no UI text line
        return True, 'missing_line'
    
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return False, 'error'

def main():
    abilities_dir = "/Users/joel/Github/eliteredux/eliteredux-source/eliteredux-darky/knowledge/abilities"
    
    if not os.path.exists(abilities_dir):
        print(f"Error: Directory {abilities_dir} does not exist!")
        return
    
    # Categories
    correct_files = []
    wrong_format_files = []
    missing_line_files = []
    no_extended_section_files = []
    error_files = []
    
    total_files = 0
    
    # Analyze all .md files
    for filename in os.listdir(abilities_dir):
        if filename.endswith('.md') and not filename.startswith('CLAUDE'):
            filepath = os.path.join(abilities_dir, filename)
            total_files += 1
            
            has_extended, status = analyze_file(filepath)
            
            if status == 'correct':
                correct_files.append(filename)
            elif status == 'wrong_format':
                wrong_format_files.append(filename)
            elif status == 'missing_line':
                missing_line_files.append(filename)
            elif status == 'no_extended_section':
                no_extended_section_files.append(filename)
            else:  # error
                error_files.append(filename)
    
    # Report results
    print(f"Total ability files analyzed: {total_files}")
    print(f"\nCorrect format: {len(correct_files)}")
    print(f"Wrong format: {len(wrong_format_files)}")
    print(f"Missing UI text line: {len(missing_line_files)}")
    print(f"No Extended In-Game Description section: {len(no_extended_section_files)}")
    print(f"Errors: {len(error_files)}")
    
    # Save categorized results
    output_dir = os.path.dirname(abilities_dir)
    
    # Save wrong format files
    if wrong_format_files:
        wrong_format_file = os.path.join(output_dir, "scripts", "ui_text_wrong_format.txt")
        with open(wrong_format_file, 'w') as f:
            f.write("Files with wrong UI text format:\n")
            f.write("Need to replace with: *For use in Elite Redux extended ability UI (280-300 chars max)*\n\n")
            for filename in sorted(wrong_format_files):
                f.write(f"{filename}\n")
        print(f"\nWrong format list saved to: {wrong_format_file}")
    
    # Save missing line files
    if missing_line_files:
        missing_line_file = os.path.join(output_dir, "scripts", "ui_text_missing_line.txt")
        with open(missing_line_file, 'w') as f:
            f.write("Files missing UI text line entirely:\n")
            f.write("Need to add: *For use in Elite Redux extended ability UI (280-300 chars max)*\n\n")
            for filename in sorted(missing_line_files):
                f.write(f"{filename}\n")
        print(f"Missing line list saved to: {missing_line_file}")
    
    # Save summary
    summary_file = os.path.join(output_dir, "scripts", "ui_text_analysis_summary.txt")
    with open(summary_file, 'w') as f:
        f.write("UI Text Analysis Summary\n")
        f.write("========================\n\n")
        f.write(f"Total files: {total_files}\n")
        f.write(f"Correct format: {len(correct_files)}\n")
        f.write(f"Wrong format: {len(wrong_format_files)}\n")
        f.write(f"Missing UI text line: {len(missing_line_files)}\n")
        f.write(f"No Extended section: {len(no_extended_section_files)}\n")
        f.write(f"Errors: {len(error_files)}\n\n")
        f.write(f"Files needing fixes: {len(wrong_format_files) + len(missing_line_files)}\n")
    
    print(f"\nSummary saved to: {summary_file}")
    print(f"\nTotal files needing fixes: {len(wrong_format_files) + len(missing_line_files)}")

if __name__ == "__main__":
    main()