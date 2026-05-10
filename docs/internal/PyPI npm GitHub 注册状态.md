---
name: PyPI npm GitHub 注册状态
description: OWorker ACLIP 在开源注册中心的当前发布状态和 blocker。
---

# PyPI npm GitHub 注册状态

## GitHub

- 仓库：`https://github.com/oworker-dev/oworker-aclip`
- 状态：已创建，`main` 分支可用
- 注意：本地文档和 APCC 状态提交是否已同步远端，以 `git status -sb` 和远端 `main` commit 为准复核。

## npm

- 包名：`@oworker/aclip`
- 版本：`0.3.5`
- 状态：已发布并验证
- 验证命令：

```powershell
npm view @oworker/aclip version
```

干净安装验证已通过：

```powershell
npm install @oworker/aclip@0.3.5
node --input-type=module -e "import { AclipApp } from '@oworker/aclip'; console.log(Boolean(AclipApp))"
```

## PyPI

- 包名：`oworker-aclip`
- 目标版本：`0.3.5`
- 状态：构建和 `twine check` 已通过，上传被 `upload.pypi.org` 返回 `429 Too Many Requests`
- 当前处理：等待 PyPI 限流解除后重试。本次 npm 0.3.5 已发布，PyPI 仍未上线。

重试命令：

```powershell
cd sdk\python
python -m twine upload --non-interactive --disable-progress-bar --skip-existing dist\*
```

## 不发布短名 alias

本次不自动发布 PyPI 短名 alias `aclip`。原因：

- `aclip` 更适合作为代码 import path 和协议命名空间，而不是当前 canonical PyPI 包名。
- 自动发布短名 alias 可能制造安装入口和权限预期混乱。
- OWorker canonical 包名是 `oworker-aclip`。
