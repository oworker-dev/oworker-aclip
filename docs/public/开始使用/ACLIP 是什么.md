---
name: ACLIP 是什么
description: 面向 SDK 使用者解释 ACLIP 的用途、适用场景和基本工作方式。
---

# ACLIP 是什么

ACLIP 是 Agent Command Line Interface Protocol。它不是新的 Shell、不是 MCP，也不是一套强制的命令行框架。它是一组 SDK 和约定，用来把普通 CLI 写成“人能自然使用、Agent 也能稳定理解”的 CLI。

一个 ACLIP CLI 仍然像普通 CLI 一样运行：

```bash
notes --help
notes note create --title hello --body world
notes note list
```

不同点在于，CLI 作者在代码里把命令、参数、认证、诊断和 Skill hook 明确声明出来。SDK 会把这些信息用于：

- 普通 `--help` Markdown 帮助。
- `help` 命令和 `--all` 展开的渐进式帮助。
- `.aclip.json` sidecar manifest。
- 结构化错误 envelope。
- 可选 `auth` 和 `doctor` 控制面。
- 可选 Agent Skills 导出。

## 什么时候适合用 ACLIP

适合：

- 你要写一个给人和 Agent 都会用的 CLI。
- CLI 有多层命令、参数、认证或环境依赖。
- 你希望 Agent 不靠猜测阅读 README，而是能读取 manifest、help payload 和错误结构。
- 你希望把 CLI 使用经验导出为 Agent Skill 包。

不适合：

- 你只需要一个一次性脚本。
- 你要标准化长期 REPL、浏览器会话、远程服务市场或多 Agent 编排。
- 你希望从任意已有 CLI 自动推断完整协议。ACLIP 是作者声明式协议，不是逆向推断器。

## 使用者需要掌握的核心概念

- `AclipApp`: 一个 CLI 应用的根对象，包含名称、版本、摘要、描述、命令、凭证和 Skill hook。
- command: 可执行命令，例如 `note create`。
- command group: 命令分组，例如 `note`。
- argument: 命令参数，支持 string、integer、boolean、默认值、choices、多值和自定义 flags。
- credential: 凭证声明，支持环境变量和本地文件来源。
- doctor: 可选诊断命令组，用于检查环境和修复建议。
- manifest: 打包后生成的 `.aclip.json`，给 Agent 读取 CLI 结构和分发信息。
- Skill export: 把开发者维护的 Skill 包复制出来，并补充 ACLIP 元数据。

## 选择 SDK

- 写 Python CLI：使用 PyPI 包 `oworker-aclip`，代码里 `from aclip import ...`。
- 写 TypeScript CLI：使用 npm 包 `@oworker/aclip`。

两个 SDK 的协议语义对齐，但 API 风格不同。Python 更偏函数签名和 docstring 推断；TypeScript 更偏显式 `stringArgument`、`integerArgument`、`booleanArgument` helper。
