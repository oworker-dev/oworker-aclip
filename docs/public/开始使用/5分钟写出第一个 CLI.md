---
name: 5分钟写出第一个 CLI
description: 不读源码，直接写出第一个 Python 或 TypeScript ACLIP CLI。
---

# 5分钟写出第一个 CLI

这页只做一件事：写出一个可运行的 `notes` CLI。

## Python 版本

安装：

```bash
pip install oworker-aclip
```

创建 `app.py`：

```python
from aclip import AclipApp, run_cli


def create_app() -> AclipApp:
    app = AclipApp(
        name="notes",
        version="0.1.0",
        summary="A minimal notes CLI.",
        description="Create and list notes from a local CLI.",
    )

    def create_note(title: str, body: str) -> dict:
        """Create a note.

        Args:
            title: Note title.
            body: Note body.
        """
        return {"note": {"title": title, "body": body}}

    app.group(
        "note",
        summary="Manage notes",
        description="Create and inspect notes.",
    ).command(
        "create",
        handler=create_note,
        examples=["notes note create --title hello --body world"],
    )

    return app


if __name__ == "__main__":
    run_cli(create_app)
```

运行：

```bash
python app.py --help
python app.py note --help
python app.py note create --title hello --body world
```

Python SDK 会从 `create_note(title: str, body: str)` 和 docstring 里推断出 `--title`、`--body` 两个 string 参数。

## TypeScript 版本

安装：

```bash
npm install @oworker/aclip tsx
```

创建 `app.ts`：

```ts
import { AclipApp, runCli, stringArgument } from "@oworker/aclip";

export function createApp() {
  const app = new AclipApp({
    name: "notes",
    version: "0.1.0",
    summary: "A minimal notes CLI.",
    description: "Create and list notes from a local CLI."
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
node --import tsx ./app.ts note --help
node --import tsx ./app.ts note create --title hello --body world
```

## 你刚刚用到了哪些 ACLIP 能力

- 根 CLI 元数据：`name`、`version`、`summary`、`description`。
- 命令组：`note`。
- 命令：`note create`。
- 参数：Python 从函数签名推断，TypeScript 显式声明。
- 成功输出：handler 返回 dict/object，SDK 输出 JSON。
- 帮助：`--help` 按命令路径渐进展示。

下一步读对应 SDK 指南，把参数、输出、auth、doctor、打包和 Skill 导出补齐。
