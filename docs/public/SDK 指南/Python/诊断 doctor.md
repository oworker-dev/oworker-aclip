---
name: 诊断 doctor
description: Python SDK 中添加 doctor check/fix 控制面的方式。
---

# Python 诊断 doctor

`doctor` 是可选命令组，适合有本地环境依赖的 CLI，例如需要 token、配置文件、外部 binary、网络连通性或工作目录结构。

## 添加 doctor 控制面

```python
from aclip import (
    DoctorCheck,
    DoctorCommandConfig,
    DoctorRemediation,
    build_doctor_control_plane,
    doctor_result,
)


def check(payload):
    return doctor_result(
        checks=[
            DoctorCheck(
                id="token",
                status="fail",
                summary="NOTES_TOKEN is missing.",
                severity="high",
                category="auth",
                hint="Set NOTES_TOKEN before calling remote commands.",
                remediation=[
                    DoctorRemediation(
                        summary="Login again.",
                        command="notes auth login",
                        automatable=False,
                    )
                ],
            )
        ],
        guidance_md="Fix high severity checks before running remote commands.",
    )


doctor = build_doctor_control_plane(
    DoctorCommandConfig(
        check_description="Inspect local environment.",
        check_examples=["notes doctor check"],
        check_handler=check,
        fix_description="Apply safe automatic fixes.",
        fix_examples=["notes doctor fix"],
        fix_handler=lambda payload: {"fixed": []},
    )
)
```

挂到 app：

```python
app = AclipApp(
    name="notes",
    version="0.1.0",
    summary="Notes CLI.",
    description="Remote notes CLI.",
    command_groups=[doctor.command_group],
    commands=doctor.commands,
)
```

## Check 字段

- `id`: 稳定检查 ID。
- `status`: `pass`、`warn`、`fail`。
- `summary`: 检查结果摘要。
- `severity`: `low`、`medium`、`high`、`critical`。
- `category`: 自定义分类，例如 `auth`、`network`、`filesystem`。
- `hint`: 简短提示。
- `remediation`: 修复建议列表。

`doctor fix` 是否真的修复由 CLI 作者决定。不要把有风险的动作伪装成自动修复。
