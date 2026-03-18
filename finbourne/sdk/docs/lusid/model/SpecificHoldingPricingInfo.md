# SpecificHoldingPricingInfo

Allows a user to specify fallbacks/overrides using Holding fields for sources that match a particular DependencySourceFilter.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **dependency_source_filter** | [DependencySourceFilter](DependencySourceFilter.md) | Required | *No description available.* |
| **var_field** | **str** | Required | The Holding field which the fallback/override should use to create a price quote. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SpecificHoldingPricingInfo import SpecificHoldingPricingInfo

instance = SpecificHoldingPricingInfo(
    dependency_source_filter=DependencySourceFilter(...),  # required
    var_field="..."  # required — The Holding field which the fallback/override should use to create a price quote.
)
```


## Related Models

- [DependencySourceFilter](DependencySourceFilter.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

