# @oworker/aclip

`@oworker/aclip` 是 ACLIP 的 TypeScript SDK。ACLIP 用来编写“人类能自然使用、Agent 能稳定理解”的 CLI。

## 安装

```bash
npm install @oworker/aclip
```

开发时通常也会安装 `tsx`：

```bash
npm install -D tsx
```

## 最小 CLI

`app.ts`：

```ts
import { AclipApp, runCli, stringArgument } from "@oworker/aclip";

export function createApp() {
  const app = new AclipApp({
    name: "notes",
    version: "0.1.0",
    summary: "A minimal notes CLI.",
    description: "Create and list notes."
  });

  app.group("note", {
    summary: "Manage notes",
    description: "Create and inspect notes."
  }).command("create", {
    summary: "Create a note",
    description: "Create a note.",
    arguments: [
      stringArgument("title", { required: true, description: "Note title." }),
      stringArgument("body", { required: true, description: "Note body." })
    ],
    examples: ["notes note create --title hello --body world"],
    handler: ({ title, body }) => ({ note: { title, body } })
  });

  return app;
}

void runCli(createApp);
```

运行：

```bash
node --import tsx ./app.ts --help
node --import tsx ./app.ts note create --title hello --body world
```

## 常用能力

- `AclipApp`: 创建 CLI。
- `app.command(...)` / `app.group(...)`: 声明命令和命令组。
- `stringArgument(...)` / `integerArgument(...)` / `booleanArgument(...)`: 声明参数。
- `envCredential(...)` / `fileCredential(...)`: 声明凭证来源。
- `buildAuthControlPlane(...)`: 添加 `auth login/status/logout`。
- `buildDoctorControlPlane(...)`: 添加 `doctor check/fix`。
- `build(...)` / `build_cli(...)`: 生成 Node CLI artifact 和 `.aclip.json` manifest。
- `export_skills(...)`: 导出 Agent Skills 兼容包。

## 打包

```ts
import { build_cli } from "@oworker/aclip";

const artifact = await build_cli({
  factory: "./app.ts:createApp",
  projectRoot: process.cwd(),
  outDir: "./dist"
});

console.log(artifact.entryPath);
console.log(artifact.manifestPath);
```

## 文档

完整文档在 GitHub 仓库：

- 快速开始：`docs/public/开始使用`
- TypeScript SDK 指南：`docs/public/SDK 指南/TypeScript`
- 示例：`docs/public/示例/TypeScript demo-notes 逐步讲解.md`
- 参考：`docs/public/参考`

仓库：<https://github.com/oworker-dev/oworker-aclip>
