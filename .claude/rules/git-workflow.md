# Git Workflow Rules

## Context
Standardize Git workflow for team collaboration and code quality.

## Rules

### 1. Branch Naming Convention

Use descriptive branch names with prefixes:
```bash
# Feature branches
feature/user-authentication
feature/payment-integration

# Bug fix branches
bugfix/login-error
bugfix/validation-issue

# Hotfix branches
hotfix/security-patch

# Release branches
release/v1.2.0
```

### 2. Commit Message Format

Follow Conventional Commits specification:
```bash
# Format
<type>(<scope>): <description>

# Examples
feat(auth): add OAuth2 login support
fix(api): resolve null pointer in user endpoint
docs(readme): update installation instructions
refactor(utils): simplify date formatting functions
test(auth): add unit tests for login flow
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style (formatting, semicolons, etc.)
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

### 3. Pull Request Guidelines

#### Before Creating PR
```bash
# Ensure tests pass
npm test

# Run linting
npm run lint

# Update documentation if needed
# Add changelog entry if user-facing change
```

#### PR Description Template
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Manual testing completed

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No console.log statements left
```

### 4. Merge Strategy

- **Feature branches**: Squash and merge to main
- **Bugfix branches**: Squash and merge to main
- **Hotfix branches**: Merge to main and cherry-pick to release
- **Release branches**: Merge to main with tag

### 5. Protected Branches

- `main`: Requires PR review and passing CI
- `release/*`: Requires PR review
- Direct commits prohibited

### 6. Tagging Releases

Use semantic versioning:
```bash
# Create tag
git tag -a v1.2.0 -m "Release version 1.2.0"

# Push tag
git push origin v1.2.0
```

## Common Mistakes

| ❌ Don't | ✅ Do |
|----------|-------|
| `git commit -m "fix stuff"` | `fix(auth): resolve login timeout issue` |
| Direct commit to main | Create feature branch and PR |
| Force push to shared branches | Use `git revert` for corrections |
| Commit large binary files | Use Git LFS or exclude from repo |
| Mix unrelated changes | Keep PRs focused on single concern |