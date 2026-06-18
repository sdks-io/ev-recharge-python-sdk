
# Inline Response 202

## Structure

`InlineResponse202`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `uuid\|str` | Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request. |
| `status` | [`GetChargeSessionRetrieveResponse200JsonStatusEnum`](../../doc/models/get-charge-session-retrieve-response-200-json-status-enum.md) | Required | Indicates overall status of the request |
| `data` | [`List[InlineResponse202Data]`](../../doc/models/inline-response-202-data.md) | Required | - |

## Example

```python
from shellev.models.get_charge_session_retrieve_response_200_json_status_enum import GetChargeSessionRetrieveResponse200JsonStatusEnum
from shellev.models.inline_response_202 import InlineResponse202
from shellev.models.inline_response_202_data import InlineResponse202Data

inline_response_202 = InlineResponse202(
    request_id='9d2dee33-7803-485a-a2b1-2c7538e597ee',
    status=GetChargeSessionRetrieveResponse200JsonStatusEnum.SUCCESS,
    data=[
        InlineResponse202Data(
            session_id='c3e332f0-1bb2-4f50-a96b-e075bbb71e68'
        )
    ]
)
```

