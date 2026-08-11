# MarketDataOverrides

Class which holds market data overrides to be used in valuation
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **complex_market_data** | [List[EconomicDependencyWithComplexMarketData]](EconomicDependencyWithComplexMarketData.md) | Optional | A list of EconomicDependency paired with quote data satisfying that economic dependency |
| **quotes** | [List[EconomicDependencyWithQuote]](EconomicDependencyWithQuote.md) | Optional | A list of EconomicDependency paired with a ComplexMarketData satisfying that economic dependency |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.MarketDataOverrides import MarketDataOverrides

instance = MarketDataOverrides(
    complex_market_data=[],  # optional — A list of EconomicDependency paired with quote data satisfying that economic dependency
    quotes=[]  # optional — A list of EconomicDependency paired with a ComplexMarketData satisfying that economic dependency
)
```


## Related Models

- [EconomicDependencyWithComplexMarketData](EconomicDependencyWithComplexMarketData.md) — used in `complex_market_data`
- [EconomicDependencyWithQuote](EconomicDependencyWithQuote.md) — used in `quotes`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

