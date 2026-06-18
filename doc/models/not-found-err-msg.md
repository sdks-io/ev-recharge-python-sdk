
# Not Found Err Msg

## Structure

`NotFoundErrMsg`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `str` | Optional | Error code |
| `message` | `str` | Optional | Error desctiption in English |
| `description` | `str` | Optional | Technical details of the error message, the example which is given in the sample payload is one of the scenarios. actual response will vary based on the technical nature |
| `details` | `List[str]` | Optional | - |

## Example

```python
from shellev.models.not_found_err_msg import NotFoundErrMsg

not_found_err_msg = NotFoundErrMsg(
    code='E0038',
    message='Not Found',
    description='Requested API resource not found',
    details=[
        'details1',
        'details2'
    ]
)
```

