# CashFlowHaircutTermPoint

A point on a cashflow haircut term structure: the haircut rate applying at a given tenor from  the valuation date. Rates are linearly interpolated on time-to-payment between points and  extrapolated flat beyond either end of the term structure.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **tenor** | **str** | Required | The tenor from the valuation date at which the rate applies, e.g. &#39;6M&#39; or &#39;5Y&#39;. |
| **rate** | **float** | Required | The haircut rate applying at the tenor, as a fraction in the range [0, 1]. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CashFlowHaircutTermPoint import CashFlowHaircutTermPoint

instance = CashFlowHaircutTermPoint(
    tenor="...",  # required — The tenor from the valuation date at which the rate applies, e.g. &#39;6M&#39; or &#39;5Y&#39;.
    rate=0.0  # required — The haircut rate applying at the tenor, as a fraction in the range [0, 1].
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

