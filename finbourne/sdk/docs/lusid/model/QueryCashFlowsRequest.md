# QueryCashFlowsRequest

Query for cashflows from one or more portfolios
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **as_at** | **datetime** | Optional | The time of the system at which to query for cashflows. |
| **window_start** | **datetime** | Required | The start date of the window. |
| **window_end** | **datetime** | Required | The end date of the window. |
| **portfolio_entity_ids** | [List[PortfolioEntityId]](PortfolioEntityId.md) | Required | The set of portfolios and portfolio groups to which the instrument events must belong. |
| **recipe_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **effective_at** | **datetime** | Required | The Effective date used in the valuation of the cashflows. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.QueryCashFlowsRequest import QueryCashFlowsRequest

instance = QueryCashFlowsRequest(
    as_at=datetime.now(),  # optional — The time of the system at which to query for cashflows.
    window_start=datetime.now(),  # required — The start date of the window.
    window_end=datetime.now(),  # required — The end date of the window.
    portfolio_entity_ids=[],  # required — The set of portfolios and portfolio groups to which the instrument events must belong.
    recipe_id=ResourceId(...),  # required
    effective_at=datetime.now()  # required — The Effective date used in the valuation of the cashflows.
)
```

- [PortfolioEntityId](PortfolioEntityId.md) — used in `portfolio_entity_ids`
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

