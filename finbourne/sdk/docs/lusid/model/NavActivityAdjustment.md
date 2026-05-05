# NavActivityAdjustment

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **nav_activity_adjustment_type** | **str** | Required | The type of the entity being applied, for example a PortfolioTransaction. Available values: PortfolioTransaction, PortfolioSettlementInstruction, InstrumentActivity, QuoteActivity. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.NavActivityAdjustment import NavActivityAdjustment

instance = NavActivityAdjustment(
    nav_activity_adjustment_type="..."  # required — The type of the entity being applied, for example a PortfolioTransaction. Available values: PortfolioTransaction, PortfolioSettlementInstruction, InstrumentActivity, QuoteActivity.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

