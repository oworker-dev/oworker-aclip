---
name: Python SDK 指南
description: Python 参考 SDK 的核心 API、命令声明、认证、诊断和测试方法。
---

# Python SDK 指南

## 安装与导入

```bash
pip install oworker-aclip
```

```python
from aclip import AclipApp, run_cli
```

包名迁移为 `oworker-aclip`，import path 保持 `aclip`，这是为了兼容既有代码和协议术语。

## 命令声明

```python
from aclip import AclipApp, boolean_argument, string_argument

app = AclipApp(
    name="deploy",
    version="0.1.0",
    summary="Deploy a service.",
    description="Deploy and inspect service releases."
)

app.command(
    "ship",
    summary="Ship a release",
    description="Build and ship one release.",
    arguments=[
        string_argument("target", description="Release target"),
        boolean_argument("dry_run", description="Preview only", default=False),
    ],
    examples=["deploy ship production --dry-run"],
    handler=lambda target, dry_run=False: {"target": target, "dryRun": dry_run},
)
```

参数声明会被用于 Click 解析、ACLIP 帮助、manifest 和 schema 验证。

## 命令组

适合多层 CLI：

```python
notes = app.group("note", summary="Manage notes", description="Create and inspect notes.")

notes.command(
    "create",
    summary="Create a note",
    description="Create a note with a title.",
    arguments=[string_argument("title", description="Note title")],
    handler=lambda title: {"created": True, "title": title},
)
```

SDK 会把树形结构翻译成自然命令路径，例如 `notes note create "title"`。

## 装饰器写法

Python SDK 支持从函数签名和 docstring 生成命令声明。适合已有函数快速暴露为 CLI，但维护长期产品 CLI 时仍建议显式写清参数描述、示例和认证要求。

## 认证控制面

凭证来源分为环境变量和文件：

```python
from aclip import env_credential

app.add_credential(env_credential(
    "api_token",
    env_var="NOTES_TOKEN",
    description="Token for notes API.",
    required=True,
))
```

可以挂载可选 `auth` 命令组，提供 `login`、`status`、`logout` 语义。运行时帮助不会泄露凭证值，只暴露凭证来源和修复动作。

## Doctor 诊断

Doctor 是可选控制面，不是每个 CLI 的硬性要求。适合依赖环境变量、本地文件、外部 binary 或远端服务的 CLI。

诊断结果建议使用稳定 check name、状态、说明、remediation 和可选 fix 动作，让 Agent 能区分环境缺失、配置错误和外部服务故障。

## 本地测试

```powershell
cd sdk\python
python -m pip install -e ".[dev]"
python -m pytest
```

关键测试覆盖 Click 翻译、命令树、decorator authoring、manifest、demo CLI、packaging、auth、doctor、session 边界和 Skill 导出。
