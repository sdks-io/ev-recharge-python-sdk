
# M404 Error Response Error

## Structure

`M404ErrorResponseError`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `str` | Required | Error code that logically best represents the error encountered<br>**Constraints**: *Minimum Length*: `5`, *Maximum Length*: `5` |
| `title` | `str` | Required | Description of the error type<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `100` |
| `detail` | `str` | Required | Details of the error that can help under the cause of the error<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `250` |
| `additional_info` | `Dict[str, str]` | Optional | - |

## Example (as JSON)

```json
{
  "Code": "E0005",
  "Title": "Not Found",
  "Detail": "Invalid Charging token with provided",
  "AdditionalInfo": {
    "key0": "AdditionalInfo2",
    "key1": "AdditionalInfo3"
  }
}
```
