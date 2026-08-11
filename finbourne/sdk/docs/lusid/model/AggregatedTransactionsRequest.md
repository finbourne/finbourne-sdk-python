# AggregatedTransactionsRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **from_transaction_date** | **datetime** | Required | *No description available.* |
| **to_transaction_date** | **datetime** | Required | *No description available.* |
| **portfolio_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **portfolio_entity_ids** | [List[PortfolioEntityId]](PortfolioEntityId.md) | Optional | The set of portfolio or portfolio group identifiers containing the relevant transactions. |
| **as_at** | **datetime** | Optional | *No description available.* |
| **metrics** | [List[AggregateSpec]](AggregateSpec.md) | Required | *No description available.* |
| **group_by** | **List[str]** | Optional | *No description available.* |
| **filters** | [List[PropertyFilter]](PropertyFilter.md) | Optional | *No description available.* |
| **sort** | [List[OrderBySpec]](OrderBySpec.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AggregatedTransactionsRequest import AggregatedTransactionsRequest

instance = AggregatedTransactionsRequest(
    from_transaction_date=datetime.now(),  # required
    to_transaction_date=datetime.now(),  # required
    portfolio_id=ResourceId(...),  # optional
    portfolio_entity_ids=[],  # optional — The set of portfolio or portfolio group identifiers containing the relevant transactions.
    as_at=datetime.now(),  # optional
    metrics=[],  # required
    group_by=,  # optional
    filters=[],  # optional
    sort=[]  # optional
)
```

- [ResourceId](ResourceId.md)
- [PortfolioEntityId](PortfolioEntityId.md) — used in `portfolio_entity_ids`
- [AggregateSpec](AggregateSpec.md)
- [PropertyFilter](PropertyFilter.md)
- [OrderBySpec](OrderBySpec.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

