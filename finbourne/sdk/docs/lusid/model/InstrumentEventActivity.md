# InstrumentEventActivity

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **as_at** | **datetime** | Required | The asAt time for which the adjustment is being applied. |
| **corporate_action_source_scope** | **str** | Required | The scope of the corporate action source that the instrument event belongs to. |
| **corporate_action_source_code** | **str** | Required | The code of the corporate action source that the instrument event belongs to. |
| **instrument_event_id** | **str** | Required | The Id of the instrument event being adjusted. |
| **nav_activity_adjustment_type** | **str** | Required | The type of the entity being applied, for example a PortfolioTransaction. Available values: PortfolioTransaction, PortfolioSettlementInstruction, InstrumentActivity, QuoteActivity, ComplexMarketDataActivity, InstrumentEventActivity. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.InstrumentEventActivity import InstrumentEventActivity

instance = InstrumentEventActivity(
    as_at=datetime.now(),  # required — The asAt time for which the adjustment is being applied.
    corporate_action_source_scope="...",  # required — The scope of the corporate action source that the instrument event belongs to.
    corporate_action_source_code="...",  # required — The code of the corporate action source that the instrument event belongs to.
    instrument_event_id="...",  # required — The Id of the instrument event being adjusted.
    nav_activity_adjustment_type="..."  # required — The type of the entity being applied, for example a PortfolioTransaction. Available values: PortfolioTransaction, PortfolioSettlementInstruction, InstrumentActivity, QuoteActivity, ComplexMarketDataActivity, InstrumentEventActivity.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

