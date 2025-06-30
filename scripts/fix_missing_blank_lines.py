#!/usr/bin/env python3
"""
Script to fix missing blank lines between meta-comment and extended description in ability files.
Also identifies files that might have other formatting issues.
"""

import os
import re
from pathlib import Path

def check_and_fix_file(filepath):
    """Check a file for missing blank line and fix if needed."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to find the Extended In-Game Description section
    # This captures everything from the header to the next section or end of file
    pattern = r'(## Extended In-Game Description\s*\n)(\*[^\n]*\*\s*\n)([^\n#]+)'
    
    match = re.search(pattern, content)
    if not match:
        return 'no_extended_section', None
    
    header = match.group(1)
    meta_comment = match.group(2)
    after_meta = match.group(3)
    
    # Check if there's already a blank line (starts with newline)
    if after_meta.startswith('\n'):
        # Already has blank line
        return 'ok', None
    
    # Check if there's actual content (not just whitespace)
    if after_meta.strip() == '':
        return 'empty_description', None
    
    # Fix: add blank line
    original_section = match.group(0)
    fixed_section = header + meta_comment + '\n' + after_meta
    
    new_content = content.replace(original_section, fixed_section)
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return 'fixed', after_meta.strip()[:50] + '...'

def main():
    """Main function to process all ability files."""
    abilities_dir = Path("/Users/joel/Github/eliteredux/eliteredux-source/eliteredux-darky/knowledge/abilities")
    
    if not abilities_dir.exists():
        print(f"❌ Directory not found: {abilities_dir}")
        return
    
    # Get all .md files that match the pattern (number_name.md)
    ability_files = [f for f in abilities_dir.glob("*.md") 
                     if re.match(r'^\d+_.*\.md$', f.name)]
    
    if not ability_files:
        print("❌ No ability files found")
        return
    
    print(f"🔍 Checking {len(ability_files)} ability files for formatting issues...")
    print()
    
    fixed_count = 0
    ok_count = 0
    no_section_count = 0
    empty_desc_count = 0
    
    fixed_files = []
    no_section_files = []
    empty_desc_files = []
    
    for filepath in sorted(ability_files):
        try:
            status, info = check_and_fix_file(filepath)
            
            if status == 'fixed':
                fixed_count += 1
                fixed_files.append((filepath.name, info))
            elif status == 'ok':
                ok_count += 1
            elif status == 'no_extended_section':
                no_section_count += 1
                no_section_files.append(filepath.name)
            elif status == 'empty_description':
                empty_desc_count += 1
                empty_desc_files.append(filepath.name)
                
        except Exception as e:
            print(f"❌ Error processing {filepath.name}: {e}")
    
    # Report results
    print("📊 Summary:")
    print(f"✅ {ok_count} files already had correct formatting")
    print(f"🔧 {fixed_count} files were fixed (added blank line)")
    print(f"⚠️  {no_section_count} files have no Extended In-Game Description section")
    print(f"❓ {empty_desc_count} files have empty extended descriptions")
    print()
    
    if fixed_files:
        print("🔧 Fixed files (added blank line):")
        for filename, preview in fixed_files[:10]:  # Show first 10
            print(f"  - {filename}: {preview}")
        if len(fixed_files) > 10:
            print(f"  ... and {len(fixed_files) - 10} more")
        print()
    
    if no_section_files:
        print("⚠️  Files with no Extended In-Game Description section:")
        for filename in no_section_files:
            print(f"  - {filename}")
        print()
    
    if empty_desc_files:
        print("❓ Files with empty extended descriptions:")
        for filename in empty_desc_files:
            print(f"  - {filename}")

if __name__ == "__main__":
    main()