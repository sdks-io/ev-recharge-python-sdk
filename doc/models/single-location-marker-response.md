
# Single Location Marker Response

## Structure

`SingleLocationMarkerResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `uuid\|str` | Optional | requestId is unique identifier value that is attached to requests and messages that allow reference to a particular transaction or event chain. |
| `status` | `str` | Optional | status of the API call |
| `data` | List[[SingleLocationMarker](../../doc/models/single-location-marker.md) \| [MultiLocationMarker](../../doc/models/multi-location-marker.md)] \| None | Optional | - |

## Example

```python
from shellev.models.coordinates_1 import Coordinates1
from shellev.models.single_location_marker import SingleLocationMarker
from shellev.models.single_location_marker_response import SingleLocationMarkerResponse
from shellev.models.single_location_marker_status_enum import SingleLocationMarkerStatusEnum

single_location_marker_response = SingleLocationMarkerResponse(
    request_id='9d2dee33-7803-485a-a2b1-2c7538e597ee',
    status='SUCCESS',
    data=[
        SingleLocationMarker(
            marker_type='SingleLocation',
            unique_key='uniqueKey2',
            status=SingleLocationMarkerStatusEnum.AVAILABLE,
            coordinates=Coordinates1(
                latitude=39.14,
                longitude=36.94
            ),
            evse_count=26.34,
            max_power=241.78
        ),
        SingleLocationMarker(
            marker_type='SingleLocation',
            unique_key='uniqueKey2',
            status=SingleLocationMarkerStatusEnum.AVAILABLE,
            coordinates=Coordinates1(
                latitude=39.14,
                longitude=36.94
            ),
            evse_count=26.34,
            max_power=241.78
        ),
        SingleLocationMarker(
            marker_type='SingleLocation',
            unique_key='uniqueKey2',
            status=SingleLocationMarkerStatusEnum.AVAILABLE,
            coordinates=Coordinates1(
                latitude=39.14,
                longitude=36.94
            ),
            evse_count=26.34,
            max_power=241.78
        )
    ]
)
```

