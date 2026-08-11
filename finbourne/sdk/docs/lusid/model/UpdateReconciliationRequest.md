# UpdateReconciliationRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Optional | The name of the scheduled reconciliation |
| **description** | **str** | Optional | A description of the scheduled reconciliation |
| **is_portfolio_group** | **bool** | Optional | Specifies whether reconciliation is between portfolios or portfolio groups |
| **left** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **right** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **transactions** | [ReconciliationTransactions](ReconciliationTransactions.md) | Optional | *No description available.* |
| **positions** | [ReconciliationConfiguration](ReconciliationConfiguration.md) | Optional | *No description available.* |
| **valuations** | [ReconciliationConfiguration](ReconciliationConfiguration.md) | Optional | *No description available.* |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | Reconciliation properties |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpdateReconciliationRequest import UpdateReconciliationRequest

instance = UpdateReconciliationRequest(
    name="...",  # optional — The name of the scheduled reconciliation
    description="...",  # optional — A description of the scheduled reconciliation
    is_portfolio_group=True,  # optional — Specifies whether reconciliation is between portfolios or portfolio groups
    left=ResourceId(...),  # optional
    right=ResourceId(...),  # optional
    transactions=ReconciliationTransactions(...),  # optional
    positions=ReconciliationConfiguration(...),  # optional
    valuations=ReconciliationConfiguration(...),  # optional
    properties=ModelProperty(...)  # optional — Reconciliation properties
)
```

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ReconciliationTransactions](ReconciliationTransactions.md)
- [ReconciliationConfiguration](ReconciliationConfiguration.md)
- [ReconciliationConfiguration](ReconciliationConfiguration.md)
- [ModelProperty](ModelProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

