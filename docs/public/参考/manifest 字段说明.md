---
name: manifest 字段说明
description: .aclip.json manifest 的字段含义。
---

# manifest 字段说明

打包后，ACLIP 会在 artifact 旁生成 `.aclip.json` manifest。Agent 可以不运行 CLI，就先读取它理解 CLI 结构。

## 根字段

```json
{
  "protocol": "aclip/0.1",
  "name": "notes",
  "version": "0.1.0",
  "summary": "Notes CLI.",
  "description": "Create and list notes.",
  "command_groups": [],
  "commands": [],
  "credentials": [],
  "distribution": []
}
```

- `protocol`: 当前协议版本，固定为 `aclip/0.1`。
- `name`: CLI canonical name，来自 `AclipApp.name`。
- `version`: CLI 版本，来自 `AclipApp.version`。
- `summary`: 一句话摘要。
- `description`: 完整说明。
- `command_groups`: 命令组索引。
- `commands`: 命令索引。
- `credentials`: 凭证声明。
- `distribution`: 分发信息。

## command_groups

```json
{
  "path": "note",
  "summary": "Manage notes"
}
```

`path` 是空格连接的命令路径。

## commands

```json
{
  "path": "note create",
  "summary": "Create a note"
}
```

详细参数不在根 manifest 命令索引里展开；运行时帮助会给出命令详情。

## credentials

环境变量：

```json
{
  "name": "notes_token",
  "source": "env",
  "required": true,
  "description": "API token.",
  "envVar": "NOTES_TOKEN"
}
```

文件：

```json
{
  "name": "notes_token_file",
  "source": "file",
  "required": false,
  "description": "Local token file.",
  "path": ".secrets/notes-token.txt"
}
```

## distribution

Python binary：

```json
{
  "kind": "standalone_binary",
  "binary": "notes.exe",
  "platform": "win32-amd64",
  "sha256": "..."
}
```

TypeScript npm package：

```json
{
  "kind": "npm_package",
  "package": "@example/notes-cli",
  "version": "0.1.0",
  "executable": "notes"
}
```
