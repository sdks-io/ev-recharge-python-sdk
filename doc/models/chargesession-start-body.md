
# Chargesession Start Body

## Structure

`ChargesessionStartBody`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ev_charge_number` | `str` | Required | Ev charge number<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `50` |
| `evse_id` | `str` | Required | This is the Electric Vehicle EquipmentID<br><br>**Constraints**: *Minimum Length*: `18`, *Maximum Length*: `36` |

## Example

```python
from shellev.models.chargesession_start_body import ChargesessionStartBody

chargesession_start_body = ChargesessionStartBody(
    ev_charge_number='NL-TNM-C00122045-K',
    evse_id='NL*TNM*E02003451*0'
)
```

