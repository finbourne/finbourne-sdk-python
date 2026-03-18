# GroupReconciliationInstanceId

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instance_id_type** | **str** | Required | Type of the reconciliation run, manual or automatic (via the workflow). \&quot;Manual\&quot; | \&quot;WorkflowServiceTaskId\&quot; |
| **instance_id_value** | **str** | Required | Reconciliation run identifier: a manually-provided key or taskId. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.GroupReconciliationInstanceId import GroupReconciliationInstanceId

instance = GroupReconciliationInstanceId(
    instance_id_type="...",  # required — Type of the reconciliation run, manual or automatic (via the workflow). \&quot;Manual\&quot; | \&quot;WorkflowServiceTaskId\&quot;
    instance_id_value="..."  # required — Reconciliation run identifier: a manually-provided key or taskId.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

