
# Single Location Marker Response V2

## Structure

`SingleLocationMarkerResponseV2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `uuid\|str` | Optional | requestId is unique identifier value that is attached to requests and messages that allow reference to a particular transaction or event chain. |
| `status` | `str` | Optional | status of the API call |
| `data` | List[[SingleLocationMarkerV2](../../doc/models/single-location-marker-v2.md) \| [MultiLocationMarkerV2](../../doc/models/multi-location-marker-v2.md)] \| None | Optional | - |

## Example

```python
from shellev.models.coordinates import Coordinates
from shellev.models.single_location_marker_response_v_2 import SingleLocationMarkerResponseV2
from shellev.models.single_location_marker_status_enum import SingleLocationMarkerStatusEnum
from shellev.models.single_location_marker_v_2 import SingleLocationMarkerV2

single_location_marker_response_v_2 = SingleLocationMarkerResponseV2(
    request_id='9d2dee33-7803-485a-a2b1-2c7538e597ee',
    status='SUCCESS',
    data=[
        SingleLocationMarkerV2(
            status=SingleLocationMarkerStatusEnum.UNAVAILABLE,
            coordinates=Coordinates(
                latitude=39.14,
                longitude=36.94
            ),
            evse_count=223.04,
            max_power=45.08,
            location_count=62.98
        ),
        SingleLocationMarkerV2(
            status=SingleLocationMarkerStatusEnum.UNAVAILABLE,
            coordinates=Coordinates(
                latitude=39.14,
                longitude=36.94
            ),
            evse_count=223.04,
            max_power=45.08,
            location_count=62.98
        ),
        SingleLocationMarkerV2(
            status=SingleLocationMarkerStatusEnum.UNAVAILABLE,
            coordinates=Coordinates(
                latitude=39.14,
                longitude=36.94
            ),
            evse_count=223.04,
            max_power=45.08,
            location_count=62.98
        )
    ]
)
```

