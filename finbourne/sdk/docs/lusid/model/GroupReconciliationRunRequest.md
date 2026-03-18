# GroupReconciliationRunRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instance_id** | **str** | Required | Reconciliation run Id. Consists of run type (manual or workflow) and identifier. |
| **dates_to_reconcile** | [GroupReconciliationDates](GroupReconciliationDates.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.GroupReconciliationRunRequest import GroupReconciliationRunRequest

instance = GroupReconciliationRunRequest(
    instance_id="...",  # required — Reconciliation run Id. Consists of run type (manual or workflow) and identifier.
    dates_to_reconcile=GroupReconciliationDates(...)  # optional
)
```

- [GroupReconciliationDates](GroupReconciliationDates.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

