# OWorker ACLIP

OWorker ACLIP 是 Agent Command Line Interface Protocol 的 OWorker 维护版。它保留 Rendo `aclip` 的协议、schema、Python SDK、TypeScript SDK、示例 CLI 和测试语义，并把开源入口迁移到 OWorker 生态。

ACLIP 的目标很明确：让一个普通 CLI 继续像普通 CLI 一样被人使用，同时让 Agent 能稳定读取命令结构、参数、认证需求、帮助文本、错误结果、诊断入口和可导出的 Skill 包。

## 安装

Python:

```bash
pip install oworker-aclip
```

Python 代码里的 import path 仍然是 `aclip`：

```python
from aclip import AclipApp, string_argument
```

TypeScript:

```bash
npm install @oworker/aclip
```

```ts
import { AclipApp, stringArgument } from "@oworker/aclip";
```

## 最小 CLI

Python:

```python
from aclip import AclipApp, run_cli, string_argument

app = AclipApp(
    name="notes",
    version="0.1.0",
    summary="A minimal notes CLI.",
    description="Create and inspect notes."
)

app.command(
    "create",
    summary="Create a note",
    description="Create a note with a title.",
    arguments=[string_argument("title", description="Note title")],
    handler=lambda title: {"created": True, "title": title},
)

if __name__ == "__main__":
    run_cli(app)
```

TypeScript:

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
  description: "Create a note with a title.",
  arguments: [stringArgument("title", { description: "Note title" })],
  handler: ({ title }) => ({ created: true, title })
});

runCli(app);
```

## 项目结构

- `schema/`: ACLIP 机器可读协议契约。
- `sdk/python/`: Python Click 参考适配器、测试、示例、打包脚本。
- `sdk/typescript/`: TypeScript Commander 参考适配器、测试、示例、打包脚本。
- `docs/`: OWorker 中文优先文档包，可通过 APCC 文档站阅读。
- `legacy/rendo-docs/`: Rendo 原始归档文档，保留历史设计判断。
- `legacy/rendo-README.md`: Rendo 原始根 README。

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
npm publish --dry-run --access public
```

## 文档入口

运行中的 APCC 文档站可用于浏览项目文档、目标与维护指南：

```powershell
apcc site start --port 4318
```

核心公开文档在 `docs/public/`，维护文档在 `docs/internal/`。
