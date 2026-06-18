
# Charge Error

## Structure

`ChargeError`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `str` | Optional | Session code e.g InternalError |
| `message` | `str` | Optional | Session message |

## Example

```python
from shellev.models.charge_error import ChargeError

charge_error = ChargeError(
    code='code8',
    message='message0'
)
```

