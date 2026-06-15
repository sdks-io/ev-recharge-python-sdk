
# Location Marker

## Data Type

`SingleLocationMarker | MultiLocationMarker`

## Cases

| Type |
|  --- |
| [`SingleLocationMarker`](../../../doc/models/single-location-marker.md) |
| [`MultiLocationMarker`](../../../doc/models/multi-location-marker.md) |

## SingleLocationMarker

### Initialization Code

#### Example

```python
value = SingleLocationMarker(
    marker_type='SingleLocation',
    unique_key='2057411_1',
    status=SingleLocationMarkerStatusEnum.AVAILABLE,
    evse_count=12,
    max_power=42,
    geo_hash='sx',
    location_uid=2057411,
    operator_id='AT-HTB'
)
```

## MultiLocationMarker

### Initialization Code

#### Example

```python
value = MultiLocationMarker(
    marker_type='MultiLocation',
    unique_key='2060319_6',
    location_count=6,
    evse_count=10,
    max_power=42,
    geo_hash='sx'
)
```

