# GroupReconciliationRunResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **reconciliation_summaries** | [List[GroupReconciliationSummary]](GroupReconciliationSummary.md) | Required | One summary record for each of the \&quot;Holding\&quot; | \&quot;Transaction\&quot; | \&quot;Valuation\&quot; reconciliations performed |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.GroupReconciliationRunResponse import GroupReconciliationRunResponse

instance = GroupReconciliationRunResponse(
    reconciliation_summaries=[]  # required — One summary record for each of the \&quot;Holding\&quot; | \&quot;Transaction\&quot; | \&quot;Valuation\&quot; reconciliations performed
)
```


## Related Models

- [GroupReconciliationSummary](GroupReconciliationSummary.md) — used in `reconciliation_summaries`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

