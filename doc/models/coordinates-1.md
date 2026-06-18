
# Coordinates 1

## Structure

`Coordinates1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `latitude` | `float` | Optional | Latitude of the Coordinate<br><br>**Constraints**: `>= -90`, `<= 90` |
| `longitude` | `float` | Optional | Longitude of the Coordinate<br><br>**Constraints**: `>= -180`, `<= 180` |

## Example

```python
from shellev.models.coordinates_1 import Coordinates1

coordinates_1 = Coordinates1(
    latitude=52.143814,
    longitude=52.143814
)
```

