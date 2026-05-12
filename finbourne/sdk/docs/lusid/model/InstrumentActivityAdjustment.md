# InstrumentActivityAdjustment

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **nav_activity_adjustment_source** | **str** | Required | The post closed activity source of the given entity, for example Manual. Available values: Undefined, Manual, Auto. |
| **as_at** | **datetime** | Required | The asAt time for which the adjustment is being applied. |
| **scope** | **str** | Required | The Scope of the given entity |
| **lusid_instrument_id** | **str** | Required | The LusidInstrumentId of the given entity |
| **nav_activity_adjustment_type** | **str** | Required | The type of the entity being applied, for example a PortfolioTransaction. Available values: PortfolioTransactionAdjustment, PortfolioSettlementInstructionAdjustment, InstrumentActivityAdjustment, QuoteActivityAdjustment. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.InstrumentActivityAdjustment import InstrumentActivityAdjustment

instance = InstrumentActivityAdjustment(
    nav_activity_adjustment_source="...",  # required — The post closed activity source of the given entity, for example Manual. Available values: Undefined, Manual, Auto.
    as_at=datetime.now(),  # required — The asAt time for which the adjustment is being applied.
    scope="...",  # required — The Scope of the given entity
    lusid_instrument_id="...",  # required — The LusidInstrumentId of the given entity
    nav_activity_adjustment_type="..."  # required — The type of the entity being applied, for example a PortfolioTransaction. Available values: PortfolioTransactionAdjustment, PortfolioSettlementInstructionAdjustment, InstrumentActivityAdjustment, QuoteActivityAdjustment.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

