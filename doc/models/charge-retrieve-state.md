
# Charge Retrieve State

## Structure

`ChargeRetrieveState`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `str` | Optional | Describes the session state<br><br>started, stopped, start-requested, stop-requested, failed-to-start, failed-to-stop |
| `error` | [`ChargeError`](../../doc/models/charge-error.md) | Optional | - |

## Example

```python
from shellev.models.charge_error import ChargeError
from shellev.models.charge_retrieve_state import ChargeRetrieveState

charge_retrieve_state = ChargeRetrieveState(
    status='status8',
    error=ChargeError(
        code='code2',
        message='message4'
    )
)
```

