---
name: Agent Skill 导出
description: ACLIP 如何从 CLI 和命令级 hook 导出 Agent Skills 兼容包。
---

# Agent Skill 导出

## 为什么需要 Skill 导出

Agent 需要的不只是命令参数，还需要方法论：什么时候用某个命令、如何组合步骤、哪些输入危险、常见失败如何修复。ACLIP 的 Skill hook 让 CLI 作者把这些知识绑定到 CLI 或具体命令上。

## Hook 类型

- CLI 级 hook：描述整个 CLI 的使用原则。
- 命令级 hook：描述某个命令路径的最佳实践。

导出的 Skill 包会补充 ACLIP 元数据，例如 CLI 名称、hook 类型、命令路径和命令摘要。

## Python 导出

示例项目：

```powershell
cd sdk\python\examples\demo-notes
python .\scripts\export_skills.py
```

导出结果位于 `dist\skills`。运行普通 CLI 命令不会自动打印 Skill 文件，导出是显式动作。

## TypeScript 导出

```powershell
cd sdk\typescript\examples\demo-notes
node --import tsx .\scripts\export-skills.ts
```

## 维护规范

Skill 源内容由开发者维护，ACLIP 只负责复制、校验和补充协议锚点。不要把 Skill 文案从 runtime help 自动生成出来；runtime help 负责命令结构，Skill 负责操作判断和经验。
