
# Bad Request Exception

## Structure

`BadRequestException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Optional | requestId is unique identifier value that is attached to requests and messages that allow reference to a particular transaction or event chain. |
| `status` | `str` | Optional | Status of the request |
| `errors` | [`List[BadRequestErrMsg]`](../../doc/models/bad-request-err-msg.md) | Optional | Exception details of the error |

## Example

```python
try:
    # make the API call
except BadRequestException as e:
    print(e)
except APIException as e:
    print(e)
```

