
# Electrical Properties V2

Electrical Properties of the Connector

## Structure

`ElectricalPropertiesV2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `power_type` | [`ElectricalPropertiesPowerTypeEnum`](../../doc/models/electrical-properties-power-type-enum.md) | Optional | Power Type used in this connector. |
| `voltage` | `float` | Optional | Voltage in Volts for this connector |
| `amperage` | `float` | Optional | Electric Current in Amperes for this connector |
| `max_electric_power` | `float` | Optional | Power in Kilowatts for this connector |

## Example

```python
from shellev.models.electrical_properties_power_type_enum import ElectricalPropertiesPowerTypeEnum
from shellev.models.electrical_properties_v_2 import ElectricalPropertiesV2

electrical_properties_v_2 = ElectricalPropertiesV2(
    power_type=ElectricalPropertiesPowerTypeEnum.AC1PHASE,
    voltage=230,
    amperage=16,
    max_electric_power=3.7
)
```

