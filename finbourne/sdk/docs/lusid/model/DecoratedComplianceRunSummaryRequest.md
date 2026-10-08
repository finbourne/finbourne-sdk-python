# DecoratedComplianceRunSummaryRequest

Specification for retrieving a decorated compliance run summary, optionally restricted to a  set of portfolios and/or portfolio groups.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **run_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **portfolio_entity_ids** | [List[PortfolioEntityId]](PortfolioEntityId.md) | Optional | *No description available.* |
| **property_keys** | **List[str]** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.DecoratedComplianceRunSummaryRequest import DecoratedComplianceRunSummaryRequest

instance = DecoratedComplianceRunSummaryRequest(
    run_id=ResourceId(...),  # required
    portfolio_entity_ids=[],  # optional
    property_keys=  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [PortfolioEntityId](PortfolioEntityId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

