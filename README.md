# Floyd Skills

Claude Code Skills 技能库，用于管理和组织可复用的 Claude Code 技能。同时兼容 OpenAI Codex，支持跨平台配置审查。

## 什么是 Skills？

Skills 是 Claude Code 的可复用能力模块，可以通过 `/skill-name` 或对话中直接调用来使用。每个技能定义了特定的任务流程、角色和输出格式。

## 当前技能

| 技能 | 描述 | 调用方式 |
|------|------|----------|
| [claude-md-guide](.claude/skills/claude-md-guide/) | CLAUDE.md 编写指南 | `使用 claude-md-guide` |
| [harness-rule-reviewer](.claude/skills/harness-rule-reviewer/) | 规则文件静态分析审查 | `使用 harness-rule-reviewer` |
| [possession](.claude/skills/possession/) | 角色扮演蒸馏器：从游戏设定中蒸馏可扮演角色 | `使用 possession` |

## Soul 人格设定

`soul/` 目录存放 AI 人格设定文件，用于定义 AI 助手的性格、语气和行为模式。

| 人格 | 描述 | 特点 |
|------|------|------|
| [豆包型小龙虾](soul/豆包型小龙虾.md) | 勤奋真诚、呆萌反差的 AI 助手 | 嘴甜、不内耗、道歉速度快 |

## 项目结构

```
floyd-skills/
├── CLAUDE.md                    # Claude Code 配置文件
├── AGENTS.md                    # OpenAI Codex 配置文件
├── README.md                    # 本文件
├── soul/                        # AI 人格设定目录
│   └── 豆包型小龙虾.md           # 豆包型人格设定
├── .claude/
│   ├── skills/                  # 技能定义目录
│   │   ├── claude-md-guide/     # CLAUDE.md 编写指南技能
│   │   │   └── SKILL.md
│   │   ├── harness-rule-reviewer/ # 规则审查技能
│   │   │   └── SKILL.md
│   │   └── possession/            # 角色扮演蒸馏器
│   │       └── SKILL.md
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

## 使用方法

### 调用技能

在 Claude Code 对话中：

```
使用 claude-md-guide 帮我为 React 项目创建 CLAUDE.md
使用 harness-rule-reviewer 审查项目的规则文件
```

### 跨平台审查

```
使用 harness-rule-reviewer 审查 CLAUDE.md 和 AGENTS.md 的一致性
使用 harness-rule-reviewer 对比两个平台的配置差异
```

### 查看可用技能

```
/skills
```

## 添加新技能

1. 在 `.claude/skills/` 下创建新目录
2. 创建 `SKILL.md` 文件，包含必要的 frontmatter：

```yaml
---
name: your-skill-name
description: Brief description of what this skill does
---

# Skill Title

## Overview
[Skill description]

## When to Use
[Usage scenarios]

## Process
[Step-by-step process]

## Output Format
[Expected output format]
```

3. 更新本 README 的技能列表

## 技能开发指南

### Frontmatter 字段

| 字段 | 必需 | 描述 |
|------|------|------|
| `name` | ✅ | 技能名称，使用 kebab-case |
| `description` | ✅ | 一句话描述技能用途 |

### 内容结构建议

1. **Overview**: 技能概述
2. **When to Use**: 使用场景和条件
3. **Process**: 详细步骤流程
4. **Output Format**: 输出格式要求
5. **Examples**: 示例用法
6. **Quality Checklist**: 质量检查清单

### 减法哲学

设计技能时遵循减法哲学：
- 只包含必要的步骤
- 避免过度规范化
- 保持清晰和可操作性
- 每个规则都要有存在的理由

## 规则文件

项目还包含一套规则文件，用于规范 AI 编码助手的行为：

| 规则文件 | 描述 | 适用平台 |
|----------|------|----------|
| git-workflow.md | Git 分支、提交、PR 规范 | Claude Code, Codex |
| code-style.md | 代码风格和命名规范 | Claude Code, Codex |
| commit-conventions.md | 提交信息格式规范 | Claude Code, Codex |

这些规则文件可以通过 `harness-rule-reviewer` 技能进行审查和优化，支持跨平台一致性检查。

## 相关资源

- [Claude Code 文档](https://docs.anthropic.com/claude-code)
- [Claude Code Skills 最佳实践](https://docs.anthropic.com/claude-code/skills)
- [OpenAI Codex CLI](https://github.com/openai/codex)
- [AGENTS.md 规范](https://github.com/openai/codex/blob/main/docs/agents.md)

## License

MIT