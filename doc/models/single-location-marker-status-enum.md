
# Single Location Marker Status Enum

Minimum of all status values in the Marker, e.g. if at least one Evse in the Marker is available, the value will be available

## Enumeration

`SingleLocationMarkerStatusEnum`

## Fields

| Name |
|  --- |
| `AVAILABLE` |
| `OCCUPIED` |
| `UNAVAILABLE` |
| `UNKNOWN` |

## Example

```python
from shellev.models.single_location_marker_status_enum import SingleLocationMarkerStatusEnum

single_location_marker_status = SingleLocationMarkerStatusEnum.UNAVAILABLE
```

