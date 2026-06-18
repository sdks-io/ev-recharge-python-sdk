
# Unauthorized Exception

## Structure

`UnauthorizedException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Optional | requestId or correlation id of the message |
| `status` | `str` | Optional | Status of the request |
| `errors` | [`List[UnauthorizedErrMsg]`](../../doc/models/unauthorized-err-msg.md) | Optional | Exception details of the error |

## Example

```python
try:
    # make the API call
except UnauthorizedException as e:
    print(e)
except APIException as e:
    print(e)
```

