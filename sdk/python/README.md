# oworker-aclip

`oworker-aclip` 是 ACLIP 的 Python SDK。ACLIP 用来编写“人类能自然使用、Agent 能稳定理解”的 CLI。

Python 发布包名是 `oworker-aclip`，代码导入路径是 `aclip`。

## 安装

```bash
pip install oworker-aclip
```

```python
from aclip import AclipApp, run_cli
```

## 最小 CLI

`app.py`：

```python
from aclip import AclipApp, run_cli


def create_app() -> AclipApp:
    app = AclipApp(
        name="notes",
        version="0.1.0",
        summary="A minimal notes CLI.",
        description="Create and list notes.",
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
python app.py note create --title hello --body world
```

Python SDK 会从函数签名和 docstring 推断参数。需要完全控制时使用 `ArgumentSpec`。

## 常用能力

- `AclipApp`: 创建 CLI。
- `app.command(...)` / `app.group(...)`: 声明命令和命令组。
- `ArgumentSpec`: 显式声明参数、flag、choices、多值和位置参数。
- `CredentialSpec.env(...)` / `CredentialSpec.file(...)`: 声明凭证来源。
- `build_auth_control_plane(...)`: 添加 `auth login/status/logout`。
- `build_doctor_control_plane(...)`: 添加 `doctor check/fix`。
- `build(...)` / `build_cli(...)`: 生成 binary 和 `.aclip.json` manifest。
- `export_skills(...)`: 导出 Agent Skills 兼容包。

## 打包

```python
import aclip

artifact = aclip.build("app:create_app")
print(artifact.binary_path)
print(artifact.manifest_path)
```

## 文档

完整文档在 GitHub 仓库：

- 快速开始：`docs/public/开始使用`
- Python SDK 指南：`docs/public/SDK 指南/Python`
- 示例：`docs/public/示例/Python demo-notes 逐步讲解.md`
- 参考：`docs/public/参考`

仓库：<https://github.com/oworker-dev/oworker-aclip>
