# UpdateCalendarRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **weekend_mask** | [WeekendMask](WeekendMask.md) | Required | *No description available.* |
| **source_provider** | **str** | Required | *No description available.* |
| **properties** | [List[ModelProperty]](ModelProperty.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpdateCalendarRequest import UpdateCalendarRequest

instance = UpdateCalendarRequest(
    weekend_mask=WeekendMask(...),  # required
    source_provider="...",  # required
    properties=[]  # required
)
```


## Related Models

- [WeekendMask](WeekendMask.md)
- [ModelProperty](ModelProperty.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

