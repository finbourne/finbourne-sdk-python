# ManagementFeeLine

One partner's management fee for the period.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **investor_record_id** | **str** | Required | The investor record the fee belongs to. |
| **basis_amount** | **float** | Required | The capital the fee was charged on. |
| **rate** | **float** | Required | The annual fee rate applied. |
| **day_count_fraction** | **float** | Required | The fraction of a year the period covers, on an ACT/365 basis. |
| **gross** | **float** | Required | The fee before offsets. |
| **offset** | **float** | Required | The offset applied to the fee. |
| **net** | **float** | Required | The fee after offsets. |
| **carried_forward** | **float** | Required | Offset in excess of the fee, carried forward to the next period. |
| **waived** | **bool** | Required | Whether the partner is fee-exempt and the fee was waived. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ManagementFeeLine import ManagementFeeLine

instance = ManagementFeeLine(
    investor_record_id="...",  # required — The investor record the fee belongs to.
    basis_amount=0.0,  # required — The capital the fee was charged on.
    rate=0.0,  # required — The annual fee rate applied.
    day_count_fraction=0.0,  # required — The fraction of a year the period covers, on an ACT/365 basis.
    gross=0.0,  # required — The fee before offsets.
    offset=0.0,  # required — The offset applied to the fee.
    net=0.0,  # required — The fee after offsets.
    carried_forward=0.0,  # required — Offset in excess of the fee, carried forward to the next period.
    waived=True  # required — Whether the partner is fee-exempt and the fee was waived.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

