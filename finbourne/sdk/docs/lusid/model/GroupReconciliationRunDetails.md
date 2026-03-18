# GroupReconciliationRunDetails

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **completion_status** | **str** | Required | Provides the reconciliation completion status \&quot;Completed\&quot; | \&quot;FailedToComplete\&quot; |
| **error_detail** | **str** | Optional | Error information if the reconciliation failed to complete |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.GroupReconciliationRunDetails import GroupReconciliationRunDetails

instance = GroupReconciliationRunDetails(
    completion_status="...",  # required — Provides the reconciliation completion status \&quot;Completed\&quot; | \&quot;FailedToComplete\&quot;
    error_detail="..."  # optional — Error information if the reconciliation failed to complete
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

