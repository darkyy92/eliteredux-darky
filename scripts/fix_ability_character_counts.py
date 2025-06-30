#!/usr/bin/env python3
"""
Script to fix character counts in ability documentation frontmatter.
Counts the actual characters in the extended description and updates the frontmatter.
"""

import os
import re
from pathlib import Path

def parse_markdown_file(filepath):
    """Parse a markdown file and extract frontmatter and content."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract frontmatter
    frontmatter_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not frontmatter_match:
        return None, None, None
    
    frontmatter = frontmatter_match.group(1)
    rest_of_content = content[frontmatter_match.end():]
    
    return frontmatter, rest_of_content, content

def extract_extended_description(content):
    """Extract the extended description from the markdown content."""
    # Look for the Extended In-Game Description section
    pattern = r'## Extended In-Game Description\s*\n\*[^\n]*\*\s*\n\n([^\n]+)'
    match = re.search(pattern, content)
    
    if match:
        return match.group(1).strip()
    return None

def update_character_count(frontmatter, actual_count):
    """Update the character_count in the frontmatter."""
    # Replace the character_count line
    updated = re.sub(
        r'character_count:\s*\d+',
        f'character_count: {actual_count}',
        frontmatter
    )
    return updated

def process_file(filepath):
    """Process a single ability file and fix its character count."""
    frontmatter, rest_of_content, full_content = parse_markdown_file(filepath)
    
    if not frontmatter:
        print(f"⚠️  No frontmatter found in {filepath.name}")
        return False
    
    # Extract current character count from frontmatter
    current_count_match = re.search(r'character_count:\s*(\d+)', frontmatter)
    if not current_count_match:
        print(f"⚠️  No character_count in frontmatter for {filepath.name}")
        return False
    
    current_count = int(current_count_match.group(1))
    
    # Extract extended description
    extended_desc = extract_extended_description(rest_of_content)
    if not extended_desc:
        print(f"⚠️  No extended description found in {filepath.name}")
        return False
    
    # Count actual characters (including spaces)
    actual_count = len(extended_desc)
    
    # Check if update is needed
    if current_count != actual_count:
        print(f"📝 {filepath.name}: {current_count} → {actual_count} chars")
        
        # Update frontmatter
        updated_frontmatter = update_character_count(frontmatter, actual_count)
        
        # Reconstruct file content
        new_content = f"---\n{updated_frontmatter}\n---\n{rest_of_content}"
        
        # Write back to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True
    else:
        return False

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
    
    print(f"🔍 Checking {len(ability_files)} ability files...")
    print()
    
    updated_count = 0
    error_count = 0
    
    for filepath in sorted(ability_files):
        try:
            if process_file(filepath):
                updated_count += 1
        except Exception as e:
            print(f"❌ Error processing {filepath.name}: {e}")
            error_count += 1
    
    print()
    print(f"✅ Complete! Updated {updated_count} files")
    if error_count > 0:
        print(f"⚠️  {error_count} files had errors")
    
    # Show some stats
    total_correct = len(ability_files) - updated_count - error_count
    print(f"📊 {total_correct} files already had correct counts")

if __name__ == "__main__":
    main()