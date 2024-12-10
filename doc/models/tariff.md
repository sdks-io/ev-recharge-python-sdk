
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
| `updated_by` | [`TariffVOUpdatedByEnum`](../../doc/models/tariff-vo-updated-by-enum.md) | Optional | - |
| `structure` | `str` | Optional | Tariff structure that this tariff belongs to, typically Default unless specific tariff is defined for provider |

## Example (as JSON)

```json
{
  "startFee": 0.0,
  "perMinute": 0.12,
  "perKWh": 0.89,
  "currency": "EUR",
  "updated": "07/06/2021 10:44:24",
  "structure": "default"
}
```

