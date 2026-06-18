
# Inline Response 2021

## Structure

`InlineResponse2021`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `uuid\|str` | Required, Read-only | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request. |
| `status` | [`GetChargeSessionRetrieveResponse200JsonStatusEnum`](../../doc/models/get-charge-session-retrieve-response-200-json-status-enum.md) | Required, Read-only | **Constraints**: *Minimum Length*: `6`, *Maximum Length*: `7` |

## Example

```python
from shellev.models.get_charge_session_retrieve_response_200_json_status_enum import GetChargeSessionRetrieveResponse200JsonStatusEnum
from shellev.models.inline_response_2021 import InlineResponse2021

inline_response_202_1 = InlineResponse2021(
    request_id='9d2dee33-7803-485a-a2b1-2c7538e597ee',
    status=GetChargeSessionRetrieveResponse200JsonStatusEnum.SUCCESS
)
```

