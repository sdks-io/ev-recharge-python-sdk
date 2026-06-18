
# Tariff

## Structure

`Tariff`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start_fee` | `float` | Optional | Tariff to start a charging session |
| `per_minute` | `float` | Optional | Tariff per minute of charging time |
| `per_k_wh` | `float` | Optional | Tariff per kWh of energy consumed |
| `currency` | `str` | Optional | ISO 4217 Currency Code of the local currency. |
| `updated` | `str` | Optional | ISO8601-compliant UTC datetime of the last update of the Tariff |
| `updated_by` | [`TariffVOUpdatedByEnum`](../../doc/models/tariff-vo-updated-by-enum.md) | Optional | Source of the last update of the tariff details |
| `structure` | `str` | Optional | Tariff structure that this tariff belongs to, typically Default unless specific tariff is defined for provider |

## Example

```python
from shellev.models.tariff import Tariff
from shellev.models.tariff_vo_updated_by_enum import TariffVOUpdatedByEnum

tariff = Tariff(
    start_fee=0,
    per_minute=0.12,
    per_k_wh=0.89,
    currency='EUR',
    updated='2021-07-06T10:44:24Z',
    updated_by=TariffVOUpdatedByEnum.TARIFFSERVICE,
    structure='default'
)
```

