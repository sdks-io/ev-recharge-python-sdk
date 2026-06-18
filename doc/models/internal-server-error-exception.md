
# Internal Server Error Exception

## Structure

`InternalServerErrorException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Optional | requestId is unique identifier value that is attached to requests and messages that allow reference to a particular transaction or event chain. |
| `status` | `str` | Optional | Status of the request |
| `errors` | [`List[InternalErrorObject]`](../../doc/models/internal-error-object.md) | Optional | Exception details of the error |
| `details` | `List[str]` | Optional | - |

## Example

```python
try:
    # make the API call
except InternalServerErrorException as e:
    print(e)
except APIException as e:
    print(e)
```

