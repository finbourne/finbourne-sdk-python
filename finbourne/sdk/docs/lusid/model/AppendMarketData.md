# AppendMarketData

Base class for types containing required data to append to complex market data.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **market_data_type** | **str** | Required | The available values are: AppendFxForwardCurveByQuoteReference, AppendFxForwardCurveData, AppendFxForwardPipsCurveData, AppendFxForwardTenorCurveData, AppendFxForwardTenorPipsCurveData |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AppendMarketData import AppendMarketData

instance = AppendMarketData(
    market_data_type="..."  # required — The available values are: AppendFxForwardCurveByQuoteReference, AppendFxForwardCurveData, AppendFxForwardPipsCurveData, AppendFxForwardTenorCurveData, AppendFxForwardTenorPipsCurveData
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

