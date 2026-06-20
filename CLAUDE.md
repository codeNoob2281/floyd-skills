# CLAUDE.md

## 项目概述

这是一个 Claude Code Skills 技能库项目，用于管理和组织可复用的 Claude Code 技能（Skills）。同时兼容 OpenAI Codex，支持跨平台配置审查。

## 技能列表

当前项目包含以下技能：

| 技能名称 | 描述 | 位置 |
|----------|------|------|
| claude-md-guide | CLAUDE.md 编写指南 | skills/claude-md-guide/ |
| harness-rule-reviewer | 规则文件静态分析审查 | skills/harness-rule-reviewer/ |
| possession | 角色扮演蒸馏器：从游戏设定中蒸馏可扮演角色 | skills/possession/ |

## Soul 人格设定

`soul/` 目录存放 AI 人格设定文件，用于定义 AI 助手的性格、语气和行为模式：

| 人格 | 描述 | 特点 |
|------|------|------|
| 豆包型小龙虾 | 勤奋真诚、呆萌反差的 AI 助手 | 嘴甜、不内耗、道歉速度快 |

## 游戏角色档案

`characters/` 目录存放通过 possession 技能蒸馏的游戏角色档案，包含完整的角色设定：

| 角色 | 游戏 | 描述 | 质量评分 |
|------|------|------|----------|
| 派蒙 | 原神 | 旅行者的向导，话痨小吃货 | 0.881 (优秀) |

### 角色档案结构

每个角色目录包含：
- `SKILL.md`：角色扮演入口文件
- `profile.md`：角色档案（基本信息、世界观定位）
- `personality.md`：性格与价值观
- `interaction.md`：说话方式与台词
- `memory.md`：背景故事
- `relations.md`：人际关系网络
- `conflicts.md`：设定冲突记录
- `manifest.json`：元数据
- `test-report.md`：扮演测试报告
- `quality-report.md`：质量评分报告

## 目录结构

```
floyd-skills/
├── CLAUDE.md                    # Claude Code 配置文件
├── AGENTS.md                    # OpenAI Codex 配置文件
├── README.md                    # 项目文档
├── skills/                      # 技能定义目录
│   ├── claude-md-guide/         # CLAUDE.md 编写指南技能
│   ├── harness-rule-reviewer/   # 规则审查技能
│   └── possession/              # 角色扮演蒸馏器
├── characters/                  # 游戏角色档案目录
│   └── paimon/                  # 派蒙（原神）
│       └── SOUL.md              # 派蒙人格设定
├── soul/                        # AI 人格设定目录
│   └── 豆包型小龙虾.md           # 豆包型人格设定
├── .claude/
│   ├── hooks.json               # Claude Code hooks 配置
│   ├── hooks/                   # Hook 脚本目录
│   │   ├── check-edit-count.sh  # 检查编辑次数
│   │   ├── record-edit.sh       # 记录编辑历史
│   │   └── cleanup-edit-history.sh # 清理临时文件
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

# 查看 hooks 配置
cat .claude/hooks.json
```

## Hooks 说明

本项目配置了 Claude Code hooks 用于防止重复编辑：

| Hook | 时机 | 功能 |
|------|------|------|
| PreToolUse | 编辑前 | 检查同一文件是否已连续编辑 10 次，是则拦截 |
| PostToolUse | 编辑后 | 记录编辑历史 |
| Stop | 会话结束 | 清理临时历史文件 |

**目的**：防止在同一文件上陷入无效的循环编辑，促使重新审视修改策略。