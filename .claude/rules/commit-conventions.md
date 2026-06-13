# Commit Conventions

## Context
Standardized commit messages for automated changelog generation and clear project history.

## Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Header (Required)
- **Type**: What kind of change
- **Scope**: What area of code (optional)
- **Subject**: Imperative, present tense, no period

### Types

| Type | Description | Example |
|------|-------------|---------|
| `feat` | New feature | `feat(auth): add OAuth2 support` |
| `fix` | Bug fix | `fix(api): handle null response` |
| `docs` | Documentation | `docs(readme): update setup guide` |
| `style` | Formatting, no code change | `style: fix indentation` |
| `refactor` | Code restructuring | `refactor(utils): extract helpers` |
| `perf` | Performance improvement | `perf(query): optimize database calls` |
| `test` | Add/update tests | `test(auth): add login tests` |
| `build` | Build system/dependencies | `build: update webpack config` |
| `ci` | CI/CD changes | `ci: add GitHub Actions workflow` |
| `chore` | Maintenance tasks | `chore: update dependencies` |
| `revert` | Revert commit | `revert: undo feature X` |

### Scope (Optional)
Common scopes:
- `auth` - Authentication
- `api` - API endpoints
- `ui` - User interface
- `db` - Database
- `config` - Configuration
- `deps` - Dependencies

### Subject Rules
- Use imperative mood ("add" not "added" or "adds")
- Don't capitalize first letter
- No period at the end
- Max 50 characters

### Body (Optional)
- Explain **what** and **why**, not **how**
- Wrap at 72 characters
- Separate from subject with blank line

### Footer (Optional)
- Reference issues: `Closes #123`
- Breaking changes: `BREAKING CHANGE: description`

## Examples

### Simple Change
```
feat(auth): add password reset functionality
```

### With Body
```
fix(api): handle network timeout errors

Previously, the API client would hang indefinitely on network errors.
Now implements a 30-second timeout with proper error handling.

Closes #456
```

### Breaking Change
```
feat(api): change response format

BREAKING CHANGE: API responses now use {data, error} format instead of
returning data directly. Update all API consumers.

Closes #789
```

### Multiple Changes
```
refactor(auth): restructure authentication module

- Extract JWT logic to separate service
- Move validation to middleware
- Update tests for new structure

Closes #101, #102
```

## Validation Rules

### Pre-commit Checks
```bash
# Commit message must match pattern
^(feat|fix|docs|style|refactor|perf|test|build|ci|chore|revert)(\(.+\))?: .{1,50}

# No WIP commits on main
git log --oneline --grep="WIP" main..HEAD
```

### CI Checks
- Commit message format validation
- No merge commits with default messages
- Signed commits (optional)

## Common Mistakes

| ❌ Don't | ✅ Do |
|----------|-------|
| `Fixed bug` | `fix(auth): resolve login timeout` |
| `Update README` | `docs: update installation guide` |
| `WIP: working on feature` | `feat(api): add user endpoints` (when complete) |
| `fix: Fix the thing` | `fix: resolve login timeout` (lowercase, no "Fix") |
| `feat: add feature.` | `feat: add feature` (no period) |

## Changelog Integration

Commits with these types appear in changelog:
- `feat` → Features section
- `fix` → Bug Fixes section
- `perf` → Performance section
- Breaking changes → Breaking Changes section

## Tooling

### Commitlint
```bash
# Install
npm install --save-dev @commitlint/cli @commitlint/config-conventional

# commitlint.config.js
module.exports = {
  extends: ['@commitlint/config-conventional'],
  rules: {
    'type-enum': [2, 'always', [
      'feat', 'fix', 'docs', 'style', 'refactor',
      'perf', 'test', 'build', 'ci', 'chore', 'revert'
    ]],
    'subject-max-length': [2, 'always', 50],
  },
};
```

### Husky
```bash
# Install
npm install --save-dev husky

# Setup
npx husky install
npx husky add .husky/commit-msg 'npx --no -- commitlint --edit $1'
```