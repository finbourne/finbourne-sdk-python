# CreateCalendarRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **calendar_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **calendar_type** | **str** | Required | *No description available.* |
| **weekend_mask** | [WeekendMask](WeekendMask.md) | Required | *No description available.* |
| **source_provider** | **str** | Required | *No description available.* |
| **properties** | [List[ModelProperty]](ModelProperty.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CreateCalendarRequest import CreateCalendarRequest

instance = CreateCalendarRequest(
    calendar_id=ResourceId(...),  # required
    calendar_type="...",  # required
    weekend_mask=WeekendMask(...),  # required
    source_provider="...",  # required
    properties=[]  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [WeekendMask](WeekendMask.md)
- [ModelProperty](ModelProperty.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

