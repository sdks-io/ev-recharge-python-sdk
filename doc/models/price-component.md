
# Price Component

## Structure

`PriceComponent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`TypeEnum`](../../doc/models/type-enum.md) | Required | Type of the price component |
| `step_size` | `int` | Required | Step size in seconds for TIME-based components, in kWh for ENERGY-based components, or 1 for FLAT components |
| `price` | `float` | Required | Price per step in the specified currency for this price component |
| `vat` | `float` | Required | VAT percentage applicable to this price component |

## Example (as JSON)

```json
{
  "type": "FLAT",
  "stepSize": 1,
  "price": 0.3,
  "vat": 21.0
}
```

