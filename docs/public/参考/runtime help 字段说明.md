---
name: runtime help 字段说明
description: ACLIP runtime help payload 的三种形态和字段含义。
---

# runtime help 字段说明

ACLIP 帮助是渐进式的。用户可以用普通命令查看 Markdown 帮助：

```bash
notes --help
notes note --help
notes note create --help
notes help --all
```

SDK 内部也会生成结构化 help payload，主要有三种。

## help_index

根帮助：

```json
{
  "protocol": "aclip/0.1",
  "type": "help_index",
  "summary": "Notes CLI.",
  "description": "Create and list notes.",
  "command_groups": [
    { "path": "note", "summary": "Manage notes" }
  ],
  "commands": [
    { "path": "status", "summary": "Show status" }
  ]
}
```

## help_command_group

命令组帮助：

```json
{
  "protocol": "aclip/0.1",
  "type": "help_command_group",
  "path": "note",
  "summary": "Manage notes",
  "description": "Create and inspect notes.",
  "commands": [
    { "path": "note create", "summary": "Create a note" }
  ]
}
```

## help_command

叶子命令帮助：

```json
{
  "protocol": "aclip/0.1",
  "type": "help_command",
  "path": "note create",
  "summary": "Create a note",
  "description": "Create a note.",
  "usage": "notes note create --title <string> --body <string>",
  "arguments": [],
  "examples": [
    "notes note create --title hello --body world"
  ]
}
```

## 参数字段

`arguments` 中每项来自参数 manifest：

- `name`
- `kind`
- `required`
- `description`
- `flag` / `flags`
- `position`
- `default`
- `choices`
- `multiple`
- `envVar`
