---
name: 诊断 doctor
description: TypeScript SDK 中添加 doctor check/fix 控制面的方式。
---

# TypeScript 诊断 doctor

`doctor` 是可选命令组，适合有本地环境依赖的 CLI。

## 添加 doctor 控制面

```ts
import {
  buildDoctorControlPlane,
  doctorResult
} from "@oworker/aclip";

const doctor = buildDoctorControlPlane({
  checkDescription: "Inspect local environment.",
  checkExamples: ["notes doctor check"],
  checkHandler: () => doctorResult({
    checks: [{
      id: "token",
      status: "fail",
      summary: "NOTES_TOKEN is missing.",
      severity: "high",
      category: "auth",
      hint: "Set NOTES_TOKEN before calling remote commands.",
      remediation: [{
        summary: "Login again.",
        command: "notes auth login",
        automatable: false
      }]
    }],
    guidance_md: "Fix high severity checks before running remote commands."
  }),
  fixDescription: "Apply safe automatic fixes.",
  fixExamples: ["notes doctor fix"],
  fixHandler: () => ({ fixed: [] })
});
```

挂到 app：

```ts
const app = new AclipApp({
  name: "notes",
  version: "0.1.0",
  summary: "Notes CLI.",
  description: "Remote notes CLI.",
  commandGroups: [doctor.commandGroup],
  commands: doctor.commands
});
```

## Check 字段

- `id`: 稳定检查 ID。
- `status`: `pass`、`warn`、`fail`。
- `summary`: 检查结果摘要。
- `severity`: `low`、`medium`、`high`、`critical`。
- `category`: 自定义分类。
- `hint`: 简短提示。
- `remediation`: 修复建议列表。

`doctor fix` 是否真的修复由 CLI 作者决定。不要把有风险的动作伪装成自动修复。
