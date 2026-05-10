---
name: 从 Rendo 包迁移到 OWorker 包
description: 从旧 Rendo aclip 包切换到 OWorker 维护入口的最小改动。
---

# 从 Rendo 包迁移到 OWorker 包

OWorker 迁移版保留协议名和核心 API，主要变更是开源包名与仓库入口。

## Python

旧依赖名：

```bash
pip install rendo-aclip
```

新依赖名：

```bash
pip install oworker-aclip
```

Python 代码里的 import path 不变：

```python
from aclip import AclipApp, run_cli
```

如果旧代码已经 `from aclip import ...`，通常只需要改项目依赖文件里的包名。

## TypeScript

旧依赖名：

```bash
npm install @rendo-studio/aclip
```

新依赖名：

```bash
npm install @oworker/aclip
```

代码导入需要替换：

```ts
import { AclipApp, runCli } from "@oworker/aclip";
```

## 保持不变

- 协议版本仍是 `aclip/0.1`。
- Python import path 仍是 `aclip`。
- `AclipApp`、命令组、认证、诊断、打包、Skill 导出语义保持对齐。
- Rendo 原始文档保存在 `legacy/rendo-docs/`，用于追溯设计判断。

## 发布状态

- GitHub: `https://github.com/oworker-dev/oworker-aclip`
- npm: `@oworker/aclip`
- PyPI: `oworker-aclip`

如果 PyPI 页面暂时不可用，以 internal 发布状态记录为准。
