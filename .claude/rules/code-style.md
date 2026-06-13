# Code Style Rules

## Context
Maintain consistent code style across the project for readability and maintainability.

## General Principles

### 1. Formatting
- **Indentation**: 2 spaces (not tabs)
- **Line Length**: Max 100 characters
- **Semicolons**: No semicolons (ASI)
- **Quotes**: Single quotes for strings
- **Trailing Commas**: Yes for multi-line

### 2. Naming Conventions

| Element | Convention | Example |
|---------|------------|---------|
| Variables | camelCase | `userName`, `isActive` |
| Constants | UPPER_SNAKE | `MAX_RETRIES`, `API_URL` |
| Functions | camelCase | `getUserById`, `formatDate` |
| Classes | PascalCase | `UserService`, `ApiClient` |
| Components | PascalCase | `UserCard`, `NavigationBar` |
| Interfaces | PascalCase + `I` prefix (optional) | `IUser` or `User` |
| Types | PascalCase | `UserProfile`, `ApiResponse` |
| Enums | PascalCase | `UserRole`, `HttpStatus` |
| Files (components) | PascalCase | `UserCard.tsx` |
| Files (utilities) | camelCase | `formatDate.ts` |
| Files (tests) | Same as source + `.test` | `UserCard.test.tsx` |

### 3. Import Organization

Order imports in this sequence:
```typescript
// 1. React and external libraries
import React, { useState, useEffect } from 'react';
import { useQuery } from '@tanstack/react-query';
import axios from 'axios';

// 2. Internal absolute imports
import { User } from '@/types/user';
import { UserService } from '@/services/user';
import { Button } from '@/components/ui/Button';

// 3. Relative imports
import { UserCard } from './UserCard';
import { formatDate } from './utils';

// 4. Styles
import './UserList.css';
```

### 4. Component Structure

```typescript
// 1. Imports
import React from 'react';

// 2. Types/Interfaces
interface UserCardProps {
  user: User;
  onSelect: (user: User) => void;
}

// 3. Component
export const UserCard: React.FC<UserCardProps> = ({ user, onSelect }) => {
  // 3a. Hooks
  const [isSelected, setIsSelected] = useState(false);
  
  // 3b. Event handlers
  const handleClick = () => {
    setIsSelected(true);
    onSelect(user);
  };
  
  // 3c. Render
  return (
    <div onClick={handleClick}>
      {user.name}
    </div>
  );
};
```

### 5. Function Style

```typescript
// ✅ Arrow functions for components and callbacks
const UserCard: React.FC<Props> = ({ user }) => {
  return <div>{user.name}</div>;
};

// ✅ Regular functions for utilities
function formatDate(date: Date): string {
  return date.toLocaleDateString();
}

// ✅ Object methods
const userService = {
  getUser(id: string) {
    return api.get(`/users/${id}`);
  },
};
```

## TypeScript Rules

### 1. Type Safety
```typescript
// ✅ Explicit types for function signatures
function getUser(id: string): Promise<User> {
  return api.get(`/users/${id}`);
}

// ✅ Infer types when obvious
const name = 'John'; // string is inferred

// ❌ Avoid `any`
const data: any = getData();

// ✅ Use `unknown` for truly unknown types
const data: unknown = getData();
```

### 2. Interface vs Type
```typescript
// ✅ Use interfaces for object shapes
interface User {
  id: string;
  name: string;
}

// ✅ Use types for unions, intersections, primitives
type UserRole = 'admin' | 'user' | 'guest';
type UserWithPosts = User & { posts: Post[] };
```

### 3. Null Handling
```typescript
// ✅ Use optional chaining
const userName = user?.profile?.name;

// ✅ Use nullish coalescing
const displayName = userName ?? 'Anonymous';

// ✅ Explicit null checks
if (user !== null) {
  // use user
}
```

## React Rules

### 1. Component Definitions
```typescript
// ✅ Arrow function with explicit type
const UserCard: React.FC<UserCardProps> = ({ user }) => {
  return <div>{user.name}</div>;
};

// ✅ Export at declaration
export const UserCard: React.FC<UserCardProps> = ({ user }) => {
  return <div>{user.name}</div>;
};
```

### 2. Hooks Usage
```typescript
// ✅ Destructure hooks
const [count, setCount] = useState(0);
const { data, isLoading } = useQuery(['user'], fetchUser);

// ✅ Custom hooks start with "use"
function useUser(userId: string) {
  return useQuery(['user', userId], () => fetchUser(userId));
}
```

### 3. Event Handlers
```typescript
// ✅ Prefix with "handle"
const handleClick = () => { /* ... */ };
const handleSubmit = (e: FormEvent) => { /* ... */ };

// ✅ Prefix props with "on"
interface Props {
  onClick: () => void;
  onSubmit: (data: FormData) => void;
}
```

## CSS/Styling Rules

### 1. Tailwind CSS
```typescript
// ✅ Use Tailwind classes
<div className="flex items-center gap-2 p-4">

// ✅ Conditional classes with template literals
<div className={`${isActive ? 'bg-blue-500' : 'bg-gray-200'}`}>

// ✅ Use cn() utility for complex conditions
<div className={cn(
  'base-class',
  isActive && 'active-class',
  variant === 'primary' && 'primary-class'
)}>
```

## Common Mistakes

| ❌ Don't | ✅ Do |
|----------|-------|
| `var x = 1` | `const x = 1` or `let x = 1` |
| `function Component()` | `const Component: React.FC = () =>` |
| Inline styles everywhere | Use Tailwind or CSS modules |
| Magic numbers | Named constants |
| Deep nesting (3+ levels) | Extract components or early returns |
| Console.log in production | Use proper logging |
| Commented-out code | Delete it (use git history) |