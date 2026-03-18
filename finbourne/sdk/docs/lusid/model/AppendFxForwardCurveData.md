# AppendFxForwardCurveData

Used to append a new point to an FX curve defined using `FxForwardCurveData`.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **var_date** | **datetime** | Required | Date for which the forward rate applies. |
| **rate** | **float** | Required | Rate provided for the fx forward (price in FgnCcy per unit of DomCcy). |
| **market_data_type** | **str** | Required | The available values are: AppendFxForwardCurveByQuoteReference, AppendFxForwardCurveData, AppendFxForwardPipsCurveData, AppendFxForwardTenorCurveData, AppendFxForwardTenorPipsCurveData |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AppendFxForwardCurveData import AppendFxForwardCurveData

instance = AppendFxForwardCurveData(
    var_date=datetime.now(),  # required — Date for which the forward rate applies.
    rate=0.0,  # required — Rate provided for the fx forward (price in FgnCcy per unit of DomCcy).
    market_data_type="..."  # required — The available values are: AppendFxForwardCurveByQuoteReference, AppendFxForwardCurveData, AppendFxForwardPipsCurveData, AppendFxForwardTenorCurveData, AppendFxForwardTenorPipsCurveData
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

