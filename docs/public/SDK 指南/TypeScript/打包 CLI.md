---
name: 打包 CLI
description: TypeScript SDK 使用 build/build_cli 生成 Node CLI artifact 和 .aclip.json manifest。
---

# TypeScript 打包 CLI

TypeScript SDK 使用 tsup 构建可运行 Node CLI artifact，并在输出目录生成 `.aclip.json` manifest。

## 准备 package.json

```json
{
  "name": "@example/notes-cli",
  "version": "0.1.0",
  "type": "module",
  "bin": {
    "notes": "./dist/notes.cjs"
  }
}
```

`package.json.version` 默认需要和 `AclipApp.version` 一致。不一致时要传 `packageVersion`。

## 构建

`scripts/build.ts`：

```ts
import { build_cli } from "@oworker/aclip";

const artifact = await build_cli({
  factory: "./src/app.ts:createApp",
  projectRoot: process.cwd(),
  outDir: "./dist"
});

console.log(artifact.entryPath);
console.log(artifact.manifestPath);
```

运行：

```bash
node --import tsx ./scripts/build.ts
```

## 可用 target 形式

```ts
await build_cli("./src/app.ts:app");
await build_cli({ factory: "./src/app.ts:createApp" });
await build_cli({
  factory: "./src/app.ts:createApp",
  packageName: "@example/notes-cli",
  packageVersion: "0.1.0"
});
```

`build` 是 `build_cli` 的别名。

## 产物

`CliArtifact` 包含：

- `entryPath`: 生成的 `.cjs` CLI 入口。
- `manifestPath`: `.aclip.json` 路径。
- `manifest`: 内存里的 manifest object。

manifest 的 distribution 会写入 npm package 信息：

- `kind: "npm_package"`
- `package`
- `version`
- `executable`

## 常见问题

- `package name is required`: 设置 `package.json.name` 或传 `packageName`。
- `package.json version does not match`: 对齐版本或传 `packageVersion`。
- import target 找不到：确认 `projectRoot` 和 `factory` 相对路径正确。
