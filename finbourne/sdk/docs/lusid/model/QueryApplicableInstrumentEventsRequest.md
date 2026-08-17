# QueryApplicableInstrumentEventsRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **window_start** | **datetime** | Required | The start date of the window. |
| **window_end** | **datetime** | Required | The end date of the window. |
| **effective_at** | **datetime** | Optional | The Effective date that splits query window into two parts: factual period and forecast period. Optional - a timeline (with an optional closed period) may be supplied instead to derive the effective date. |
| **portfolio_entity_ids** | [List[PortfolioEntityId]](PortfolioEntityId.md) | Required | The set of portfolios and portfolio groups to which the instrument events must belong. |
| **forecasting_recipe_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **timeline_scope** | **str** | Optional | The scope of the timeline to be used when building the instrument events. |
| **timeline_code** | **str** | Optional | The code of the timeline to be used when building the instrument events. This can optionally include a colon, followed by the Closed Period Id to use at the head of the timeline, for a timeline with unconfirmed periods. |
| **closed_period_id** | **str** | Optional | The id of the closed period, on the given timeline, to be used when building the instrument events. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.QueryApplicableInstrumentEventsRequest import QueryApplicableInstrumentEventsRequest

instance = QueryApplicableInstrumentEventsRequest(
    window_start=datetime.now(),  # required — The start date of the window.
    window_end=datetime.now(),  # required — The end date of the window.
    effective_at=datetime.now(),  # optional — The Effective date that splits query window into two parts: factual period and forecast period. Optional - a timeline (with an optional closed period) may be supplied instead to derive the effective date.
    portfolio_entity_ids=[],  # required — The set of portfolios and portfolio groups to which the instrument events must belong.
    forecasting_recipe_id=ResourceId(...),  # required
    timeline_scope="...",  # optional — The scope of the timeline to be used when building the instrument events.
    timeline_code="...",  # optional — The code of the timeline to be used when building the instrument events. This can optionally include a colon, followed by the Closed Period Id to use at the head of the timeline, for a timeline with unconfirmed periods.
    closed_period_id="..."  # optional — The id of the closed period, on the given timeline, to be used when building the instrument events.
)
```

- [PortfolioEntityId](PortfolioEntityId.md) — used in `portfolio_entity_ids`
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

