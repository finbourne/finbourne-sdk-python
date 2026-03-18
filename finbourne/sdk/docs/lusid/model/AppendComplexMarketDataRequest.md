# AppendComplexMarketDataRequest

The details of the point to be appended to a complex market data item.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **market_data_id** | [ComplexMarketDataId](ComplexMarketDataId.md) | Required | *No description available.* |
| **append_market_data** | [AppendMarketData](AppendMarketData.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AppendComplexMarketDataRequest import AppendComplexMarketDataRequest

instance = AppendComplexMarketDataRequest(
    market_data_id=ComplexMarketDataId(...),  # required
    append_market_data=AppendMarketData(...)  # required
)
```


## Related Models

- [ComplexMarketDataId](ComplexMarketDataId.md)
- [AppendMarketData](AppendMarketData.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

