
# Electrical Properties

Electrical Properties of the Connector

## Structure

`ElectricalProperties`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `power_type` | [`ElectricalPropertiesPowerTypeEnum`](../../doc/models/electrical-properties-power-type-enum.md) | Optional | - |
| `voltage` | `float` | Optional | Voltage in Volts for this connector |
| `amperage` | `float` | Optional | Electric Current in Amperes for this connector |
| `max_electric_power` | `float` | Optional | Power in Kilowatts for this connector |

## Example (as JSON)

```json
{
  "voltage": 230.0,
  "amperage": 16.0,
  "maxElectricPower": 3.7,
  "powerType": "DC"
}
```

