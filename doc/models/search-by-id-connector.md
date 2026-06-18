
# Search by Id Connector

An EVSE can have one or many Connectors. Each Connector will normally have a different socket / cable and only one can be used to charge at a time.

## Structure

`SearchByIdConnector`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Optional | Internal identifier used to refer to this Connector |
| `external_id` | `str` | Optional | Identifier of the Evse as given by the Operator, unique for the containing EVSE' |
| `connector_type` | [`ConnectorVOConnectorTypeEnum`](../../doc/models/connector-vo-connector-type-enum.md) | Optional | Type of the connector in the EVSE unit. |
| `electrical_properties` | [`ElectricalPropertiesV2`](../../doc/models/electrical-properties-v2.md) | Optional | Electrical Properties of the Connector |
| `tariffs` | [`List[TariffV2]`](../../doc/models/tariff-v2.md) | Optional | Tariffs applicable to this Connector |

## Example

```python
import dateutil.parser

from shellev.models.connector_vo_connector_type_enum import ConnectorVOConnectorTypeEnum
from shellev.models.electrical_properties_power_type_enum import ElectricalPropertiesPowerTypeEnum
from shellev.models.electrical_properties_v_2 import ElectricalPropertiesV2
from shellev.models.power_range import PowerRange
from shellev.models.price_component import PriceComponent
from shellev.models.restrictions import Restrictions
from shellev.models.search_by_id_connector import SearchByIdConnector
from shellev.models.tariff_alt_text import TariffAltText
from shellev.models.tariff_element import TariffElement
from shellev.models.tariff_type_enum import TariffTypeEnum
from shellev.models.tariff_v_2 import TariffV2
from shellev.models.type_enum import TypeEnum

search_by_id_connector = SearchByIdConnector(
    uid='2',
    external_id='01000861_1_21',
    connector_type=ConnectorVOConnectorTypeEnum.TYPE2,
    electrical_properties=ElectricalPropertiesV2(
        power_type=ElectricalPropertiesPowerTypeEnum.AC1PHASE,
        voltage=110.62,
        amperage=46.4,
        max_electric_power=232.04
    ),
    tariffs=[
        TariffV2(
            tariff_id='tariffId4',
            tariff_type=TariffTypeEnum.DRIVER,
            power_range=PowerRange(
                min=102,
                max=20
            ),
            internal_id='internalId2',
            operator_id='operatorId8',
            provider_id='providerId2',
            currency='currency8',
            tariff_alt_text=[
                TariffAltText(
                    language='language8',
                    text='text6'
                )
            ],
            min_price=189.42,
            max_price=247.64,
            elements=[
                TariffElement(
                    price_components=[
                        PriceComponent(
                            mtype=TypeEnum.TIME,
                            step_size=124,
                            price=196.82,
                            vat=137.74
                        ),
                        PriceComponent(
                            mtype=TypeEnum.TIME,
                            step_size=124,
                            price=196.82,
                            vat=137.74
                        ),
                        PriceComponent(
                            mtype=TypeEnum.TIME,
                            step_size=124,
                            price=196.82,
                            vat=137.74
                        )
                    ],
                    restrictions=Restrictions(
                        start_time='startTime0',
                        end_time='endTime2',
                        start_date=dateutil.parser.parse('2016-03-13').date(),
                        end_date=dateutil.parser.parse('2016-03-13').date(),
                        min_kwh=247.22
                    )
                )
            ],
            start_date_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            end_date_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            last_updated=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            created_by='createdBy4'
        ),
        TariffV2(
            tariff_id='tariffId4',
            tariff_type=TariffTypeEnum.DRIVER,
            power_range=PowerRange(
                min=102,
                max=20
            ),
            internal_id='internalId2',
            operator_id='operatorId8',
            provider_id='providerId2',
            currency='currency8',
            tariff_alt_text=[
                TariffAltText(
                    language='language8',
                    text='text6'
                )
            ],
            min_price=189.42,
            max_price=247.64,
            elements=[
                TariffElement(
                    price_components=[
                        PriceComponent(
                            mtype=TypeEnum.TIME,
                            step_size=124,
                            price=196.82,
                            vat=137.74
                        ),
                        PriceComponent(
                            mtype=TypeEnum.TIME,
                            step_size=124,
                            price=196.82,
                            vat=137.74
                        ),
                        PriceComponent(
                            mtype=TypeEnum.TIME,
                            step_size=124,
                            price=196.82,
                            vat=137.74
                        )
                    ],
                    restrictions=Restrictions(
                        start_time='startTime0',
                        end_time='endTime2',
                        start_date=dateutil.parser.parse('2016-03-13').date(),
                        end_date=dateutil.parser.parse('2016-03-13').date(),
                        min_kwh=247.22
                    )
                )
            ],
            start_date_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            end_date_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            last_updated=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            created_by='createdBy4'
        ),
        TariffV2(
            tariff_id='tariffId4',
            tariff_type=TariffTypeEnum.DRIVER,
            power_range=PowerRange(
                min=102,
                max=20
            ),
            internal_id='internalId2',
            operator_id='operatorId8',
            provider_id='providerId2',
            currency='currency8',
            tariff_alt_text=[
                TariffAltText(
                    language='language8',
                    text='text6'
                )
            ],
            min_price=189.42,
            max_price=247.64,
            elements=[
                TariffElement(
                    price_components=[
                        PriceComponent(
                            mtype=TypeEnum.TIME,
                            step_size=124,
                            price=196.82,
                            vat=137.74
                        ),
                        PriceComponent(
                            mtype=TypeEnum.TIME,
                            step_size=124,
                            price=196.82,
                            vat=137.74
                        ),
                        PriceComponent(
                            mtype=TypeEnum.TIME,
                            step_size=124,
                            price=196.82,
                            vat=137.74
                        )
                    ],
                    restrictions=Restrictions(
                        start_time='startTime0',
                        end_time='endTime2',
                        start_date=dateutil.parser.parse('2016-03-13').date(),
                        end_date=dateutil.parser.parse('2016-03-13').date(),
                        min_kwh=247.22
                    )
                )
            ],
            start_date_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            end_date_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            last_updated=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            created_by='createdBy4'
        )
    ]
)
```

