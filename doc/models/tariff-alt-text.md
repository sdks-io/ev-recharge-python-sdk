
# Tariff Alt Text

## Structure

`TariffAltText`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `language` | `str` | Required | ISO language code |
| `text` | `str` | Required | Human readable tariff description |

## Example

```python
from shellev.models.tariff_alt_text import TariffAltText

tariff_alt_text = TariffAltText(
    language='en',
    text='€0.30 per kWh'
)
```

