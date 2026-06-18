
# Restrictions

## Structure

`Restrictions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start_time` | `str` | Optional | Valid from this time of the day (HH:mm) |
| `end_time` | `str` | Optional | Valid until this time of the day (HH:mm) |
| `start_date` | `date` | Optional | - |
| `end_date` | `date` | Optional | - |
| `min_kwh` | `float` | Optional | - |
| `max_kwh` | `float` | Optional | - |
| `min_current` | `float` | Optional | - |
| `max_current` | `float` | Optional | - |
| `min_power` | `float` | Optional | - |
| `max_power` | `float` | Optional | - |
| `min_duration` | `int` | Optional | Minimum session duration in seconds |
| `max_duration` | `int` | Optional | Maximum session duration in seconds |
| `day_of_week` | [`List[DayOfWeekEnum]`](../../doc/models/day-of-week-enum.md) | Optional | - |

## Example

```python
import dateutil.parser

from shellev.models.restrictions import Restrictions

restrictions = Restrictions(
    start_time='08:00',
    end_time='18:00',
    start_date=dateutil.parser.parse('2021-10-06').date(),
    end_date=dateutil.parser.parse('2021-10-31').date(),
    min_kwh=0.1,
    max_kwh=100,
    min_current=0,
    max_current=500,
    min_power=0,
    max_power=100,
    min_duration=0,
    max_duration=86400
)
```

