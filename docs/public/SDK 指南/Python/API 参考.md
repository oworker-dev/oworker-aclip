---
name: API 参考
description: Python SDK 外部使用者常用公开 API 速查。
---

# Python API 参考

## App 与运行

- `AclipApp(...)`: 创建 CLI 根对象。
- `run_cli(target, argv=None)`: 运行 CLI，target 可为 app、factory 或 import target 字符串。
- `cli_main(...)`: `run_cli` 的等价入口。

## 命令

- `app.command(name, ..., handler=...)`: 添加根命令。
- `app.group(name, summary, description)`: 添加命令组，返回 `CommandGroupBuilder`。
- `group.command(...)`: 在组里添加命令。
- `group.group(...)`: 添加子命令组。

## 参数与契约对象

- `ArgumentSpec`: 显式参数定义。
- `CommandSpec`: 显式命令定义。
- `CommandGroupSpec`: 显式命令组定义。
- `CredentialSpec.env(...)`: 环境变量凭证。
- `CredentialSpec.file(...)`: 文件凭证。
- `DistributionSpec.standalone_binary(...)`: binary 分发元数据。
- `DistributionSpec.npm_package(...)`: npm 分发元数据。

## Auth

- `AuthCommandConfig`: `auth login/status/logout` 配置。
- `AuthStatus`: 认证状态。
- `AuthNextAction`: 下一步动作。
- `build_auth_control_plane(config)`: 生成 auth 命令组和命令列表。
- `auth_status_result(status, guidance_md=None)`: 生成 auth status payload。

## Doctor

- `DoctorCommandConfig`: `doctor check/fix` 配置。
- `DoctorCheck`: 单项检查结果。
- `DoctorRemediation`: 修复建议。
- `build_doctor_control_plane(config)`: 生成 doctor 命令组和命令列表。
- `doctor_result(checks, guidance_md=None)`: 生成 doctor payload。

## 打包与 Skill

- `build(target, ...)`: `build_cli` 的别名。
- `build_cli(target, ...)`: 构建 binary 和 manifest。
- `load_app_factory(target)`: 加载 app factory。
- `load_app_target(target)`: 加载 app 或 factory。
- `export_skills(app, output_dir=...)`: 导出 Skill 包。

## Runtime helper

通常不需要直接使用，但可用于高级集成：

- `render_success_output(data)`
- `result_envelope(command, data)`
- `error_envelope(command, code, message, ...)`
- `AUTH_ERROR_CODES`
