
# Opening Hours Object

## Structure

`OpeningHoursObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `week_day` | [`OpeningHoursObjectWeekDayEnum`](../../doc/models/opening-hours-object-week-day-enum.md) | Optional | 3 letter day of the week |
| `start_time` | `str` | Optional | Hour in 24h local time when the location opens. |
| `end_time` | `str` | Optional | Hour in 24h local time when the location closes. |

## Example

```python
from shellev.models.opening_hours_object import OpeningHoursObject
from shellev.models.opening_hours_object_week_day_enum import OpeningHoursObjectWeekDayEnum

opening_hours_object = OpeningHoursObject(
    week_day=OpeningHoursObjectWeekDayEnum.MON,
    start_time='08:00',
    end_time='23:00'
)
```

