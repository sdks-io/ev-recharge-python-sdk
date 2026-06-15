
# Location Marker V2

## Data Type

`SingleLocationMarkerV2 | MultiLocationMarkerV2`

## Cases

| Type |
|  --- |
| [`SingleLocationMarkerV2`](../../../doc/models/single-location-marker-v2.md) |
| [`MultiLocationMarkerV2`](../../../doc/models/multi-location-marker-v2.md) |

## SingleLocationMarkerV2

### Initialization Code

#### Example

```python
value = SingleLocationMarkerV2(
    status=SingleLocationMarkerStatusEnum.AVAILABLE,
    evse_count=12,
    location_count=6,
    location_uid='2057411',
    operator_name='TheNewMotion'
)
```

## MultiLocationMarkerV2

### Initialization Code

#### Example

```python
value = MultiLocationMarkerV2(
    location_count=6,
    evse_count=10,
    max_power=42,
    operator_name='TheNewMotion'
)
```

