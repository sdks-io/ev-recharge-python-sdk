
# Address

Address of the Shell Recharge Location

## Structure

`Address`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `street_and_number` | `str` | Optional | Street Name and Number of the Shell Recharge Location |
| `postal_code` | `str` | Optional | Postal Code of the Shell Recharge Location |
| `city` | `str` | Optional | City name of the Shell Recharge Location |
| `country` | `str` | Optional | ISO 3166 Alpha-2 Country Code of the Shell Recharge Location |

## Example

```python
from shellev.models.address import Address

address = Address(
    street_and_number='Maarssenbroeksedijk 33',
    postal_code='3542 DM',
    city='Utrecht',
    country='NLD'
)
```

