# Reconciliation

Representation of Reconciliation in LUSID Api
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [../model/ReconciliationId](ReconciliationId.md) | Optional | *No description available.* |
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **name** | **str** | Optional | The name of the scheduled reconciliation |
| **description** | **str** | Optional | A description of the scheduled reconciliation |
| **is_portfolio_group** | **bool** | Optional | Specifies whether reconciliation is between portfolios or portfolio groups |
| **left** | [../model/ResourceId](ResourceId.md) | Optional | *No description available.* |
| **right** | [../model/ResourceId](ResourceId.md) | Optional | *No description available.* |
| **transactions** | [../model/ReconciliationTransactions](ReconciliationTransactions.md) | Optional | *No description available.* |
| **positions** | [../model/ReconciliationConfiguration](ReconciliationConfiguration.md) | Optional | *No description available.* |
| **valuations** | [../model/ReconciliationConfiguration](ReconciliationConfiguration.md) | Optional | *No description available.* |
| **properties** | [../model/Dict[str, ModelProperty]](ModelProperty.md) | Optional | Reconciliation properties |
| **version** | [../model/Version](Version.md) | Optional | *No description available.* |
| **links** | [../model/List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.Reconciliation import Reconciliation

instance = Reconciliation(
    id=ReconciliationId(...),  # optional
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    name="...",  # optional — The name of the scheduled reconciliation
    description="...",  # optional — A description of the scheduled reconciliation
    is_portfolio_group=True,  # optional — Specifies whether reconciliation is between portfolios or portfolio groups
    left=ResourceId(...),  # optional
    right=ResourceId(...),  # optional
    transactions=ReconciliationTransactions(...),  # optional
    positions=ReconciliationConfiguration(...),  # optional
    valuations=ReconciliationConfiguration(...),  # optional
    properties=ModelProperty(...),  # optional — Reconciliation properties
    version=Version(...),  # optional
    links=[]  # optional
)
```


## Related Models

- [ReconciliationId](ReconciliationId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ReconciliationTransactions](ReconciliationTransactions.md)
- [ReconciliationConfiguration](ReconciliationConfiguration.md)
- [ReconciliationConfiguration](ReconciliationConfiguration.md)
- [ModelProperty](ModelProperty.md) — used in `properties`
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

