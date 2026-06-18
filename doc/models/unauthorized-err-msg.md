
# Unauthorized Err Msg

## Structure

`UnauthorizedErrMsg`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `str` | Optional | Error code |
| `message` | `str` | Optional | Error desctiption in English |
| `description` | `str` | Optional | Technical details of the error message, the example which is given in the sample payload is one of the scenarios. actual response will vary based on the technical nature |
| `details` | `List[str]` | Optional | - |

## Example

```python
from shellev.models.unauthorized_err_msg import UnauthorizedErrMsg

unauthorized_err_msg = UnauthorizedErrMsg(
    code='E0003',
    message='Unauthorized',
    description='Invalid Access Token',
    details=[
        'details1'
    ]
)
```

