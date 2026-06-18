
# Accessibility V2

Accessibility of the Location

## Structure

`AccessibilityV2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | [`AccessibilityStatusEnum`](../../doc/models/accessibility-status-enum.md) | Optional | Accessibility Status |

## Example

```python
from shellev.models.accessibility_status_enum import AccessibilityStatusEnum
from shellev.models.accessibility_v_2 import AccessibilityV2

accessibility_v_2 = AccessibilityV2(
    status=AccessibilityStatusEnum.FREEPUBLIC
)
```

