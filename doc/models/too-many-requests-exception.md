
# Too Many Requests Exception

## Structure

`TooManyRequestsException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Optional | RequestID is unique identifier value that is attached to requests and messages that allow reference to a particular transaction or event chain. |
| `status` | `str` | Optional | Status of the request |
| `errors` | [`List[RatelimitErrMsg]`](../../doc/models/ratelimit-err-msg.md) | Optional | Exception details of the error |

## Example

```python
try:
    # make the API call
except TooManyRequestsException as e:
    print(e)
except APIException as e:
    print(e)
```

