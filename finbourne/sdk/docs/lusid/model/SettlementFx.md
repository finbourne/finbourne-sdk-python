# SettlementFx

The FX gain or loss on a settlement instruction, with its transaction's realised gain or loss.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **settlement_currency** | **str** | Optional | *No description available.* |
| **settlement_amount** | **float** | Optional | *No description available.* |
| **portfolio_currency_amount** | **float** | Optional | *No description available.* |
| **trade_date_fx_rate** | **float** | Optional | *No description available.* |
| **fx_rate_used** | **float** | Optional | *No description available.* |
| **fx_rate_source** | **str** | Optional | *No description available.* |
| **fx_gain_loss_on_settlement** | **float** | Optional | *No description available.* |
| **total_realised_gain_loss_on_transaction** | **float** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SettlementFx import SettlementFx

instance = SettlementFx(
    settlement_currency="...",  # optional
    settlement_amount=0.0,  # optional
    portfolio_currency_amount=0.0,  # optional
    trade_date_fx_rate=0.0,  # optional
    fx_rate_used=0.0,  # optional
    fx_rate_source="...",  # optional
    fx_gain_loss_on_settlement=0.0,  # optional
    total_realised_gain_loss_on_transaction=0.0  # optional
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

