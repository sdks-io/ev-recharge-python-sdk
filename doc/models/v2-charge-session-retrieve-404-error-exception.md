
# V2 Charge Session Retrieve 404 Error Exception

## Structure

`V2ChargeSessionRetrieve404ErrorException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Optional | requestId is unique identifier value that is attached to requests and messages that allow reference to a particular transaction or event chain. |
| `status` | `str` | Optional | Status of the request |
| `errors` | [`List[NotFoundErrMsg]`](../../doc/models/not-found-err-msg.md) | Optional | Exception details of the error |

## Example

```python
try:
    # make the API call
except V2ChargeSessionRetrieve404ErrorException as e:
    print(e)
except APIException as e:
    print(e)
```

