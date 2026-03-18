# AppendFxForwardTenorPipsCurveData

Used to append a new point to an FX curve defined using `FxForwardTenorPipsCurveData`.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **tenor** | **str** | Required | Tenor for which the forward rate applies. |
| **pip_rate** | **float** | Required | Rate provided for the fx forward (price in FgnCcy per unit of DomCcy), expressed in pips. |
| **market_data_type** | **str** | Required | The available values are: AppendFxForwardCurveByQuoteReference, AppendFxForwardCurveData, AppendFxForwardPipsCurveData, AppendFxForwardTenorCurveData, AppendFxForwardTenorPipsCurveData |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AppendFxForwardTenorPipsCurveData import AppendFxForwardTenorPipsCurveData

instance = AppendFxForwardTenorPipsCurveData(
    tenor="...",  # required — Tenor for which the forward rate applies.
    pip_rate=0.0,  # required — Rate provided for the fx forward (price in FgnCcy per unit of DomCcy), expressed in pips.
    market_data_type="..."  # required — The available values are: AppendFxForwardCurveByQuoteReference, AppendFxForwardCurveData, AppendFxForwardPipsCurveData, AppendFxForwardTenorCurveData, AppendFxForwardTenorPipsCurveData
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

