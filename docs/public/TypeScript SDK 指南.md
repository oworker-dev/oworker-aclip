---
name: TypeScript SDK 指南
description: TypeScript 参考 SDK 的核心 API、命令声明、构建和测试方法。
---

# TypeScript SDK 指南

## 安装与导入

```bash
npm install @oworker/aclip
```

```ts
import { AclipApp, runCli } from "@oworker/aclip";
```

TypeScript SDK 使用 Commander 作为底层 CLI 解析适配器，外层 API 与 Python SDK 保持语义对齐。

## 命令声明

```ts
import { AclipApp, booleanArgument, stringArgument } from "@oworker/aclip";

const app = new AclipApp({
  name: "deploy",
  version: "0.1.0",
  summary: "Deploy a service.",
  description: "Deploy and inspect service releases."
});

app.command("ship", {
  summary: "Ship a release",
  description: "Build and ship one release.",
  arguments: [
    stringArgument("target", { description: "Release target" }),
    booleanArgument("dryRun", { description: "Preview only", defaultValue: false })
  ],
  examples: ["deploy ship production --dry-run"],
  handler: ({ target, dryRun }) => ({ target, dryRun })
});
```

## 命令组

```ts
const note = app.group("note", {
  summary: "Manage notes",
  description: "Create and inspect notes."
});

note.command("create", {
  summary: "Create a note",
  description: "Create a note with a title.",
  arguments: [stringArgument("title", { description: "Note title" })],
  handler: ({ title }) => ({ created: true, title })
});
```

## 构建 CLI artifact

```ts
import { build_cli } from "@oworker/aclip";

await build_cli({
  factory: "./src/app.ts:app",
  projectRoot: process.cwd(),
  outDir: "./dist"
});
```

构建结果包含可运行入口和 `.aclip.json` manifest。

## 本地测试

```powershell
cd sdk\typescript
npm install
npm test
npm run check
npm run build
```

关键测试覆盖 Commander 翻译、runtime help、manifest schema、consumer package-root import、demo CLI、packaging、auth、doctor 和 Skill 导出。
