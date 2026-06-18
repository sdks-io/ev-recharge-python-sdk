
# Connector V2

An EVSE can have one or many Connectors. Each Connector will normally have a different socket / cable and only one can be used to charge at a time.

## Structure

`ConnectorV2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Optional | Internal identifier used to refer to this Connector |
| `external_id` | `str` | Optional | Identifier of the Evse as given by the Operator, unique for the containing EVSE' |
| `connector_type` | [`ConnectorVOConnectorTypeEnum`](../../doc/models/connector-vo-connector-type-enum.md) | Optional | Type of the connector in the EVSE unit. |
| `electrical_properties` | [`ElectricalPropertiesV2`](../../doc/models/electrical-properties-v2.md) | Optional | Electrical Properties of the Connector |

## Example

```python
from shellev.models.connector_v_2 import ConnectorV2
from shellev.models.connector_vo_connector_type_enum import ConnectorVOConnectorTypeEnum
from shellev.models.electrical_properties_power_type_enum import ElectricalPropertiesPowerTypeEnum
from shellev.models.electrical_properties_v_2 import ElectricalPropertiesV2

connector_v_2 = ConnectorV2(
    uid='2',
    external_id='01000861_1_21',
    connector_type=ConnectorVOConnectorTypeEnum.TYPE2,
    electrical_properties=ElectricalPropertiesV2(
        power_type=ElectricalPropertiesPowerTypeEnum.AC1PHASE,
        voltage=110.62,
        amperage=46.4,
        max_electric_power=232.04
    )
)
```

