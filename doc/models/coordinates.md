
# Coordinates

Coordinates of the Shell Recharge Site Location

## Structure

`Coordinates`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `latitude` | `float` | Optional | Latitude of the Coordinate<br><br>**Constraints**: `>= -90`, `<= 90` |
| `longitude` | `float` | Optional | Longitude of the Coordinate<br><br>**Constraints**: `>= -180`, `<= 180` |

## Example

```python
from shellev.models.coordinates import Coordinates

coordinates = Coordinates(
    latitude=52.143814,
    longitude=52.143814
)
```

