# EconomicDependencyWithComplexMarketData

Container class pairing economic dependency and complex market data (i.e. discounting curves, etc.)
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **economic_dependency** | [EconomicDependency](EconomicDependency.md) | Required | *No description available.* |
| **complex_market_data** | [ComplexMarketData](ComplexMarketData.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.EconomicDependencyWithComplexMarketData import EconomicDependencyWithComplexMarketData

instance = EconomicDependencyWithComplexMarketData(
    economic_dependency=EconomicDependency(...),  # required
    complex_market_data=ComplexMarketData(...)  # required
)
```


## Related Models

- [EconomicDependency](EconomicDependency.md)
- [ComplexMarketData](ComplexMarketData.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

