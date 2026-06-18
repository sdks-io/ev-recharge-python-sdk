
# Search by Id Evse

Each Location will contain one or more EVSEs (Electric Vehicle Supply Equipment). Each EVSE is capable of charging one car at a time.

## Structure

`SearchByIdEvse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Optional | Internal identifier used to refer to single individual  EVSE unit. |
| `external_id` | `str` | Optional | Identifier of the Evse as given by the Operator, unique for that Operator |
| `evse_id` | `str` | Optional | Standard EVSEId identifier (ISO-IEC-15118) |
| `status` | [`EvseVOStatusEnum`](../../doc/models/evse-vo-status-enum.md) | Optional | The current status of the EVSE units availability |
| `updated` | `str` | Optional | ISO8601-compliant UTC datetime of the last update of the EVSE |
| `physical_reference` | `str` | Optional | An optional number/string printed on the outside of the EVSE for visual identification |
| `connectors` | [`List[SearchByIdConnector]`](../../doc/models/search-by-id-connector.md) | Optional | List of all connectors available on this EVSE unit. |
| `authorization_methods` | [`List[SingleLocationMarkerAuthorizationMethodsItemsEnum]`](../../doc/models/single-location-marker-authorization-methods-items-enum.md) | Optional | Methods that can be used to Authorize sessions on this EVSE |

## Example

```python
from shellev.models.evse_vo_status_enum import EvseVOStatusEnum
from shellev.models.search_by_id_evse import SearchByIdEvse
from shellev.models.single_location_marker_authorization_methods_items_enum import SingleLocationMarkerAuthorizationMethodsItemsEnum

search_by_id_evse = SearchByIdEvse(
    uid='NL*MKS*E0000001*0_1',
    external_id='01001188_1',
    evse_id='NL*TNM*E01000401*0',
    status=EvseVOStatusEnum.AVAILABLE,
    updated='2021-10-06T10:44:24Z',
    physical_reference='Green',
    authorization_methods=[
        SingleLocationMarkerAuthorizationMethodsItemsEnum.NEWMOTIONAPP
    ]
)
```

