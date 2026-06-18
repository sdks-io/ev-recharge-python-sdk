
# Tariff V2

Tariff metadata aligned with TariffV2 GraphQL schema

## Structure

`TariffV2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tariff_id` | `str` | Required | Unique identifier for the tariff |
| `tariff_type` | [`TariffTypeEnum`](../../doc/models/tariff-type-enum.md) | Required | Tariff type classification |
| `power_range` | [`PowerRange`](../../doc/models/power-range.md) | Required | - |
| `internal_id` | `str` | Required | Internal identifier used by the platform |
| `operator_id` | `str` | Required | Unique identifier of the operator |
| `provider_id` | `str` | Required | Unique identifier of the provider |
| `currency` | `str` | Required | ISO 4217 Currency Code |
| `tariff_alt_text` | [`List[TariffAltText]`](../../doc/models/tariff-alt-text.md) | Required | - |
| `min_price` | `float` | Required | - |
| `max_price` | `float` | Required | - |
| `elements` | [`List[TariffElement]`](../../doc/models/tariff-element.md) | Required | - |
| `start_date_time` | `datetime` | Required | - |
| `end_date_time` | `datetime` | Required | - |
| `last_updated` | `datetime` | Required | - |
| `created_by` | `str` | Required | Identifier of the actor who created the tariff |

## Example

```python
import dateutil.parser

from shellev.models.power_range import PowerRange
from shellev.models.price_component import PriceComponent
from shellev.models.restrictions import Restrictions
from shellev.models.tariff_alt_text import TariffAltText
from shellev.models.tariff_element import TariffElement
from shellev.models.tariff_type_enum import TariffTypeEnum
from shellev.models.tariff_v_2 import TariffV2
from shellev.models.type_enum import TypeEnum

tariff_v_2 = TariffV2(
    tariff_id='123e4567-e89b-12d3-a456-426614174000',
    tariff_type=TariffTypeEnum.REIMBURSEMENT,
    power_range=PowerRange(
        min=0,
        max=100
    ),
    internal_id='123e4567-e89b-12d3-a456-426614174000',
    operator_id='AT-HTB',
    provider_id='Shell_RP_2',
    currency='EUR',
    tariff_alt_text=[
        TariffAltText(
            language='en',
            text='€0.30 per kWh'
        )
    ],
    min_price=0.3,
    max_price=999,
    elements=[
        TariffElement(
            price_components=[
                PriceComponent(
                    mtype=TypeEnum.FLAT,
                    step_size=1,
                    price=0.3,
                    vat=21
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
    start_date_time=dateutil.parser.parse('2021-10-06T10:44:24Z'),
    end_date_time=dateutil.parser.parse('2021-10-06T10:44:24Z'),
    last_updated=dateutil.parser.parse('2021-10-06T10:44:24Z'),
    created_by='STAGE_API'
)
```

