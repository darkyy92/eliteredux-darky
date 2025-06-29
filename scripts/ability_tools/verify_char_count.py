#!/usr/bin/env python3
"""
Verify character counts with 100% accuracy
Tests multiple counting methods to ensure consistency
"""

import subprocess
import unicodedata

def count_methods(text):
    """Count characters using multiple methods"""
    results = {}
    
    # Method 1: Python len()
    results['python_len'] = len(text)
    
    # Method 2: Byte count (ASCII only)
    results['byte_count'] = len(text.encode('ascii', 'replace'))
    
    # Method 3: Shell printf + wc -c
    try:
        proc = subprocess.run(['sh', '-c', f'printf "%s" "{text}" | wc -c'], 
                            capture_output=True, text=True)
        results['shell_wc'] = int(proc.stdout.strip())
    except:
        results['shell_wc'] = -1
    
    # Method 4: Check for non-ASCII
    non_ascii = []
    for i, char in enumerate(text):
        if ord(char) > 127:
            non_ascii.append(f"Position {i}: '{char}' (U+{ord(char):04X})")
    results['non_ascii_chars'] = non_ascii
    
    # Method 5: Unicode normalization check
    results['has_combining'] = len(text) != len(unicodedata.normalize('NFC', text))
    
    return results

def analyze_file(filepath):
    """Analyze a specific ability file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find extended description
        lines = content.split('\n')
        desc_line = -1
        for i, line in enumerate(lines):
            if line.strip() == "## Extended In-Game Description":
                # Look for the description in next few lines
                for j in range(i+1, min(i+10, len(lines))):
                    line_content = lines[j].strip()
                    if (line_content and 
                        not line_content.startswith('*') and 
                        not line_content.startswith('#') and
                        not line_content.startswith('**Character count') and
                        len(line_content) > 50):
                        desc_line = j
                        break
                break
        
        if desc_line == -1:
            return None
        
        description = lines[desc_line]
        return description, count_methods(description)
        
    except Exception as e:
        return f"Error: {e}"

# Test the current Technician description
if __name__ == "__main__":
    print("🔍 CHARACTER COUNT VERIFICATION TOOL")
    print("=" * 60)
    
    # Test Technician
    tech_path = "knowledge/abilities/101_technician.md"
    result = analyze_file(tech_path)
    
    if result and isinstance(result, tuple):
        desc, counts = result
        print(f"\n📄 File: {tech_path}")
        print(f"Description: {desc[:60]}...")
        print(f"\n📊 Character Counts:")
        print(f"  Python len():     {counts['python_len']}")
        print(f"  Byte count:       {counts['byte_count']}")
        print(f"  Shell wc -c:      {counts['shell_wc']}")
        
        if counts['non_ascii_chars']:
            print(f"\n⚠️  NON-ASCII CHARACTERS FOUND:")
            for char_info in counts['non_ascii_chars']:
                print(f"  {char_info}")
        else:
            print(f"\n✅ All characters are ASCII")
        
        # Test with the arrow version the user showed
        arrow_version = desc.replace("40 to 60 BP", "40→60 BP")
        print(f"\n🔄 Testing version with arrow (→):")
        arrow_counts = count_methods(arrow_version)
        print(f"  Character count: {arrow_counts['python_len']}")
        if arrow_counts['non_ascii_chars']:
            print(f"  ⚠️  Contains non-ASCII: {arrow_counts['non_ascii_chars'][0]}")
    
    print("\n" + "=" * 60)
    print("📝 GUIDELINES FOR CORRECT COUNTING:")
    print("1. Use printf + wc -c for accurate counts")
    print("2. NEVER use non-ASCII characters (arrows, quotes, etc.)")
    print("3. Target 290-295 chars for safety margin")
    print("4. Always verify no hidden characters")