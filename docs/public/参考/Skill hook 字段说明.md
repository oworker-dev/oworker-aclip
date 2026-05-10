---
name: Skill hook 字段说明
description: ACLIP Skill hook 和 skills.aclip.json 的字段含义。
---

# Skill hook 字段说明

ACLIP Skill 导出是显式动作。SDK 不生成 Skill 正文，只复制开发者维护的 Skill 包并补充元数据。

## 源 Skill 包要求

```text
skills/
  notes-overview/
    SKILL.md
    references/
      README.md
```

`SKILL.md` 必须包含：

```markdown
---
name: notes-overview
description: Use the notes CLI safely.
---
```

`name` 必须是 lowercase kebab-case。

## CLI 级 hook

Python：

```python
app.add_cli_skill("skills/notes-overview")
```

TypeScript：

```ts
app.addCliSkill("skills/notes-overview");
```

导出后补充：

- `aclip-hook-kind: cli`
- `aclip-cli-name`
- `aclip-cli-version`

## 命令级 hook

Python：

```python
app.add_command_skill("note create", "skills/note-create-best-practice")
```

TypeScript：

```ts
app.addCommandSkill("note create", "skills/note-create-best-practice");
```

导出后额外补充：

- `aclip-command-path`
- `aclip-command-summary`
- `aclip-command-description`

## skills.aclip.json

```json
{
  "protocol": "aclip-skill-export/0.1",
  "cli": {
    "name": "notes",
    "version": "0.1.0"
  },
  "packages": [
    {
      "name": "notes-overview",
      "kind": "cli",
      "path": "notes-overview"
    },
    {
      "name": "note-create-best-practice",
      "kind": "command",
      "path": "note-create-best-practice",
      "commandPath": "note create"
    }
  ]
}
```

Agent 可以先读 `skills.aclip.json`，再按 path 加载具体 Skill 包。
