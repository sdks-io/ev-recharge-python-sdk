
# Get Charge Session Retrieve Response 200 Json

## Structure

`GetChargeSessionRetrieveResponse200Json`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `uuid\|str` | Required, Read-only | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request. |
| `status` | [`GetChargeSessionRetrieveResponse200JsonStatusEnum`](../../doc/models/get-charge-session-retrieve-response-200-json-status-enum.md) | Required, Read-only | **Constraints**: *Minimum Length*: `6`, *Maximum Length*: `15` |
| `data` | [`List[DataRetrieve]`](../../doc/models/data-retrieve.md) | Optional | - |

## Example

```python
from shellev.models.data_retrieve import DataRetrieve
from shellev.models.get_charge_session_retrieve_response_200_json import GetChargeSessionRetrieveResponse200Json
from shellev.models.get_charge_session_retrieve_response_200_json_status_enum import GetChargeSessionRetrieveResponse200JsonStatusEnum

get_charge_session_retrieve_response_200_json = GetChargeSessionRetrieveResponse200Json(
    request_id='9d2dee33-7803-485a-a2b1-2c7538e597ee',
    status=GetChargeSessionRetrieveResponse200JsonStatusEnum.SUCCESS,
    data=[
        DataRetrieve(
            id='00001c2a-0000-0000-0000-000000000000',
            user_id='userId0',
            ema_id='emaId8',
            evse_id='evseId2',
            last_updated='lastUpdated0'
        ),
        DataRetrieve(
            id='00001c2a-0000-0000-0000-000000000000',
            user_id='userId0',
            ema_id='emaId8',
            evse_id='evseId2',
            last_updated='lastUpdated0'
        )
    ]
)
```

