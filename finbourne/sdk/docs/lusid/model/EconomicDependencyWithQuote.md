# EconomicDependencyWithQuote

Container class pairing economic dependencies and quote data
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **economic_dependency** | [EconomicDependency](EconomicDependency.md) | Required | *No description available.* |
| **metric_value** | [MetricValue](MetricValue.md) | Required | *No description available.* |
| **scale_factor** | **float** | Optional | Scale factor for the quote - this can be null, in which case we default to 1. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.EconomicDependencyWithQuote import EconomicDependencyWithQuote

instance = EconomicDependencyWithQuote(
    economic_dependency=EconomicDependency(...),  # required
    metric_value=MetricValue(...),  # required
    scale_factor=0.0  # optional — Scale factor for the quote - this can be null, in which case we default to 1.
)
```


## Related Models

- [EconomicDependency](EconomicDependency.md)
- [MetricValue](MetricValue.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

