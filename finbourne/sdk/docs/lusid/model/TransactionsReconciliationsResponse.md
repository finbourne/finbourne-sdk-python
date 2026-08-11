# TransactionsReconciliationsResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **mapping** | [Mapping](Mapping.md) | Optional | *No description available.* |
| **data** | [List[ReconciledTransaction]](ReconciledTransaction.md) | Optional | The result of this reconciliation |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransactionsReconciliationsResponse import TransactionsReconciliationsResponse

instance = TransactionsReconciliationsResponse(
    mapping=Mapping(...),  # optional
    data=[]  # optional — The result of this reconciliation
)
```


## Related Models

- [Mapping](Mapping.md)
- [ReconciledTransaction](ReconciledTransaction.md) — used in `data`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

