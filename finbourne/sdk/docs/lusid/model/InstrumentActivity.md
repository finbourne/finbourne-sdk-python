# InstrumentActivity

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **as_at** | **datetime** | Required | The asAt time for which the adjustment is being applied. |
| **scope** | **str** | Required | The Scope of the given entity |
| **lusid_instrument_id** | **str** | Required | The LusidInstrumentId of the given entity |
| **nav_activity_adjustment_type** | **str** | Required | . The available values are: PortfolioTransaction, PortfolioSettlementInstruction, InstrumentActivity, QuoteActivity |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.InstrumentActivity import InstrumentActivity

instance = InstrumentActivity(
    as_at=datetime.now(),  # required — The asAt time for which the adjustment is being applied.
    scope="...",  # required — The Scope of the given entity
    lusid_instrument_id="...",  # required — The LusidInstrumentId of the given entity
    nav_activity_adjustment_type="..."  # required — . The available values are: PortfolioTransaction, PortfolioSettlementInstruction, InstrumentActivity, QuoteActivity
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

