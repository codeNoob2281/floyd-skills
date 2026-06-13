# Codex

## Project Overview

This is a Claude Code Skills library project for managing and organizing reusable Claude Code skills. Compatible with both Claude Code and OpenAI Codex.

## Development

```bash
# List all skills
ls -la .claude/skills/

# List all rules
ls -la .claude/rules/

# View project structure
tree -L 3 -I node_modules
```

## Code Style

- Use kebab-case for skill names
- Use PascalCase for skill titles
- Follow markdown best practices
- Keep SKILL.md files concise and actionable

## File Structure

```
floyd-skills/
├── CLAUDE.md                    # Claude Code config
├── AGENTS.md                    # Codex config (this file)
├── README.md                    # Project documentation
├── .claude/
│   ├── skills/                  # Skill definitions
│   │   ├── claude-md-guide/
│   │   └── harness-rule-reviewer/
│   └── rules/                   # Rule files
│       ├── git-workflow.md
│       ├── code-style.md
│       └── commit-conventions.md
└── .codex/
    └── rules/                   # Codex-specific rules (optional)
```

## Agent Instructions

### General Behavior
- Always read SKILL.md before using a skill
- Follow the subtraction philosophy: only add what's necessary
- Prefer specific, actionable instructions over vague guidance

### Skill Usage
- Use `claude-md-guide` for creating CLAUDE.md files
- Use `harness-rule-reviewer` for auditing configuration files
- Check both CLAUDE.md and AGENTS.md for consistency

### Cross-Platform Compatibility
- Ensure rules work with both Claude Code and Codex
- Use platform-agnostic commands when possible
- Document platform-specific behavior clearly

### Quality Standards
- Every rule must pass the necessity test
- Keep rules concise and focused
- Remove outdated or redundant rules promptly
- Maintain consistency across platforms