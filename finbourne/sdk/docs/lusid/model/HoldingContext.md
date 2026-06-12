# HoldingContext

Holding context node.  Contains settings that control how LUSID handles holdings within portfolios.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **tax_lot_level_holdings** | **bool** | Optional | Whether or not to expand the holdings to return the underlying tax-lots. Defaults to True. |
| **aggregate_cash_commitments** | **bool** | Optional | When true, cash commitment holdings sharing a SubHoldingKey are folded into a single aggregated  row per portfolio, mirroring how cash balances are already aggregated. Defaults to false to  preserve existing behaviour. Ignored when TaxLotLevelHoldings is true — tax-lot granularity  takes precedence. Aggregation is per-portfolio: cross-portfolio rows in portfolio-group / fund  responses stay separate, matching the behaviour of positions and cash balances. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.HoldingContext import HoldingContext

instance = HoldingContext(
    tax_lot_level_holdings=True,  # optional — Whether or not to expand the holdings to return the underlying tax-lots. Defaults to True.
    aggregate_cash_commitments=True  # optional — When true, cash commitment holdings sharing a SubHoldingKey are folded into a single aggregated  row per portfolio, mirroring how cash balances are already aggregated. Defaults to false to  preserve existing behaviour. Ignored when TaxLotLevelHoldings is true — tax-lot granularity  takes precedence. Aggregation is per-portfolio: cross-portfolio rows in portfolio-group / fund  responses stay separate, matching the behaviour of positions and cash balances.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

