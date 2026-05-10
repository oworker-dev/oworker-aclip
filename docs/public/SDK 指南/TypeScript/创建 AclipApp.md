---
name: 创建 AclipApp
description: TypeScript AclipApp 的必要字段、版本规则和运行入口。
---

# TypeScript 创建 AclipApp

```ts
import { AclipApp } from "@oworker/aclip";

const app = new AclipApp({
  name: "notes",
  version: "0.1.0",
  summary: "A minimal notes CLI.",
  description: "Create and list notes from a local JSON file."
});
```

## 字段说明

- `name`: CLI 命令名，也是 manifest 里的 canonical name。必须是无空格的 CLI token，可用字母、数字、`.`、`_`、`-`。
- `version`: CLI 版本。运行本地命令时可省略，但构建 manifest、打包、Skill 导出和根 `--version` 需要它。
- `summary`: 一句话摘要，用于根帮助和 manifest。
- `description`: 更完整说明，用于帮助和 manifest。
- `commands` / `commandGroups`: 可选，适合用对象一次性传入命令树。
- `credentials`: 可选凭证声明。
- `cliSkills` / `commandSkills`: 可选 Skill hook。

## 版本行为

```bash
node --import tsx ./src/cli.ts --version
```

输出：

```text
notes 0.1.0
```

如果没有设置 `version`，根 `--version` 会返回结构化 validation error。准备打包或导出 Skill 前应设置版本。

## 推荐组织方式

`src/app.ts`：

```ts
import { AclipApp } from "@oworker/aclip";

export function createApp() {
  return new AclipApp({
    name: "notes",
    version: "0.1.0",
    summary: "Notes CLI.",
    description: "Create and list notes."
  });
}

export const app = createApp();
```

`src/cli.ts`：

```ts
import { runCli } from "@oworker/aclip";
import { createApp } from "./app.js";

void runCli(createApp);
```

后续打包时可以使用 `"./src/app.ts:createApp"` 或 `"./src/app.ts:app"`。
