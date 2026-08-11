# TransactionReconciliationRequest

Specifies the parameter to be use when performing a Transaction Reconciliation.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **left_portfolio_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **right_portfolio_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **mapping_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **from_transaction_date** | **datetime** | Required | *No description available.* |
| **to_transaction_date** | **datetime** | Required | *No description available.* |
| **as_at** | **datetime** | Optional | *No description available.* |
| **property_keys** | **List[str]** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransactionReconciliationRequest import TransactionReconciliationRequest

instance = TransactionReconciliationRequest(
    left_portfolio_id=ResourceId(...),  # required
    right_portfolio_id=ResourceId(...),  # required
    mapping_id=ResourceId(...),  # optional
    from_transaction_date=datetime.now(),  # required
    to_transaction_date=datetime.now(),  # required
    as_at=datetime.now(),  # optional
    property_keys=  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

