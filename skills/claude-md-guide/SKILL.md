---
name: claude-md-guide
description: Guide for creating and maintaining CLAUDE.md files - project configuration files for Claude Code that provide project-specific context and instructions.
---

# CLAUDE.md 编写指南

## 概述
CLAUDE.md 是 Claude Code 的项目配置文件，用于为 Claude 提供项目特定的上下文、构建命令、代码风格和架构说明。好的 CLAUDE.md 能显著提升 Claude 在项目中的表现。

## 何时使用
- 需要为新项目创建 CLAUDE.md 配置文件
- 需要优化现有 CLAUDE.md 的结构和内容
- 需要了解 CLAUDE.md 的最佳实践和常见模式
- 需要为特定技术栈定制 CLAUDE.md 模板

## 文件位置优先级
1. **项目级**: `项目根目录/CLAUDE.md`（推荐，可提交到版本控制）
2. **用户级**: `~/.claude/CLAUDE.md`（全局配置，适用于所有项目）
3. **目录级**: `子目录/CLAUDE.md`（特定模块的额外配置）

## 核心结构模板

```markdown
# CLAUDE.md

## 项目概述
简要描述项目目的、技术栈、主要功能（2-3句话即可）。

## 构建和测试命令
```bash
# 开发
npm run dev

# 测试
npm test

# 构建
npm run build

# 代码检查
npm run lint
```

## 代码风格
- 缩进：2 空格
- 引号：单引号
- 命名：camelCase
- 导入顺序：外部库 → 内部模块 → 相对路径

## 项目结构
```
src/
├── components/    # React 组件
├── utils/         # 工具函数
├── types/         # TypeScript 类型
└── index.ts       # 入口文件
```

## 特殊说明
- 使用 ES 模块语法
- 测试文件放在 `__tests__` 目录
- 组件使用函数式 + Hooks
```

## 编写原则

### 1. 简洁优先
- 只包含对 Claude 有帮助的信息
- 避免重复 README 中的内容
- 使用清晰的标题和列表，避免冗长段落

### 2. 命令必须可执行
```bash
# ✅ 好的：具体可执行
npm test -- --testPathPattern=UserService

# ❌ 不好的：模糊描述
运行测试
```

### 3. 代码风格要具体
```markdown
# ✅ 好的：明确规则
- 使用 2 空格缩进
- 字符串使用单引号
- 语句末尾不加分号
- React 组件使用函数式组件 + Hooks

# ❌ 不好的：模糊描述
保持代码风格一致
```

### 4. 项目结构要说明用途
```markdown
# ✅ 好的：说明每个目录的作用
src/
├── components/    # 可复用的 UI 组件
├── pages/         # 页面组件，对应路由
├── hooks/         # 自定义 Hooks
├── services/      # API 调用服务
└── utils/         # 纯工具函数

# ❌ 不好的：只列目录名
src/
├── components/
├── pages/
├── hooks/
├── services/
└── utils/
```

## 技术栈特定模板

### React + TypeScript
```markdown
## 技术栈
- React 18 + TypeScript 5
- Vite 构建工具
- Tailwind CSS 样式
- Jest + React Testing Library 测试

## 代码规范
- 使用函数组件 + Hooks
- Props 接口以 `Props` 结尾（如 `UserCardProps`）
- 导出顺序：类型 → 组件 → 工具函数
- 使用 `const` 箭头函数定义组件

## 常用命令
```bash
npm run dev          # 启动开发服务器
npm run build        # 构建生产版本
npm test             # 运行所有测试
npm run lint         # ESLint 检查
npm run format       # Prettier 格式化
```
```

### Node.js + Express
```markdown
## 技术栈
- Node.js 20 + TypeScript
- Express.js 框架
- PostgreSQL + Prisma ORM
- Jest 测试框架

## 架构说明
- `src/routes/` - API 路由定义
- `src/controllers/` - 请求处理逻辑
- `src/services/` - 业务逻辑层
- `src/models/` - 数据模型和 Prisma Schema
- `src/middleware/` - Express 中间件

## 数据库相关
```bash
npx prisma migrate dev   # 运行数据库迁移
npx prisma generate      # 生成 Prisma Client
npx prisma studio        # 打开数据库管理界面
```
```

### Java + Spring Boot
```markdown
## 技术栈
- Java 21 + Spring Boot 3
- Maven 构建工具
- MyBatis Plus 持久层
- JUnit 5 测试

## 构建命令
```bash
mvn clean install        # 构建项目
mvn spring-boot:run      # 启动应用
mvn test                 # 运行测试
mvn checkstyle:check     # 代码规范检查
```

## 代码规范
- 使用 Lombok 简化代码
- Controller 只做参数校验和响应封装
- Service 层处理业务逻辑
- Mapper 层只做数据库操作
```

## 常见错误

| 错误 | 修正 |
|------|------|
| 内容过于冗长 | 只保留关键信息，避免复制 README |
| 命令不可执行 | 确保列出的命令真实可用 |
| 信息过时 | 定期更新，与项目保持同步 |
| 缺少实际示例 | 添加具体的代码示例 |
| 忽略特殊约束 | 列出禁止使用的特性或必须遵循的模式 |

## 高级用法

### 多语言项目
```markdown
## 语言偏好
- 代码注释：中文
- 变量命名：英文
- 文档：中文
- Git 提交信息：英文
```

### 微服务项目
```markdown
## 服务说明
- `user-service`: 用户管理服务（端口 8001）
- `order-service`: 订单服务（端口 8002）
- `gateway`: API 网关（端口 8000）

## 本地开发
需要同时启动多个服务时，使用 Docker Compose：
```bash
docker-compose up -d
```
```

### Monorepo 项目
```markdown
## 工作区说明
项目使用 pnpm workspace 管理：
- `packages/shared`: 共享工具库
- `packages/ui`: UI 组件库
- `apps/web`: Web 应用
- `apps/admin`: 管理后台

## 常用命令
```bash
pnpm install           # 安装所有依赖
pnpm --filter web dev  # 只启动 web 应用
pnpm -r run build      # 构建所有包
```
```

## 维护建议

1. **定期审查**: 每月检查一次 CLAUDE.md 是否与项目同步
2. **版本控制**: 将 CLAUDE.md 提交到 Git，团队共享
3. **团队协作**: 让团队成员共同维护，确保信息准确
4. **反馈循环**: 根据 Claude 的表现调整内容

## 相关资源
- [Claude Code 官方文档](https://docs.anthropic.com/claude-code)
- [CLAUDE.md 示例仓库](https://github.com/anthropics/claude-code-examples)