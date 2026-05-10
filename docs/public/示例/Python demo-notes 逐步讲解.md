---
name: Python demo-notes 逐步讲解
description: 解释 Python demo-notes 示例的结构、命令和构建脚本。
---

# Python demo-notes 逐步讲解

示例位置：

```text
sdk/python/examples/demo-notes
```

## 示例做什么

`aclip-demo-notes` 是一个本地 notes CLI：

- `note create`: 写入一条 note 到 JSON 文件。
- `note list`: 读取 JSON 文件里的 notes。
- `--help`: 展示渐进式帮助。
- build script: 打包 binary 和 `.aclip.json` manifest。
- export script: 导出示例 Skill 包。

## 核心 app

代码位置：

```text
sdk/python/examples/demo-notes/src/aclip_demo_notes/app.py
```

核心结构：

```python
app = AclipApp(
    name="aclip-demo-notes",
    version="0.1.0",
    summary="Example notes CLI built with the aclip SDK",
    description="Stores notes in a local JSON file and exposes agent-first command disclosure.",
)
```

命令组：

```python
app.group(
    "note",
    summary="Manage notes",
    description="Create and list notes in the local JSON store.",
)
```

命令通过函数签名和 docstring 推断参数：

```python
def create_note(title: str, body: str, store: str = ".aclip-demo-notes.json") -> dict:
    """Create a note in a local JSON store.

    Args:
        title: Title for the note.
        body: Body text for the note.
        store: Path to the local note store.
    """
```

## 运行示例

从示例目录运行：

```powershell
python -m aclip_demo_notes --help
python -m aclip_demo_notes note create --title hello --body world
python -m aclip_demo_notes note list
```

## 打包

```powershell
python .\scripts\build.py
```

输出目录：

```text
dist/
  aclip-demo-notes.exe
  aclip-demo-notes.aclip.json
```

## 导出 Skills

```powershell
python .\scripts\export_skills.py
```

输出目录：

```text
dist/skills/
  skills.aclip.json
  notes-overview/
  note-create-best-practice/
```

这个示例适合作为 Python 新 CLI 的模板：先写 `create_app()`，再加命令组、handler、build script 和 export script。
