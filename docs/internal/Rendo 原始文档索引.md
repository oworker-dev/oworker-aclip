---
name: Rendo 原始文档索引
description: legacy/rendo-docs 中原始文档的用途索引。
---

# Rendo 原始文档索引

Rendo 原始文档完整保存在：

```text
legacy/rendo-docs/
```

这些文档不作为当前 public 入口，但用于追溯设计判断。

## 核心协议与产品判断

- `PRD.md`: 原始产品需求、目标用户、协议需求和完成记录。
- `SPEC.md`: 协议语义、命令帮助、错误、manifest 等规范。
- `ARCHITECTURE.md`: 三层架构、SDK 边界和打包设计。
- `CONFORMANCE.md`: schema、文档、SDK 的一致性判断。

## 控制面与边界

- `AUTH-STANDARD.md`: credential、auth group、认证状态和错误码。
- `DOCTOR-CONTROL-PLANE.md`: doctor check/fix 控制面。
- `SESSION-CONTROL-PLANE.md`: session 控制面的历史讨论。
- `INTERACTIVE-CLI-BOUNDARY.md`: 为什么 ACLIP 不覆盖长期交互式 session。

## Skill 与互操作

- `SKILL-EXPORT-HOOKS-VPD.md`: Skill hook/export 的产品判断。
- `WORKFLOW-HOOKS-AND-SKILL-EXPORT.md`: workflow hook 退出 core 的历史判断。
- `INTEROPERABILITY-ARCHITECTURE.md`: import/export 与外部互操作边界。

## 发布与迭代

- `RELEASE-WORKFLOW.md`: Rendo 时代发布流程。
- `IMPLEMENTATION-PLAN.md`: 第一阶段实现计划。
- `VPD-NEXT-ITERATION-DECISIONS.md`: 下一轮产品判断。
- `TEN-YEAR-AGENT-TODO.md`: 旧迭代 TODO 和完成记录。

维护者改协议前应先查这些文档，确认是否存在已经讨论过的边界判断。
