# OrderRuleBreach

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **breach_task_id** | **str** | Required | Uniquely identifies this historical order breach workflow task. |
| **compliance_state** | **str** | Required | The compliance state of this order breach. Available values: Pending, Failed, Passed, ManuallyApproved, PartiallyOverridden, Warning. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.OrderRuleBreach import OrderRuleBreach

instance = OrderRuleBreach(
    breach_task_id="...",  # required — Uniquely identifies this historical order breach workflow task.
    compliance_state="..."  # required — The compliance state of this order breach. Available values: Pending, Failed, Passed, ManuallyApproved, PartiallyOverridden, Warning.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

