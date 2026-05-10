# OWorker ACLIP

OWorker ACLIP 是 Agent Command Line Interface Protocol 的 OWorker 官方实现，属于 OWorker Open System -> Agent-Native Service Standard (ANSS) 下的 CLI/SDK/协议组件。

OWorker Open System / Agent-Native Service 是由 OWorker 团队维护的开放标准与开源工具体系，不是 OWorker 平台私有技术。OWorker 是维护者、首个核心应用者和核心受益者之一；开发者也可以用 ACLIP 和后续 Agent-Native Service Kit / Suite 构建标准 Agent 原生服务。

ACLIP 的目标：让普通 CLI 继续像普通 CLI 一样被人使用，同时让 Agent 能稳定读取命令结构、参数、认证需求、帮助文本、错误结果、诊断入口和可导出的 Skill 包。

## 安装

Python:

```bash
pip install oworker-aclip
```

Python 代码里的 import path 是 `aclip`：

```python
from aclip import AclipApp, run_cli
```

TypeScript:

```bash
npm install @oworker/aclip
```

```ts
import { AclipApp, runCli, stringArgument } from "@oworker/aclip";
```

## 最小 CLI

Python 通过函数签名和 docstring 推断参数：

```python
from aclip import AclipApp, run_cli


def create_app() -> AclipApp:
    app = AclipApp(
        name="notes",
        version="0.1.0",
        summary="A minimal notes CLI.",
        description="Create and inspect notes.",
    )

    def create_note(title: str, body: str) -> dict:
        """Create a note.

        Args:
            title: Note title.
            body: Note body.
        """
        return {"created": True, "title": title, "body": body}

    app.command(
        "create",
        handler=create_note,
        examples=["notes create --title hello --body world"],
    )
    return app


if __name__ == "__main__":
    run_cli(create_app)
```

TypeScript 通过 argument helper 显式声明参数：

```ts
import { AclipApp, runCli, stringArgument } from "@oworker/aclip";

const app = new AclipApp({
  name: "notes",
  version: "0.1.0",
  summary: "A minimal notes CLI.",
  description: "Create and inspect notes."
});

app.command("create", {
  summary: "Create a note",
  description: "Create a note.",
  arguments: [
    stringArgument("title", { required: true, description: "Note title." }),
    stringArgument("body", { required: true, description: "Note body." })
  ],
  examples: ["notes create --title hello --body world"],
  handler: ({ title, body }) => ({ created: true, title, body })
});

void runCli(app);
```

## 文档

使用者文档：

- `docs/public/开始使用`
- `docs/public/SDK 指南/Python`
- `docs/public/SDK 指南/TypeScript`
- `docs/public/示例`
- `docs/public/参考`

维护者文档：

- `docs/internal`

APCC 文档站：

```powershell
apcc site start --port 4318
```

## 项目结构

- `schema/`: ACLIP 机器可读协议契约。
- `sdk/python/`: Python Click 参考适配器、测试、示例、打包脚本。
- `sdk/typescript/`: TypeScript Commander 参考适配器、测试、示例、打包脚本。
- `docs/`: 中文优先文档包。

## 本地验证

Python:

```powershell
cd sdk\python
python -m pip install -e ".[dev]"
python -m pytest
python scripts\publish.py check
```

TypeScript:

```powershell
cd sdk\typescript
npm install
npm test
npm run check
npm run build
npm run release:check
```
