---
name: 常见模式 cookbook
description: 常见 ACLIP CLI 写法片段，方便使用者复制改造。
---

# 常见模式 cookbook

## 给命令加短参数

Python：

```python
ArgumentSpec(
    name="store",
    kind="string",
    description="Path to local store.",
    flags=("--store", "-s"),
    default=".notes.json",
)
```

TypeScript：

```ts
stringArgument("store", {
  flags: ["--store", "-s"],
  description: "Path to local store.",
  defaultValue: ".notes.json"
})
```

## 写位置参数

Python：

```python
ArgumentSpec(
    name="query",
    kind="string",
    description="Search query.",
    required=True,
    positional=True,
)
```

TypeScript：

```ts
stringArgument("query", {
  description: "Search query.",
  required: true,
  positional: true
})
```

## handler 返回纯文本

Python：

```python
def status() -> str:
    return "ok"
```

TypeScript：

```ts
handler: () => "ok"
```

## handler 返回 JSON

Python：

```python
def status() -> dict:
    return {"status": "ok"}
```

TypeScript：

```ts
handler: () => ({ status: "ok" })
```

## 为远程 API 声明 token

Python：

```python
CredentialSpec.env(
    name="api_token",
    env_var="API_TOKEN",
    description="Remote API token.",
    required=True,
)
```

TypeScript：

```ts
envCredential("api_token", {
  envVar: "API_TOKEN",
  description: "Remote API token.",
  required: true
})
```

## 加一个健康检查

Python：

```python
DoctorCheck(
    id="config-file",
    status="warn",
    summary="Config file is missing; defaults will be used.",
    severity="medium",
)
```

TypeScript：

```ts
{
  id: "config-file",
  status: "warn",
  summary: "Config file is missing; defaults will be used.",
  severity: "medium"
}
```

## 导出命令级 Skill

Python：

```python
app.add_command_skill("note create", "skills/note-create-best-practice")
```

TypeScript：

```ts
app.addCommandSkill("note create", "skills/note-create-best-practice");
```
