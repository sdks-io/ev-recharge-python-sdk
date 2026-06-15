
# Multi Location Marker V2

A Marker is a place on the map that represent multiple Locations at the same spot

## Structure

`MultiLocationMarkerV2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `coordinates` | [`Coordinates`](../../doc/models/coordinates.md) | Optional | Coordinates of the Shell Recharge Site Location |
| `location_count` | `float` | Optional | Number of Locations that this Marker represents in the given set of bounds |
| `evse_count` | `float` | Optional | Total number of Evses in Locations that this Marker represents |
| `max_power` | `float` | Optional | Maximum power in kW across all locations grouped in this marker (disregarding availability) |
| `operator_name` | `str` | Optional | Operator of this Shell Recharge Location |
| `marker_type` | `str` | Required, Constant | Type of the Marker, in this case it will always be MultiLocation<br><br>**Value**: `"MultiLocation"` |

## Example (as JSON)

```json
{
  "locationCount": 6.0,
  "evseCount": 10.0,
  "maxPower": 42.0,
  "operatorName": "TheNewMotion",
  "markerType": "MultiLocation",
  "coordinates": {
    "latitude": 39.14,
    "longitude": 36.94
  }
}
```

