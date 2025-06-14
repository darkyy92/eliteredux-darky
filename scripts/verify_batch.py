#!/usr/bin/env python3
"""
Automated Batch Verification Pipeline
Validates that all ability files in a batch are properly created and formatted.
"""

import os
import sys
import glob

def verify_batch(ability_ids, base_path="/Users/joel/Github/eliteredux/eliteredux-source"):
    """
    Verify a batch of abilities for completeness and character count compliance.
    
    Args:
        ability_ids: List of ability IDs to check (e.g. [65, 66, 67, ...])
        base_path: Base path to the project
    
    Returns:
        dict: Verification results with pass/fail status
    """
    results = {
        'passed': True,
        'missing_files': [],
        'char_count_issues': [],
        'structure_issues': [],
        'summary': ''
    }
    
    abilities_dir = os.path.join(base_path, "eliteredux-darky/knowledge/abilities")
    
    print("🔍 **Batch Verification Pipeline**")
    print(f"Checking {len(ability_ids)} abilities: {ability_ids}")
    print("=" * 50)
    
    # Check 1: File Existence
    print("\n📁 **File Existence Check**")
    for ability_id in ability_ids:
        # Find file with this ID (handle different naming patterns)
        pattern = os.path.join(abilities_dir, f"{ability_id}_*.md")
        matches = glob.glob(pattern)
        
        if not matches:
            results['missing_files'].append(ability_id)
            results['passed'] = False
            print(f"❌ ID {ability_id}: File not found")
        elif len(matches) > 1:
            results['structure_issues'].append(f"ID {ability_id}: Multiple files found")
            results['passed'] = False
            print(f"⚠️ ID {ability_id}: Multiple files found: {matches}")
        else:
            print(f"✅ ID {ability_id}: {os.path.basename(matches[0])}")
    
    # Check 2: Character Count Validation (check extended_descriptions.txt)
    print("\n📊 **Character Count Validation**")
    extended_desc_file = os.path.join(base_path, "eliteredux-darky/knowledge/extended_ability_descriptions/extended_descriptions.txt")
    
    try:
        with open(extended_desc_file, 'r', encoding='utf-8') as f:
            ext_desc_content = f.read()
        
        for ability_id in ability_ids:
            # Find this ability's entry in extended_descriptions.txt
            ability_pattern = f"# ID: {ability_id}\nability {{"
            start_idx = ext_desc_content.find(ability_pattern)
            
            if start_idx == -1:
                issue = f"ID {ability_id}: Not found in extended_descriptions.txt"
                results['char_count_issues'].append(issue)
                results['passed'] = False
                print(f"❌ {issue}")
                continue
            
            # Find the extended_description line
            desc_start = ext_desc_content.find('extended_description: "', start_idx)
            if desc_start == -1:
                issue = f"ID {ability_id}: No extended_description found"
                results['char_count_issues'].append(issue)
                results['passed'] = False
                print(f"❌ {issue}")
                continue
            
            # Extract the description content
            desc_start += len('extended_description: "')
            desc_end = ext_desc_content.find('"', desc_start)
            description = ext_desc_content[desc_start:desc_end]
            
            actual_count = len(description)
            
            if 280 <= actual_count <= 300:
                print(f"✅ ID {ability_id}: {actual_count} chars (PASS)")
            else:
                issue = f"ID {ability_id}: {actual_count} chars (FAIL - need 280-300)"
                results['char_count_issues'].append(issue)
                results['passed'] = False
                print(f"❌ {issue}")
    
    except Exception as e:
        issue = f"Error reading extended_descriptions.txt: {e}"
        results['structure_issues'].append(issue)
        results['passed'] = False
        print(f"❌ {issue}")
    
    # Check 3: Required Structure Elements
    print("\n🏗️ **Structure Validation**")
    required_sections = [
        "# ",  # Title
        "## In-Game Description", 
        "## Extended In-Game Description",
        "*Character count:",
        "## Detailed Mechanical Explanation"
    ]
    
    for ability_id in ability_ids:
        pattern = os.path.join(abilities_dir, f"{ability_id}_*.md")
        matches = glob.glob(pattern)
        
        if matches:
            filepath = matches[0]
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                missing_sections = []
                for section in required_sections:
                    if section not in content:
                        missing_sections.append(section)
                
                if missing_sections:
                    issue = f"ID {ability_id}: Missing sections: {missing_sections}"
                    results['structure_issues'].append(issue)
                    results['passed'] = False
                    print(f"❌ {issue}")
                else:
                    print(f"✅ ID {ability_id}: All required sections present")
                    
            except Exception as e:
                issue = f"ID {ability_id}: Error validating structure: {e}"
                results['structure_issues'].append(issue)
                results['passed'] = False
                print(f"❌ {issue}")
    
    # Summary
    print("\n" + "=" * 50)
    if results['passed']:
        results['summary'] = f"🎉 **BATCH VERIFICATION PASSED** ✅\nAll {len(ability_ids)} abilities properly created and validated!"
        print(results['summary'])
    else:
        issues = []
        if results['missing_files']:
            issues.append(f"{len(results['missing_files'])} missing files")
        if results['char_count_issues']:
            issues.append(f"{len(results['char_count_issues'])} character count issues")
        if results['structure_issues']:
            issues.append(f"{len(results['structure_issues'])} structure issues")
        
        results['summary'] = f"❌ **BATCH VERIFICATION FAILED**\nIssues found: {', '.join(issues)}"
        print(results['summary'])
        
        print("\n🔧 **Issues to Fix:**")
        for issue_list, title in [(results['missing_files'], "Missing Files"), 
                                 (results['char_count_issues'], "Character Count Issues"),
                                 (results['structure_issues'], "Structure Issues")]:
            if issue_list:
                print(f"\n**{title}:**")
                for issue in issue_list:
                    print(f"  - {issue}")
    
    return results

if __name__ == "__main__":
    # Example usage
    if len(sys.argv) > 1:
        # Parse ability IDs from command line
        ability_ids = [int(x) for x in sys.argv[1:]]
    else:
        # Default test with last batch
        ability_ids = [65, 66, 67, 68, 69, 71, 72, 73, 74, 75]
        print("🧪 **Testing with last batch (65-69, 71-75)**")
    
    results = verify_batch(ability_ids)
    sys.exit(0 if results['passed'] else 1)