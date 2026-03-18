# PerformanceReturnsMetric

The request used in the AggregatedReturns.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Optional | The type of the metric. Default to Return |
| **window** | **str** | Optional | The given metric for the calculation i.e. 1Y, 1D. |
| **allow_partial** | **bool** | Optional | Bool if the metric is allowed partial results. Default to false. |
| **annualised** | **bool** | Optional | Bool if the metric is annualized. Default to false. |
| **with_fee** | **bool** | Optional | Bool if the metric should consider the fees when is calculated. Default to false. |
| **seed_amount** | **str** | Optional | The given seed amount for the calculation of the indicative amount metrics. |
| **alias** | **str** | Optional | The alias for the metric. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PerformanceReturnsMetric import PerformanceReturnsMetric

instance = PerformanceReturnsMetric(
    type="...",  # optional — The type of the metric. Default to Return
    window="...",  # optional — The given metric for the calculation i.e. 1Y, 1D.
    allow_partial=True,  # optional — Bool if the metric is allowed partial results. Default to false.
    annualised=True,  # optional — Bool if the metric is annualized. Default to false.
    with_fee=True,  # optional — Bool if the metric should consider the fees when is calculated. Default to false.
    seed_amount="...",  # optional — The given seed amount for the calculation of the indicative amount metrics.
    alias="..."  # optional — The alias for the metric.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

