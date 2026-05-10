---
name: 认证 auth
description: Python SDK 中声明 credential 和添加可选 auth 控制面的方式。
---

# Python 认证 auth

ACLIP 把认证拆成两层：

- credential 声明：告诉 Agent 凭证来自哪里。
- auth 控制面：可选的 `auth login/status/logout` 命令组。

## 声明凭证

```python
from aclip import AclipApp, CredentialSpec

app = AclipApp(
    name="notes",
    version="0.1.0",
    summary="Notes CLI.",
    description="Remote notes CLI.",
    credentials=[
        CredentialSpec.env(
            name="notes_token",
            env_var="NOTES_TOKEN",
            description="API token for the notes service.",
            required=True,
        ),
        CredentialSpec.file(
            name="notes_token_file",
            path=".secrets/notes-token.txt",
            description="Optional local token file.",
        ),
    ],
)
```

credential 会进入 manifest 和帮助信息，但不会输出凭证值。

## 添加 auth 控制面

```python
from aclip import (
    AuthCommandConfig,
    AuthNextAction,
    AuthStatus,
    build_auth_control_plane,
    auth_status_result,
)

auth = build_auth_control_plane(
    AuthCommandConfig(
        login_description="Login to the notes service.",
        login_examples=["notes auth login"],
        login_handler=lambda payload: {"status": "logged_in"},
        status_description="Show current auth state.",
        status_examples=["notes auth status"],
        status_handler=lambda payload: auth_status_result(
            AuthStatus(
                state="authenticated",
                principal="dev@example.com",
                next_actions=[
                    AuthNextAction(
                        summary="Refresh before running long jobs.",
                        command="notes auth login",
                    )
                ],
            )
        ),
        logout_description="Logout from the notes service.",
        logout_examples=["notes auth logout"],
        logout_handler=lambda payload: {"status": "logged_out"},
    )
)

app = AclipApp(
    name="notes",
    version="0.1.0",
    summary="Notes CLI.",
    description="Remote notes CLI.",
    command_groups=[auth.command_group],
    commands=auth.commands,
)
```

## AuthStatus 状态

可用状态：

- `authenticated`
- `unauthenticated`
- `expired`
- `partial`
- `unknown`

`auth_status_result(...)` 可追加 `guidance_md`，给 Agent 更明确的下一步说明。
