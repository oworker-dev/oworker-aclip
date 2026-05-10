---
name: 创建 AclipApp
description: Python AclipApp 的必要字段、版本规则和运行入口。
---

# Python 创建 AclipApp

`AclipApp` 是一个 CLI 的根对象。

```python
from aclip import AclipApp

app = AclipApp(
    name="notes",
    version="0.1.0",
    summary="A minimal notes CLI.",
    description="Create and list notes from a local JSON file.",
)
```

## 字段说明

- `name`: CLI 命令名，也是 manifest 里的 canonical name。必须是无空格的 CLI token，可用字母、数字、`.`、`_`、`-`。
- `version`: CLI 版本。运行本地命令时可省略，但构建 manifest、打包、Skill 导出和根 `--version` 需要它。
- `summary`: 一句话摘要，用于根帮助和 manifest。
- `description`: 更完整说明，用于帮助和 manifest。

## 版本行为

如果设置了 `version`：

```bash
python app.py --version
```

输出：

```text
notes 0.1.0
```

如果没有设置 `version`，根 `--version` 会返回结构化 validation error。准备打包或导出 Skill 前应设置版本。

## 推荐组织方式

把 app 创建函数和 CLI 入口拆开，方便打包工具按 import target 加载。

`main.py`：

```python
from aclip import AclipApp


def create_app() -> AclipApp:
    return AclipApp(
        name="notes",
        version="0.1.0",
        summary="A minimal notes CLI.",
        description="Create and list notes.",
    )


app = create_app()
```

`cli.py`：

```python
from aclip import run_cli
from main import create_app


run_cli(create_app)
```

后续打包时可以使用 `"main:create_app"` 或 `"main:app"`。
