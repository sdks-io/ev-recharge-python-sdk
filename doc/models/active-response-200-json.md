
# Active Response 200 Json

## Structure

`ActiveResponse200Json`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `uuid\|str` | Required, Read-only | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request. |
| `status` | [`GetChargeSessionRetrieveResponse200JsonStatusEnum`](../../doc/models/get-charge-session-retrieve-response-200-json-status-enum.md) | Required, Read-only | **Constraints**: *Minimum Length*: `7`, *Maximum Length*: `7` |
| `data` | [`List[DataActive]`](../../doc/models/data-active.md) | Optional | - |

## Example

```python
import dateutil.parser

from shellev.models.active_response_200_json import ActiveResponse200Json
from shellev.models.data_active import DataActive
from shellev.models.get_charge_session_retrieve_response_200_json_status_enum import GetChargeSessionRetrieveResponse200JsonStatusEnum

active_response_200_json = ActiveResponse200Json(
    request_id='9d2dee33-7803-485a-a2b1-2c7538e597ee',
    status=GetChargeSessionRetrieveResponse200JsonStatusEnum.SUCCESS,
    data=[
        DataActive(
            id='00001c2a-0000-0000-0000-000000000000',
            user_id='userId0',
            ema_id='emaId8',
            evse_id='evseId2',
            started_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        ),
        DataActive(
            id='00001c2a-0000-0000-0000-000000000000',
            user_id='userId0',
            ema_id='emaId8',
            evse_id='evseId2',
            started_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        ),
        DataActive(
            id='00001c2a-0000-0000-0000-000000000000',
            user_id='userId0',
            ema_id='emaId8',
            evse_id='evseId2',
            started_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        )
    ]
)
```

