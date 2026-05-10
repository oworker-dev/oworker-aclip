---
name: TypeScript demo-notes 逐步讲解
description: 解释 TypeScript demo-notes 示例的结构、命令和构建脚本。
---

# TypeScript demo-notes 逐步讲解

示例位置：

```text
sdk/typescript/examples/demo-notes
```

## 示例做什么

`aclip-demo-notes` 是一个本地 notes CLI：

- `note create`: 写入一条 note 到 JSON 文件。
- `note list`: 读取 JSON 文件里的 notes。
- `--help`: 展示渐进式帮助。
- build script: 打包 Node CLI artifact 和 `.aclip.json` manifest。
- export script: 导出示例 Skill 包。

## 核心 app

代码位置：

```text
sdk/typescript/examples/demo-notes/src/app.ts
```

核心结构：

```ts
const app = new AclipApp({
  name: "aclip-demo-notes",
  version: "0.1.0",
  summary: "Example notes CLI built with the aclip SDK",
  description: "Stores notes in a local JSON file and exposes agent-first command disclosure."
});
```

参数显式声明：

```ts
stringArgument("title", { required: true, description: "Title for the note." })
```

handler 从 payload 读取值：

```ts
handler: (payload) => {
  const title = String(payload.title);
  const body = String(payload.body);
  return { note: { title, body } };
}
```

## 运行示例

从 TypeScript SDK 根目录运行测试或示例脚本时，依赖已由 workspace 安装：

```powershell
cd sdk\typescript
npm install
node --import tsx .\examples\demo-notes\src\cli.ts --help
node --import tsx .\examples\demo-notes\src\cli.ts note create --title hello --body world
```

## 打包

```powershell
cd sdk\typescript\examples\demo-notes
node --import tsx .\scripts\build.ts
```

输出目录：

```text
dist/
  aclip-demo-notes.cjs
  aclip-demo-notes.aclip.json
```

## 导出 Skills

```powershell
node --import tsx .\scripts\export-skills.ts
```

输出目录：

```text
dist/skills/
  skills.aclip.json
  notes-overview/
  note-create-best-practice/
```

这个示例适合作为 TypeScript 新 CLI 的模板：先写 `createApp()`，再写 `cli.ts`，最后补 build/export scripts。
