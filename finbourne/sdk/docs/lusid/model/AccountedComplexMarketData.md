# AccountedComplexMarketData

The Valuation Point complex market data response for a Fund, including the origin of the complex market data relative to the Valuation Point period.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **complex_market_data** | [ComplexMarketData](ComplexMarketData.md) | Optional | *No description available.* |
| **valuation_point_origin** | **str** | Optional | Designates if the complex market data was originally part of the Valuation Point or if it was added as part of a Complex Close action. Available values: None, Original, Added, OriginalAndAdded. |
| **added_origin_valuation_point_code** | **str** | Optional | The Valuation Point code, only for complex market data added as part of a Complex Close action. |
| **added_origin_valuation_point_variant_code** | **str** | Optional | The Valuation Point variant code, only for complex market data added as part of a Complex Close action. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AccountedComplexMarketData import AccountedComplexMarketData

instance = AccountedComplexMarketData(
    complex_market_data=ComplexMarketData(...),  # optional
    valuation_point_origin="...",  # optional — Designates if the complex market data was originally part of the Valuation Point or if it was added as part of a Complex Close action. Available values: None, Original, Added, OriginalAndAdded.
    added_origin_valuation_point_code="...",  # optional — The Valuation Point code, only for complex market data added as part of a Complex Close action.
    added_origin_valuation_point_variant_code="..."  # optional — The Valuation Point variant code, only for complex market data added as part of a Complex Close action.
)
```


## Related Models

- [ComplexMarketData](ComplexMarketData.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

