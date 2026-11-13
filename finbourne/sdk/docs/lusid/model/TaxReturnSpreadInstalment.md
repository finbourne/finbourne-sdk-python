# TaxReturnSpreadInstalment

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **source_period_id** | **str** | Optional | The label of the period whose deemed disposal is being spread. |
| **period_id** | **str** | Optional | The label of the period the amount falls into. |
| **fraction** | **float** | Optional | The fraction of the source period&#39;s spread amount that falls into the period. |
| **amount** | **float** | Optional | The amount, in pounds. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TaxReturnSpreadInstalment import TaxReturnSpreadInstalment

instance = TaxReturnSpreadInstalment(
    source_period_id="...",  # optional — The label of the period whose deemed disposal is being spread.
    period_id="...",  # optional — The label of the period the amount falls into.
    fraction=0.0,  # optional — The fraction of the source period&#39;s spread amount that falls into the period.
    amount=0.0  # optional — The amount, in pounds.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

