# OrderRuleBreach

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **breach_task_id** | **str** | Required | Uniquely identifies this historical order breach workflow task. |
| **compliance_state** | **str** | Required | The compliance state of this order breach. Possible values are &#39;Pending&#39;, &#39;Failed&#39;, &#39;Manually approved&#39;, &#39;Passed&#39; and &#39;Warning&#39;. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.OrderRuleBreach import OrderRuleBreach

instance = OrderRuleBreach(
    breach_task_id="...",  # required — Uniquely identifies this historical order breach workflow task.
    compliance_state="..."  # required — The compliance state of this order breach. Possible values are &#39;Pending&#39;, &#39;Failed&#39;, &#39;Manually approved&#39;, &#39;Passed&#39; and &#39;Warning&#39;.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

