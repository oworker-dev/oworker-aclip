---
name: 认证 auth
description: TypeScript SDK 中声明 credential 和添加可选 auth 控制面的方式。
---

# TypeScript 认证 auth

## 声明凭证

```ts
import { AclipApp, envCredential, fileCredential } from "@oworker/aclip";

const app = new AclipApp({
  name: "notes",
  version: "0.1.0",
  summary: "Notes CLI.",
  description: "Remote notes CLI.",
  credentials: [
    envCredential("notes_token", {
      envVar: "NOTES_TOKEN",
      description: "API token for the notes service.",
      required: true
    }),
    fileCredential("notes_token_file", {
      path: ".secrets/notes-token.txt",
      description: "Optional local token file."
    })
  ]
});
```

credential 会进入 manifest 和帮助信息，但不会输出凭证值。

## 添加 auth 控制面

```ts
import {
  buildAuthControlPlane,
  authStatusResult
} from "@oworker/aclip";

const auth = buildAuthControlPlane({
  loginDescription: "Login to the notes service.",
  loginExamples: ["notes auth login"],
  loginHandler: () => ({ status: "logged_in" }),
  statusDescription: "Show current auth state.",
  statusExamples: ["notes auth status"],
  statusHandler: () => authStatusResult({
    state: "authenticated",
    principal: "dev@example.com",
    next_actions: [{
      summary: "Refresh before running long jobs.",
      command: "notes auth login"
    }]
  }),
  logoutDescription: "Logout from the notes service.",
  logoutExamples: ["notes auth logout"],
  logoutHandler: () => ({ status: "logged_out" })
});

const app = new AclipApp({
  name: "notes",
  version: "0.1.0",
  summary: "Notes CLI.",
  description: "Remote notes CLI.",
  commandGroups: [auth.commandGroup],
  commands: auth.commands
});
```

## Auth 状态

可用状态：

- `authenticated`
- `unauthenticated`
- `expired`
- `partial`
- `unknown`

`authStatusResult(status, { guidance_md })` 可追加给 Agent 读取的下一步说明。
