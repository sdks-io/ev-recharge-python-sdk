
# Tariff Element

## Structure

`TariffElement`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `price_components` | [`List[PriceComponent]`](../../doc/models/price-component.md) | Required | - |
| `restrictions` | [`Restrictions`](../../doc/models/restrictions.md) | Optional | - |

## Example

```python
import dateutil.parser

from shellev.models.price_component import PriceComponent
from shellev.models.restrictions import Restrictions
from shellev.models.tariff_element import TariffElement
from shellev.models.type_enum import TypeEnum

tariff_element = TariffElement(
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
```

