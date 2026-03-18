# ListComplexMarketDataWithMetaDataResponse

Wraps a ComplexMarketData object with information that was retrieved from storage with it.  In particular,  the scope that the data was stored in,  and an object identifying the market data in that scope.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **scope** | **str** | Optional | The scope that the listed ComplexMarketData entity is stored in. |
| **market_data_id** | [ComplexMarketDataId](ComplexMarketDataId.md) | Optional | *No description available.* |
| **market_data** | [ComplexMarketData](ComplexMarketData.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ListComplexMarketDataWithMetaDataResponse import ListComplexMarketDataWithMetaDataResponse

instance = ListComplexMarketDataWithMetaDataResponse(
    scope="...",  # optional — The scope that the listed ComplexMarketData entity is stored in.
    market_data_id=ComplexMarketDataId(...),  # optional
    market_data=ComplexMarketData(...)  # optional
)
```

- [ComplexMarketDataId](ComplexMarketDataId.md)
- [ComplexMarketData](ComplexMarketData.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

