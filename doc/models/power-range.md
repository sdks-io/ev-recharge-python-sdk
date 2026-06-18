
# Power Range

## Structure

`PowerRange`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `min` | `int` | Required | Minimum supported power in kW |
| `max` | `int` | Required | Maximum supported power in kW |

## Example

```python
from shellev.models.power_range import PowerRange

power_range = PowerRange(
    min=0,
    max=100
)
```

