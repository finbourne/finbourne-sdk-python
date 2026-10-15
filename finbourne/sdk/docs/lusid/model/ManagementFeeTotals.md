# ManagementFeeTotals

The management fee totals over every partner.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **gross** | **float** | Required | The fee before offsets. |
| **offset** | **float** | Required | The offset applied to the fee. |
| **net** | **float** | Required | The fee after offsets. |
| **carried_forward** | **float** | Required | Offset in excess of the fee, carried forward to the next period. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ManagementFeeTotals import ManagementFeeTotals

instance = ManagementFeeTotals(
    gross=0.0,  # required — The fee before offsets.
    offset=0.0,  # required — The offset applied to the fee.
    net=0.0,  # required — The fee after offsets.
    carried_forward=0.0  # required — Offset in excess of the fee, carried forward to the next period.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

