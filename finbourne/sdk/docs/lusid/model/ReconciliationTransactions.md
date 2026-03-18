# ReconciliationTransactions

Specification for the transactions of a scheduled reconciliation
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **transaction_window** | [DateRange](DateRange.md) | Optional | *No description available.* |
| **mapping_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ReconciliationTransactions import ReconciliationTransactions

instance = ReconciliationTransactions(
    transaction_window=DateRange(...),  # optional
    mapping_id=ResourceId(...)  # optional
)
```


## Related Models

- [DateRange](DateRange.md)
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

