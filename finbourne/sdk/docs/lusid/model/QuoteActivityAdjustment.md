# QuoteActivityAdjustment

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **nav_activity_adjustment_source** | **str** | Required | The post closed activity source of the given entity, for example Manual. Available values: Undefined, Manual, Auto. |
| **as_at** | **datetime** | Required | The asAt time for which the adjustment is being applied. |
| **effective_at** | **str** | Required | The EffectiveAt time of the quote event that need to be added to the closed period. |
| **entity_unique_id** | **str** | Required | The EntityUniqueId from the quote which needs to be added as a post close activity. |
| **instrument_id** | **str** | Required | The InstrumentId from the quote which needs to be added as a post close activity. |
| **nav_activity_adjustment_type** | **str** | Required | The type of the entity being applied, for example a PortfolioTransaction. Available values: PortfolioTransactionAdjustment, PortfolioSettlementInstructionAdjustment, InstrumentActivityAdjustment, QuoteActivityAdjustment. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.QuoteActivityAdjustment import QuoteActivityAdjustment

instance = QuoteActivityAdjustment(
    nav_activity_adjustment_source="...",  # required — The post closed activity source of the given entity, for example Manual. Available values: Undefined, Manual, Auto.
    as_at=datetime.now(),  # required — The asAt time for which the adjustment is being applied.
    effective_at="...",  # required — The EffectiveAt time of the quote event that need to be added to the closed period.
    entity_unique_id="...",  # required — The EntityUniqueId from the quote which needs to be added as a post close activity.
    instrument_id="...",  # required — The InstrumentId from the quote which needs to be added as a post close activity.
    nav_activity_adjustment_type="..."  # required — The type of the entity being applied, for example a PortfolioTransaction. Available values: PortfolioTransactionAdjustment, PortfolioSettlementInstructionAdjustment, InstrumentActivityAdjustment, QuoteActivityAdjustment.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

