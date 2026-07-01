# ResolveTenorsRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **start_date** | **datetime** | Required | *No description available.* |
| **calendars** | [List[ResourceId]](ResourceId.md) | Required | *No description available.* |
| **spot_days** | **int** | Required | *No description available.* |
| **tenors** | **List[str]** | Required | *No description available.* |
| **business_day_convention** | **str** | Optional | Available values: NoAdjustment, None, Previous, P, Following, F, ModifiedPrevious, MP, ModifiedFollowing, MF, HalfMonthModifiedFollowing, Nearest, Invalid. |
| **eom_rule** | **str** | Optional | *No description available.* |
| **as_at** | **datetime** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ResolveTenorsRequest import ResolveTenorsRequest

instance = ResolveTenorsRequest(
    start_date=datetime.now(),  # required
    calendars=[],  # required
    spot_days=0,  # required
    tenors=,  # required
    business_day_convention="...",  # optional — Available values: NoAdjustment, None, Previous, P, Following, F, ModifiedPrevious, MP, ModifiedFollowing, MF, HalfMonthModifiedFollowing, Nearest, Invalid.
    eom_rule="...",  # optional
    as_at=datetime.now()  # optional
)
```

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

