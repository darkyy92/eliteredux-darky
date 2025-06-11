#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

// First, fix ability caps in the source files
console.log('Fixing ability title capitalization...');
try {
  const fixCapsScript = path.join(__dirname, '../../scripts/fix_ability_caps.py');
  execSync(`python3 "${fixCapsScript}"`, { stdio: 'inherit' });
  console.log('✓ Ability titles normalized\n');
} catch (error) {
  console.error('Warning: Could not run fix_ability_caps.py:', error.message);
}

// Paths
const sourceDir = path.join(__dirname, '../../knowledge/abilities');
const targetDir = path.join(__dirname, '../docs/abilities');

// Ensure target directory exists
if (!fs.existsSync(targetDir)) {
  fs.mkdirSync(targetDir, { recursive: true });
}

// Get all markdown files from source directory
const files = fs.readdirSync(sourceDir).filter(file => file.endsWith('.md'));

console.log(`Copying ${files.length} ability files...`);

// Copy each file
files.forEach(file => {
  if (file === 'index.md' || file === 'README.md') {
    // Skip index.md and README.md as we have our own
    return;
  }
  
  const sourcePath = path.join(sourceDir, file);
  const targetPath = path.join(targetDir, file);
  
  fs.copyFileSync(sourcePath, targetPath);
  console.log(`  ✓ ${file}`);
});

console.log('Done! All ability files copied successfully.');