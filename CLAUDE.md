# CLAUDE.md

## 项目概述

这是一个 Claude Code Skills 技能库项目，用于管理和组织可复用的 Claude Code 技能（Skills）。同时兼容 OpenAI Codex，支持跨平台配置审查。

## 技能列表

当前项目包含以下技能：

| 技能名称 | 描述 | 位置 |
|----------|------|------|
| claude-md-guide | CLAUDE.md 编写指南 | skills/claude-md-guide/ |
| harness-rule-reviewer | 规则文件静态分析审查 | skills/harness-rule-reviewer/ |

## 目录结构

```
floyd-skills/
├── CLAUDE.md                    # Claude Code 配置文件
├── AGENTS.md                    # OpenAI Codex 配置文件
├── README.md                    # 项目文档
├── skills/                      # 技能定义目录
│   ├── claude-md-guide/         # CLAUDE.md 编写指南技能
│   └── harness-rule-reviewer/   # 规则审查技能
├── .claude/
│   └── rules/                   # Claude Code 规则文件
│       ├── git-workflow.md      # Git 工作流规范
│       ├── code-style.md        # 代码风格规范
│       └── commit-conventions.md # 提交信息规范
└── .codex/
    └── rules/                   # Codex 规则文件 (可选)
```

## 跨平台兼容性

本项目同时支持 Claude Code 和 OpenAI Codex：

| 平台 | 配置文件 | 规则目录 | 文档 |
|------|----------|----------|------|
| Claude Code | `CLAUDE.md` | `.claude/rules/` | [Claude Code 文档](https://docs.anthropic.com/claude-code) |
| OpenAI Codex | `AGENTS.md` | `.codex/rules/` | [Codex CLI 文档](https://github.com/openai/codex) |

## 使用方式

### 调用技能

```
使用 claude-md-guide 帮我创建 CLAUDE.md
使用 harness-rule-reviewer 审查项目配置文件
```

### 跨平台审查

```
使用 harness-rule-reviewer 审查 CLAUDE.md 和 AGENTS.md 的一致性
使用 harness-rule-reviewer 对比两个平台的配置差异
```

### 查看技能列表

```
/skills
```

## 开发规范

### 技能文件结构

每个技能必须包含：
- `SKILL.md`: 技能定义文件，包含 YAML frontmatter 和 Markdown 内容

### 技能 frontmatter 格式

```yaml
---
name: skill-name
description: Brief description of what this skill does
---
```

## 常用命令

```bash
# 查看项目结构
ls -la

# 查看技能目录
ls -la skills/

# 查看规则目录
ls -la .claude/rules/
```