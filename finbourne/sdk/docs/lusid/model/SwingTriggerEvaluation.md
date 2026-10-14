# SwingTriggerEvaluation

How a Market swing trigger was evaluated at a valuation point.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **fired** | **bool** | Required | Whether the net cashflow was in the trigger&#39;s direction and above its threshold. |
| **threshold** | **float** | Required | The trigger&#39;s threshold. |
| **metric** | **str** | Required | What the threshold measured: NetCashflowAbsolute or NetCashflowPctOfNav. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SwingTriggerEvaluation import SwingTriggerEvaluation

instance = SwingTriggerEvaluation(
    fired=True,  # required — Whether the net cashflow was in the trigger&#39;s direction and above its threshold.
    threshold=0.0,  # required — The trigger&#39;s threshold.
    metric="..."  # required — What the threshold measured: NetCashflowAbsolute or NetCashflowPctOfNav.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

