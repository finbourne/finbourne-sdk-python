# EffectiveDateRelative

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **var_date** | [PointInTimeSpecification](PointInTimeSpecification.md) | Optional | *No description available.* |
| **adjustment** | **int** | Optional | *No description available.* |
| **unit** | [DateUnit](DateUnit.md) | Optional | *No description available.* |
| **relative_to_date_time** | [RelativeToDateTime](RelativeToDateTime.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.access.models.EffectiveDateRelative import EffectiveDateRelative

instance = EffectiveDateRelative(
    var_date=PointInTimeSpecification(...),  # optional
    adjustment=0,  # optional
    unit=DateUnit(...),  # optional
    relative_to_date_time=RelativeToDateTime(...)  # optional
)
```


## Related Models

- [PointInTimeSpecification](PointInTimeSpecification.md)
- [DateUnit](DateUnit.md)
- [RelativeToDateTime](RelativeToDateTime.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

