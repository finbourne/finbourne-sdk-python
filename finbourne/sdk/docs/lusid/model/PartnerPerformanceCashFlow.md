# PartnerPerformanceCashFlow

One dated cash flow the net IRR was solved from, signed from the partner's point of view.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **var_date** | **datetime** | Required | The date of the cash flow. |
| **amount** | **float** | Required | The amount of the cash flow, negative for contributions and positive for distributions and the residual value. |
| **kind** | **str** | Required | The kind of cash flow: Contribution, Distribution or ResidualValue. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PartnerPerformanceCashFlow import PartnerPerformanceCashFlow

instance = PartnerPerformanceCashFlow(
    var_date=datetime.now(),  # required — The date of the cash flow.
    amount=0.0,  # required — The amount of the cash flow, negative for contributions and positive for distributions and the residual value.
    kind="..."  # required — The kind of cash flow: Contribution, Distribution or ResidualValue.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

