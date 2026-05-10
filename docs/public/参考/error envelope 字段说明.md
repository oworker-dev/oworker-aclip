---
name: error envelope 字段说明
description: ACLIP 错误 envelope、标准错误码和退出码。
---

# error envelope 字段说明

错误输出写入 stderr，结构如下：

```json
{
  "protocol": "aclip/0.1",
  "type": "error",
  "ok": false,
  "command": "note create",
  "error": {
    "code": "validation_error",
    "message": "invalid command usage",
    "category": "input",
    "retryable": false,
    "hint": "Run notes note create --help."
  }
}
```

## 根字段

- `protocol`: 固定为 `aclip/0.1`。
- `type`: 固定为 `error`。
- `ok`: 固定为 `false`。
- `command`: 出错的命令路径。
- `error`: 错误详情。

## error 字段

- `code`: 稳定错误码。
- `message`: 人类可读错误说明。
- `category`: 可选分类。
- `retryable`: 可选，是否值得重试。
- `hint`: 可选，下一步提示。

## SDK 自动错误码

- `validation_error`: 参数解析、帮助路径、版本配置错误。
- `execution_error`: handler 执行时抛异常。

## 认证相关标准码

SDK 暴露 `AUTH_ERROR_CODES`：

- `auth_required`
- `invalid_credential`
- `expired_credential`

这些码通常由 CLI 作者在自己的业务逻辑或 auth 控制面中使用。

## 退出码

- `0`: 成功或帮助输出。
- `1`: handler 执行异常。
- `2`: 参数、帮助路径或版本配置错误。
