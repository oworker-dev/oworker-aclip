---
name: conformance 与 schema 维护
description: Python/TypeScript SDK、schema、测试和文档同步规则。
---

# conformance 与 schema 维护

## 双 SDK 必须语义对齐

Python 和 TypeScript API 风格可以不同，但协议语义必须一致：

- 相同的 manifest 字段。
- 相同的 runtime help payload 类型。
- 相同的 error envelope。
- 相同的 auth 状态集合。
- 相同的 doctor check 状态和 severity。
- 相同的 Skill export 元数据语义。

如果只改一端 SDK，必须说明另一端为什么不需要改。

## schema 变更流程

涉及下列字段时，先改 schema，再改 SDK：

- manifest 根字段或 distribution 字段。
- runtime help payload。
- result/error envelope。
- credential 表达。

流程：

1. 更新 `schema/*.schema.json`。
2. 同步 `sdk/python/src/aclip/_schema/`。
3. 同步 `sdk/typescript/schema/`。
4. 修改两个 SDK。
5. 修改测试。
6. 修改 public 参考文档。
7. 运行完整验证。

## 测试矩阵

Python：

```powershell
cd sdk\python
python -m pytest
python scripts\publish.py check
```

TypeScript：

```powershell
cd sdk\typescript
npm test
npm run check
npm run build
npm run release:check
```

APCC：

```powershell
apcc doctor check
```

## 文档同步规则

- 使用者能直接照抄的内容放 public。
- 维护判断、迁移背景、发布状态、协议边界放 internal。
- Rendo 原始文档只放 legacy，不作为当前 public 入口。
- 包 README 要能让 registry 用户完成最小上手，并链接到 GitHub docs。

## 禁止事项

- 不在 Python 文档里写不存在的 TypeScript helper，例如 `string_argument`。
- 不在 public 里要求用户理解 schema 才能写 CLI。
- 不让 registry README 指向只有本地仓库才看得到的相对路径作为唯一说明。
