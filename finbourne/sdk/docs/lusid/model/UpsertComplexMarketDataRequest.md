# UpsertComplexMarketDataRequest

The details of the complex market data item to upsert into Lusid.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **market_data_id** | [ComplexMarketDataId](ComplexMarketDataId.md) | Required | *No description available.* |
| **market_data** | [ComplexMarketData](ComplexMarketData.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertComplexMarketDataRequest import UpsertComplexMarketDataRequest

instance = UpsertComplexMarketDataRequest(
    market_data_id=ComplexMarketDataId(...),  # required
    market_data=ComplexMarketData(...)  # required
)
```


## Related Models

- [ComplexMarketDataId](ComplexMarketDataId.md)
- [ComplexMarketData](ComplexMarketData.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

