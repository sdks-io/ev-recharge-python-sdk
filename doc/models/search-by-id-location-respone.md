
# Search by Id Location Respone

## Structure

`SearchByIdLocationRespone`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Optional | Unique Internal identifier used to refer to this Location by Shell Recharge |
| `external_id` | `str` | Optional | Identifier as given by the Shell Recharge Operator, unique for that Operator |
| `coordinates` | [`Coordinates`](../../doc/models/coordinates.md) | Optional | Coordinates of the Shell Recharge Site Location |
| `operator_name` | `str` | Optional | Operator of this Shell Recharge Location |
| `address` | [`Address`](../../doc/models/address.md) | Optional | Address of the Shell Recharge Location |
| `accessibility` | [`AccessibilityV2`](../../doc/models/accessibility-v2.md) | Optional | Accessibility of the Location |
| `evses` | [`List[SearchByIdEvse]`](../../doc/models/search-by-id-evse.md) | Optional | - |
| `opening_hours` | [`List[OpeningHoursObject]`](../../doc/models/opening-hours-object.md) | Optional | Optional Opening Hours of the Location. Please note that it is not available for all sites. |
| `updated` | `str` | Optional | ISO8601-compliant UTC datetime of the last update of the location |
| `location_type` | `str` | Optional | the type of the location. Could be "UNKNOWN". |
| `operator_id` | `str` | Optional | Unique Id of the operator |
| `open_twenty_four_seven` | `bool` | Optional | Whether the location is open 24/7 |

## Example

```python
from shellev.models.address import Address
from shellev.models.coordinates import Coordinates
from shellev.models.search_by_id_location_respone import SearchByIdLocationRespone

search_by_id_location_respone = SearchByIdLocationRespone(
    uid='NL*MKS*E0000001*0',
    external_id='01001188',
    coordinates=Coordinates(
        latitude=39.14,
        longitude=36.94
    ),
    operator_name='TheNewMotion',
    address=Address(
        street_and_number='streetAndNumber2',
        postal_code='postalCode8',
        city='city6',
        country='country0'
    ),
    updated='2021-10-06T10:44:24Z',
    location_type='Unknown',
    operator_id='AT-HTB',
    open_twenty_four_seven=True
)
```

