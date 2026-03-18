# GroupReconciliationDefinitionPortfolioEntityIds

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **left** | [List[PortfolioEntityId]](PortfolioEntityId.md) | Required | Portfolio Entity Id of the left side of a reconciliation |
| **right** | [List[PortfolioEntityId]](PortfolioEntityId.md) | Required | Portfolio Entity Id of the right side of a reconciliation |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.GroupReconciliationDefinitionPortfolioEntityIds import GroupReconciliationDefinitionPortfolioEntityIds

instance = GroupReconciliationDefinitionPortfolioEntityIds(
    left=[],  # required — Portfolio Entity Id of the left side of a reconciliation
    right=[]  # required — Portfolio Entity Id of the right side of a reconciliation
)
```


## Related Models

- [PortfolioEntityId](PortfolioEntityId.md) — used in `left`
- [PortfolioEntityId](PortfolioEntityId.md) — used in `right`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

