---
name: skill-writer
description: Creates and updates Claude Code skills. Use when user wants to write, edit, or improve a skill definition.
allowed-tools: Read, Write, Edit, Glob
---

# Skill Writer

## Core Principles

1. **Brevity**: Skills must be short. Remove every unnecessary word.
2. **Clarity**: One skill = one purpose. No ambiguity.
3. **Structure**: Use frontmatter + minimal markdown.

## Skill Format

```markdown
---
name: skill-name
description: One sentence. When to use this skill.
allowed-tools: Tool1, Tool2
---

# Title

## Purpose (optional)
One line if name isn't self-explanatory.

## Workflow
Numbered steps. Keep each step to one line.

## Rules (optional)
Bulleted constraints. Only if critical.
```

## Writing Rules

- **No fluff**: Cut adjectives, adverbs, filler words
- **Active voice**: "Create file" not "A file should be created"
- **Imperative mood**: "Parse input" not "Parsing the input"
- **One idea per line**: Break long sentences
- **Use lists**: Easier to scan than paragraphs

## Workflow

1. Read existing skill (if updating)
2. Identify core purpose
3. Write minimal frontmatter
4. Add only essential sections
5. Review: can anything be cut? Cut it.
