
# Inline Response 202 Data

## Structure

`InlineResponse202Data`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `session_id` | `str` | Optional | Session Id for tracking.<br><br>**Constraints**: *Minimum Length*: `36`, *Maximum Length*: `36`, *Pattern*: `^[{]?[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}[}]?$` |

## Example

```python
from shellev.models.inline_response_202_data import InlineResponse202Data

inline_response_202_data = InlineResponse202Data(
    session_id='c3e332f0-1bb2-4f50-a96b-e075bbb71e68'
)
```

