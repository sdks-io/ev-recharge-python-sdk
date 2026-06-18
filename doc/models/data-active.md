
# Data Active

## Structure

`DataActive`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|str` | Optional | Id of the session |
| `user_id` | `str` | Optional | Id of the user that started the session<br><br>**Constraints**: *Minimum Length*: `36`, *Maximum Length*: `36`, *Pattern*: `^[{]?[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}[}]?$` |
| `ema_id` | `str` | Optional | Id of the evse that the user is charging<br><br>**Constraints**: *Minimum Length*: `12`, *Maximum Length*: `36` |
| `evse_id` | `str` | Optional | Electric Vehicle Supply Equipment Identifier. An EVSEID identifies a Charging Point. |
| `started_at` | `datetime` | Optional | When the session is started |
| `stopped_at` | `datetime` | Optional | When the session is stopped |
| `session_state` | [`ChargeRetrieveState`](../../doc/models/charge-retrieve-state.md) | Optional | - |
| `last_updated` | `str` | Optional | - |

## Example

```python
import dateutil.parser

from shellev.models.data_active import DataActive

data_active = DataActive(
    id='78b5d7a3-bdba-43d7-9851-1c84fcddb782',
    user_id='281482b6-2c9a-4fd1-b3ea-1928edb40ef9',
    ema_id='NL-TNM-C00122045-K',
    evse_id='NL*TNM*E02003451*0',
    started_at=dateutil.parser.parse('2015-08-19T11:20:27Z'),
    stopped_at=dateutil.parser.parse('2015-08-19T11:20:27Z')
)
```

