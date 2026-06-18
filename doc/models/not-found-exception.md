
# Not Found Exception

Requested resource path not available it will provides the error in OpenAPI spec mentioned format, if there is any change in base URL then respective platform error message will be populated.

## Structure

`NotFoundException`

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
except NotFoundException as e:
    print(e)
except APIException as e:
    print(e)
```

