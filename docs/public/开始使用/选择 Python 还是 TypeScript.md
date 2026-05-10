---
name: 选择 Python 还是 TypeScript
description: 帮助使用者按项目形态选择 ACLIP Python SDK 或 TypeScript SDK。
---

# 选择 Python 还是 TypeScript

两个 SDK 都能声明 ACLIP CLI、生成帮助、构建 manifest、定义 auth/doctor，并导出 Agent Skills。选择主要取决于你要写的 CLI 属于哪个生态。

## 选 Python SDK

适合：

- CLI 本身依赖 Python 数据处理、机器学习、自动化脚本或本地文件处理。
- 你希望通过函数签名和 docstring 自动推断命令参数。
- 你要用 PyInstaller 打包本地 binary。
- 用户习惯 `pip install ...`。

安装：

```bash
pip install oworker-aclip
```

导入：

```python
from aclip import AclipApp, run_cli
```

注意：Python 发布包名是 `oworker-aclip`，但 import path 是 `aclip`。

## 选 TypeScript SDK

适合：

- CLI 属于 Node.js、前端工具链、npm workspace 或 TypeScript 项目。
- 你希望参数声明完全显式，并获得 TypeScript 类型检查。
- 你要发布 npm package 或构建 Node CLI artifact。
- 用户习惯 `npm install ...`。

安装：

```bash
npm install @oworker/aclip
```

导入：

```ts
import { AclipApp, runCli } from "@oworker/aclip";
```

## 两端能力对照

| 能力 | Python | TypeScript |
| --- | --- | --- |
| 根应用 `AclipApp` | 支持 | 支持 |
| 命令组 | 支持 | 支持 |
| 函数签名推断参数 | 支持 | 不支持 |
| 显式参数对象 | `ArgumentSpec` | `stringArgument` 等 helper |
| 认证凭证声明 | `CredentialSpec.env/file` | `envCredential/fileCredential` |
| auth 控制面 | `build_auth_control_plane` | `buildAuthControlPlane` |
| doctor 控制面 | `build_doctor_control_plane` | `buildDoctorControlPlane` |
| 打包 CLI | PyInstaller | tsup Node artifact |
| Skill 导出 | 支持 | 支持 |

如果你只是学习 ACLIP，建议先从与你现有项目语言一致的一端开始，不需要同时学两端。
