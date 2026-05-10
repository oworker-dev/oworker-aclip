---
name: 打包 CLI
description: Python SDK 使用 build/build_cli 生成 binary 和 .aclip.json manifest。
---

# Python 打包 CLI

Python SDK 使用 PyInstaller 打包 CLI，并在输出目录生成 `.aclip.json` manifest。

## 准备 app

`main.py`：

```python
from aclip import AclipApp


def create_app() -> AclipApp:
    app = AclipApp(
        name="notes",
        version="0.1.0",
        summary="Notes CLI.",
        description="Create and list notes.",
    )
    return app


app = create_app()
```

## 构建

`build.py`：

```python
import aclip


artifact = aclip.build("main:create_app")

print(artifact.binary_path)
print(artifact.manifest_path)
```

运行：

```bash
python build.py
```

## 可用 target 形式

```python
aclip.build("main:app")
aclip.build(factory="main:create_app")
aclip.build(create_app)
```

`build` 是 `build_cli` 的别名。

## 产物

`CliArtifact` 包含：

- `binary_path`: 生成的可执行文件路径。
- `manifest_path`: `.aclip.json` 路径。
- `manifest`: 内存里的 manifest dict。

manifest 会写入：

- `protocol`
- CLI `name` / `version`
- 命令组和命令摘要
- credentials
- distribution，包含 standalone binary 名称、平台和 sha256。

## 常见问题

- `version is required`: 给 `AclipApp` 设置 `version`。
- import target 找不到：确认 `python build.py` 的工作目录能 import `main`。
- 本地包没被打进去：使用标准 `src/` 布局，或通过 `source_root` / `extra_paths` 显式传入路径。
