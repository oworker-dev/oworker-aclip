---
name: API 参考
description: TypeScript SDK 外部使用者常用公开 API 速查。
---

# TypeScript API 参考

## App 与运行

- `AclipApp`: 创建 CLI 根对象。
- `runCli(target, argv?)`: 运行 CLI，target 可为 app、factory、async factory 或 import target 字符串。
- `cliMain(...)`: `runCli` 的等价入口。

## 命令

- `app.command(name, registration)`: 添加根命令。
- `app.group(name, registration)`: 添加命令组，返回 `CommandGroupBuilder`。
- `group.command(...)`: 在组里添加命令。
- `group.group(...)`: 添加子命令组。

## 参数

- `stringArgument(name, options)`
- `integerArgument(name, options)`
- `booleanArgument(name, options)`
- `resolveFlags(argument)`
- `argumentToManifest(argument)`

## Credential

- `envCredential(name, options)`
- `fileCredential(name, options)`
- `credentialToManifest(credential)`

## Auth

- `buildAuthControlPlane(config)`
- `authStatusResult(status, options?)`
- `AUTH_STATES`
- 类型：`AuthCommandConfig`、`AuthStatus`、`AuthNextAction`

## Doctor

- `buildDoctorControlPlane(config)`
- `doctorResult(options)`
- `DOCTOR_CHECK_STATUSES`
- `DOCTOR_CHECK_SEVERITIES`
- 类型：`DoctorCommandConfig`、`DoctorCheck`、`DoctorRemediation`

## 打包与 Skill

- `build(targetOrOptions, overrides?)`: `build_cli` 的别名。
- `build_cli(...)`: 构建 Node CLI artifact 和 manifest。
- `loadAppFactory(target)`
- `loadAppTarget(target)`
- `export_skills(app, { outDir })`

## Runtime helper

通常不需要直接使用，但可用于高级集成：

- `renderSuccessOutput(data)`
- `resultEnvelope(command, data)`
- `errorEnvelope(command, code, message, options?)`
- `AUTH_ERROR_CODES`
