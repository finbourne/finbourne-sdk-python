# TaxReturnVintage

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **period_id** | **str** | Optional | The label of the period the amount falls into. |
| **start** | **datetime** | Optional | The first day of the period, inclusive. |
| **end** | **datetime** | Optional | The last day of the period, inclusive. |
| **deemed_gains** | **float** | Optional | The deemed gains arising at the end of the period. |
| **deemed_losses** | **float** | Optional | The deemed losses arising at the end of the period. |
| **net_amount** | **float** | Optional | The net deemed amount, gains less losses. |
| **carry_back_reduction** | **float** | Optional | The reduction to the net amount from losses carried back from later periods. |
| **spread_amount** | **float** | Optional | The net amount after carry-back that is spread over seven periods. |
| **outstanding** | **float** | Optional | The amount of the spread that has not yet been brought into charge. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TaxReturnVintage import TaxReturnVintage

instance = TaxReturnVintage(
    period_id="...",  # optional — The label of the period the amount falls into.
    start=datetime.now(),  # optional — The first day of the period, inclusive.
    end=datetime.now(),  # optional — The last day of the period, inclusive.
    deemed_gains=0.0,  # optional — The deemed gains arising at the end of the period.
    deemed_losses=0.0,  # optional — The deemed losses arising at the end of the period.
    net_amount=0.0,  # optional — The net deemed amount, gains less losses.
    carry_back_reduction=0.0,  # optional — The reduction to the net amount from losses carried back from later periods.
    spread_amount=0.0,  # optional — The net amount after carry-back that is spread over seven periods.
    outstanding=0.0  # optional — The amount of the spread that has not yet been brought into charge.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

