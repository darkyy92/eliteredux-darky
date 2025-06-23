# Updated Batch Analyze Prompt with Frontmatter Support

/analyze-ability batch

Think deeply and use todo list to track progress. First check progress.md, then analyze remaining
abilities using parallel subagents (each gets its own context window):

--- ABILITIES BELOW ---



--- END OF LIST ---

Steps:
1. Check eliteredux-darky/knowledge/extended_ability_descriptions/progress.md (first 100 lines)
2. If ability list above is empty:
- Identify all abilities marked as ❌ (not completed) in progress.md
- Select the next 10 uncompleted abilities to work on
- If less than 10 remain, work on all remaining
3. If abilities are provided in the list above:
- Check if a file for each ability exists in:
/Users/joel/Github/eliteredux/eliteredux-source/eliteredux-darky/knowledge/abilities/
- If not, analyze the abilities (treat as new abilities to run the full analysis)
4. Filter out abilities already marked as completed (✅), BUT if the user asks for more details or
clarifying questions to an already completed ability, answer that question and UPDATE the ability markdown
(eg. 2_drizzle.md) file.
5. For each NEW ability (maximum 10 per batch):
- Launch a parallel subagent with: "/project:analyze-ability {ability_name} --create-file"
- Include any specific user questions (if any) in the subagent prompt, but do the normal deep analysis
too, do NOT only answer the user questions.
- Do NOT use zen MCP (chat etc) for these tasks, do it all yourself > better output.
- Add to each subagent prompt: "CRITICAL: You MUST create the markdown file at
eliteredux-darky/knowledge/abilities/{id}_{name_lowercase}.md using the Write tool with YAML frontmatter. This is not optional - the
file MUST be created WITH FRONTMATTER."
6. Skip analysis for completed abilities, just note to the user in chat, they're already done.
7. Gather the correct ability IDs for each with this method:
grep "ABILITY_{ABILITY_NAME}" proto/AbilityEnum.proto

**CRITICAL REQUIREMENTS:**
Each subagent MUST create an individual markdown file at:
`eliteredux-darky/knowledge/abilities/{id}_{name_lowercase}.md`

**FRONTMATTER REQUIREMENTS:**
Every ability file MUST start with this YAML frontmatter block:
```yaml
---
id: {ability_id_number}
name: {Ability Name}
status: ai-generated
character_count: {extended_description_character_count}
---
```

**CHARACTER COUNT REQUIREMENTS FOR EXTENDED DESCRIPTIONS:**
- Extended description MUST be EXACTLY 280-300 characters INCLUDING SPACES
- Count characters before finalizing: use len("your description here")
- If not in range, revise until it fits
- Add *Character count: X* line after the description
- ALSO include character count in the frontmatter

**SUBAGENT INSTRUCTIONS TO INCLUDE:**
When launching subagents, include these verification requirements:
CRITICAL REQUIREMENTS:
1. Extended description must be EXACTLY 280-300 characters INCLUDING SPACES
2. Count characters before finalizing: use len("your description here")
3. MUST include YAML frontmatter at the very top of the file
4. Quality example (exactly 295 chars):
"Swift Swim boosts the Pokémon's Speed by 50% during rain weather. Works with all forms of rain including regular rain, heavy rain, and Primordial Sea. The speed boost applies immediately when rain is active and disappears when rain ends. Stacks with other speed modifiers for sweeping potential."

CHARACTER COUNT VALIDATION CHECKLIST:
- Extended description written
- Character count calculated: len("description")
- Count is between 280-300 (inclusive)
- If not, revise description until it fits
- Add Character count: X line in file
- Include character_count in frontmatter

**MANDATORY FILE STRUCTURE** (follow exactly like 2_drizzle.md):
```markdown
---
id: 2
name: Drizzle
status: ai-generated
character_count: 296
---

# {ABILITY NAME} - Ability ID {ID}

## In-Game Description
"{description from proto file}"

## Extended In-Game Description
*For use in Elite Redux extended ability UI (IMPORTANT: exactly 280-300 chars counted WITH spaces)*

{extended description text}

*Character count: {count}*

## Detailed Mechanical Explanation
*For Discord/reference use*

{comprehensive explanation including:}
- Core mechanics
- Activation conditions
- Numerical values/percentages
- Technical implementation with code blocks
- Complete list of affected moves (if applicable)
- Interactions with other abilities/mechanics
- Strategic implications
- Example damage calculations
- Common users
- Competitive usage notes
- Counters
- Synergies
- Version history
```

When all subagents complete:
1. Verify all individual .md files were created WITH FRONTMATTER
1a. If any files are missing frontmatter, immediately add it yourself
2. Count characters in each extended description to verify 280-300 range
3. Update extended_descriptions.txt with new entries in ID order
4. DO NOT manually update progress.md - instead run:
   ```bash
   python eliteredux-darky/scripts/ability_tools/generate_progress.py
   ```
5. Summarize key findings
6. If more uncompleted abilities remain, note how many are left for next batch

**IMPORTANT CHANGE**: Do NOT manually edit progress.md anymore. The generate_progress.py script will read all frontmatter and regenerate progress.md automatically. This prevents sync issues.