
# Search by Id Response

## Structure

`SearchByIdResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `uuid\|str` | Optional | requestId is unique identifier value that is attached to requests and messages that allow reference to a particular transaction or event chain. |
| `status` | `str` | Optional | status of the API call |
| `data` | [`List[SearchByIdLocationRespone]`](../../doc/models/search-by-id-location-respone.md) | Optional | API Response |

## Example

```python
from shellev.models.address import Address
from shellev.models.coordinates import Coordinates
from shellev.models.search_by_id_location_respone import SearchByIdLocationRespone
from shellev.models.search_by_id_response import SearchByIdResponse

search_by_id_response = SearchByIdResponse(
    request_id='9d2dee33-7803-485a-a2b1-2c7538e597ee',
    status='SUCCESS',
    data=[
        SearchByIdLocationRespone(
            uid='uid0',
            external_id='externalId6',
            coordinates=Coordinates(
                latitude=39.14,
                longitude=36.94
            ),
            operator_name='operatorName0',
            address=Address(
                street_and_number='streetAndNumber2',
                postal_code='postalCode8',
                city='city6',
                country='country0'
            )
        ),
        SearchByIdLocationRespone(
            uid='uid0',
            external_id='externalId6',
            coordinates=Coordinates(
                latitude=39.14,
                longitude=36.94
            ),
            operator_name='operatorName0',
            address=Address(
                street_and_number='streetAndNumber2',
                postal_code='postalCode8',
                city='city6',
                country='country0'
            )
        )
    ]
)
```

