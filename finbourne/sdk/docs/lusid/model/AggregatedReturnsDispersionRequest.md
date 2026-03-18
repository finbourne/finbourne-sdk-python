# AggregatedReturnsDispersionRequest

The request used in the AggregatedReturnsDispersionMetric.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **to_effective_at** | **str** | Optional | The end date for when the you want the dispersion to be calculated. |
| **years_count** | **int** | Optional | For how many years to calculate the dispersion. Default to 10. |
| **return_ids** | [List[ResourceId]](ResourceId.md) | Optional | The Scope and code of the returns. |
| **recipe_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **composite_method** | **str** | Optional | The method used to calculate the Portfolio performance: Equal/Asset. |
| **alternative_inception_date** | **str** | Optional | Optional - either a date, or the key for a portfolio property containing a date. If provided, the given date will override the inception date for this request. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AggregatedReturnsDispersionRequest import AggregatedReturnsDispersionRequest

instance = AggregatedReturnsDispersionRequest(
    to_effective_at="...",  # optional — The end date for when the you want the dispersion to be calculated.
    years_count=0,  # optional — For how many years to calculate the dispersion. Default to 10.
    return_ids=[],  # optional — The Scope and code of the returns.
    recipe_id=ResourceId(...),  # optional
    composite_method="...",  # optional — The method used to calculate the Portfolio performance: Equal/Asset.
    alternative_inception_date="..."  # optional — Optional - either a date, or the key for a portfolio property containing a date. If provided, the given date will override the inception date for this request.
)
```

- [ResourceId](ResourceId.md) — used in `return_ids`
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

