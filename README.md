# EliteRedux Darky Tools

This repository contains AI-assisted development tools, scripts, and documentation for the EliteRedux project.

## Contents

- **`knowledge/`** - Project knowledge base and documentation
- **`plans/`** - Development plans and specifications
- **`scripts/`** - Utility scripts for various tasks
  - `ability_tools/` - Scripts for ability management
  - `trainer_tools/` - Scripts for trainer management
  - `wiki_tools/` - Scripts for wiki management

**Note**: The `.claude/` folder must remain in the main repository (not this submodule) for slash commands to work properly.

## Usage

This repository is used as a git submodule in the main EliteRedux project. It keeps AI-related development files separate from the main codebase while still allowing the AI tool to access them.

## Setup

To use this as a submodule in the main repository:

```bash
git submodule add https://github.com/YOUR_USERNAME/eliteredux-darky.git eliteredux-darky
```