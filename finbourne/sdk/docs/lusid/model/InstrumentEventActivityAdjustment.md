# InstrumentEventActivityAdjustment

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **nav_activity_adjustment_source** | **str** | Required | The post closed activity source of the given entity, for example Manual. Available values: Undefined, Manual, Auto. |
| **as_at** | **datetime** | Required | The asAt time for which the adjustment is being applied. |
| **corporate_action_source_scope** | **str** | Required | The scope of the corporate action source that the instrument event belongs to. |
| **corporate_action_source_code** | **str** | Required | The code of the corporate action source that the instrument event belongs to. |
| **instrument_event_id** | **str** | Required | The Id of the instrument event being adjusted. |
| **nav_activity_adjustment_type** | **str** | Required | The type of the entity being applied, for example a PortfolioTransaction. Available values: PortfolioTransactionAdjustment, PortfolioSettlementInstructionAdjustment, InstrumentActivityAdjustment, QuoteActivityAdjustment, ComplexMarketDataActivityAdjustment, InstrumentEventActivityAdjustment. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.InstrumentEventActivityAdjustment import InstrumentEventActivityAdjustment

instance = InstrumentEventActivityAdjustment(
    nav_activity_adjustment_source="...",  # required — The post closed activity source of the given entity, for example Manual. Available values: Undefined, Manual, Auto.
    as_at=datetime.now(),  # required — The asAt time for which the adjustment is being applied.
    corporate_action_source_scope="...",  # required — The scope of the corporate action source that the instrument event belongs to.
    corporate_action_source_code="...",  # required — The code of the corporate action source that the instrument event belongs to.
    instrument_event_id="...",  # required — The Id of the instrument event being adjusted.
    nav_activity_adjustment_type="..."  # required — The type of the entity being applied, for example a PortfolioTransaction. Available values: PortfolioTransactionAdjustment, PortfolioSettlementInstructionAdjustment, InstrumentActivityAdjustment, QuoteActivityAdjustment, ComplexMarketDataActivityAdjustment, InstrumentEventActivityAdjustment.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

