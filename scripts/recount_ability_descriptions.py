#!/usr/bin/env python3
"""
Recount extended ability descriptions WITH spaces (GBA hardware requirement)

The GBA renders spaces as tiles, so character limits must include spaces.
Previous counts were wrong - they excluded spaces.
"""

import os
import re
import glob

def extract_extended_description(content):
    """Extract the extended description from markdown content."""
    # Pattern: ## Extended In-Game Description\n*instruction*\n\n(description)\n\n*Character count:*
    pattern = r'## Extended In-Game Description\s*\n\*.*?\*\s*\n\n(.*?)(?=\n\n\*Character count:|\n\n## |\Z)'
    match = re.search(pattern, content, re.DOTALL)
    
    if match:
        description = match.group(1).strip()
        return description
    return None

def update_character_count(content, new_count):
    """Update the character count line in the markdown."""
    # Replace *Character count: X* with the new count
    pattern = r'\*Character count: \d+\*'
    replacement = f'*Character count: {new_count}*'
    return re.sub(pattern, replacement, content)

def main():
    # Path to ability files
    abilities_dir = 'knowledge/abilities'
    
    if not os.path.exists(abilities_dir):
        print(f"❌ Directory {abilities_dir} not found!")
        print("Run this script from the eliteredux-darky root directory")
        return
    
    # Find all ability markdown files
    pattern = os.path.join(abilities_dir, '*_*.md')
    files = glob.glob(pattern)
    
    print(f"📊 Found {len(files)} ability files")
    print("🔍 Recounting extended descriptions WITH spaces...\n")
    
    updated_count = 0
    over_limit_count = 0
    
    for file_path in sorted(files):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract extended description
        description = extract_extended_description(content)
        
        if not description:
            print(f"⚠️  {os.path.basename(file_path)}: No extended description found")
            continue
        
        # Count characters WITH spaces (as GBA hardware requires)
        char_count = len(description)
        
        # Extract old count for comparison
        old_count_match = re.search(r'\*Character count: (\d+)\*', content)
        old_count = int(old_count_match.group(1)) if old_count_match else 0
        
        # Update the file if count changed
        if char_count != old_count:
            updated_content = update_character_count(content, char_count)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            updated_count += 1
        
        # Report results
        filename = os.path.basename(file_path)
        status = "📝" if char_count != old_count else "✅"
        
        if char_count > 300:
            print(f"🚨 {filename}: {char_count} chars (OVER LIMIT by {char_count - 300})")
            over_limit_count += 1
        elif char_count < 280:
            print(f"🟡 {filename}: {char_count} chars (under 280, could be longer)")
        else:
            print(f"✅ {filename}: {char_count} chars (perfect range)")
        
        if char_count != old_count:
            print(f"   └─ Updated: {old_count} → {char_count} (+{char_count - old_count})")
    
    print(f"\n📊 Summary:")
    print(f"   • {updated_count} files updated with new counts")
    print(f"   • {over_limit_count} files exceed 300 character limit")
    
    if over_limit_count > 0:
        print(f"\n🚨 {over_limit_count} files need shortening to fit GBA hardware!")
        print("   These will overflow the display and need editing.")

if __name__ == "__main__":
    main()