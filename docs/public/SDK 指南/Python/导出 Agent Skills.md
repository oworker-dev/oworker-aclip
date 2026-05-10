---
name: 导出 Agent Skills
description: Python SDK 中绑定 CLI/命令 Skill hook 并导出 Skill 包。
---

# Python 导出 Agent Skills

ACLIP 不自动生成 Skill 内容。Skill 源内容由开发者维护，ACLIP 负责校验、复制，并补充 CLI/命令元数据。

## 准备 Skill 源目录

```text
skills/
  notes-overview/
    SKILL.md
    references/
      README.md
```

`SKILL.md` 必须有 frontmatter：

```markdown
---
name: notes-overview
description: Use the notes CLI safely.
---

# Notes Overview

Use `notes note create` for new notes and `notes note list` before duplicate work.
```

## 绑定 hook

```python
from pathlib import Path

app.add_cli_skill(Path("skills") / "notes-overview")
app.add_command_skill(
    "note create",
    Path("skills") / "note-create-best-practice",
    metadata={"owner": "docs-team"},
)
```

命令级 hook 的路径可以是字符串 `"note create"`，也可以是 `("note", "create")`。

## 导出

```python
from pathlib import Path
from aclip import export_skills

artifact = export_skills(app, output_dir=Path("dist") / "skills")

print(artifact.index_path)
```

导出目录包含：

- `skills.aclip.json`
- 每个 Skill 包目录
- 原始 references 文件
- 被补充了 ACLIP 元数据的 `SKILL.md`

## 自动补充的元数据

CLI 级 hook：

- `aclip-hook-kind: cli`
- `aclip-cli-name`
- `aclip-cli-version`

命令级 hook 还会补充：

- `aclip-command-path`
- `aclip-command-summary`
- `aclip-command-description`

如果 app 有 `auth` 或 `doctor` 组，也会补充对应 group 元数据。
