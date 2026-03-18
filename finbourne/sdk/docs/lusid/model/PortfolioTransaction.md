# PortfolioTransaction

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **as_at** | **datetime** | Required | The asAt time for which the adjustment is being applied. |
| **portfolio_scope** | **str** | Required | The portfolio scope of the given entity |
| **portfolio_code** | **str** | Required | The portfolio code of the given entity |
| **transaction_id** | **str** | Required | The transaction Id of the PortfolioTransaction being adjusted |
| **nav_activity_adjustment_type** | **str** | Required | . The available values are: PortfolioTransaction, PortfolioSettlementInstruction, InstrumentActivity, QuoteActivity |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PortfolioTransaction import PortfolioTransaction

instance = PortfolioTransaction(
    as_at=datetime.now(),  # required — The asAt time for which the adjustment is being applied.
    portfolio_scope="...",  # required — The portfolio scope of the given entity
    portfolio_code="...",  # required — The portfolio code of the given entity
    transaction_id="...",  # required — The transaction Id of the PortfolioTransaction being adjusted
    nav_activity_adjustment_type="..."  # required — . The available values are: PortfolioTransaction, PortfolioSettlementInstruction, InstrumentActivity, QuoteActivity
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

