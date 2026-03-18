# PropertyInterval

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **value** | [PropertyValue](PropertyValue.md) | Required | *No description available.* |
| **effective_range** | [DateRange](DateRange.md) | Required | *No description available.* |
| **as_at_range** | [DateRange](DateRange.md) | Required | *No description available.* |
| **status** | **str** | Required | Indicates whether the value is part of the prevailing effective date timeline for the requested asAt date, or whether it has been superseded by correctional activity |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PropertyInterval import PropertyInterval

instance = PropertyInterval(
    value=PropertyValue(...),  # required
    effective_range=DateRange(...),  # required
    as_at_range=DateRange(...),  # required
    status="..."  # required — Indicates whether the value is part of the prevailing effective date timeline for the requested asAt date, or whether it has been superseded by correctional activity
)
```


## Related Models

- [PropertyValue](PropertyValue.md)
- [DateRange](DateRange.md)
- [DateRange](DateRange.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

