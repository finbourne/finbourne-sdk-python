# QueryApplicableInstrumentEventsRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **window_start** | **datetime** | Required | The start date of the window. |
| **window_end** | **datetime** | Required | The end date of the window. |
| **effective_at** | **datetime** | Required | The Effective date that splits query window into two parts: factual period and forecast period |
| **portfolio_entity_ids** | [List[PortfolioEntityId]](PortfolioEntityId.md) | Required | The set of portfolios and portfolio groups to which the instrument events must belong. |
| **forecasting_recipe_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.QueryApplicableInstrumentEventsRequest import QueryApplicableInstrumentEventsRequest

instance = QueryApplicableInstrumentEventsRequest(
    window_start=datetime.now(),  # required — The start date of the window.
    window_end=datetime.now(),  # required — The end date of the window.
    effective_at=datetime.now(),  # required — The Effective date that splits query window into two parts: factual period and forecast period
    portfolio_entity_ids=[],  # required — The set of portfolios and portfolio groups to which the instrument events must belong.
    forecasting_recipe_id=ResourceId(...)  # required
)
```

- [PortfolioEntityId](PortfolioEntityId.md) — used in `portfolio_entity_ids`
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

