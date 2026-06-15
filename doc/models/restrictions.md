
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

## Example (as JSON)

```json
{
  "startTime": "08:00",
  "endTime": "18:00",
  "startDate": "2021-10-06",
  "endDate": "2021-10-31",
  "minKwh": 0.1,
  "maxKwh": 100,
  "minCurrent": 0,
  "maxCurrent": 500,
  "minPower": 0,
  "maxPower": 100,
  "minDuration": 0,
  "maxDuration": 86400
}
```

