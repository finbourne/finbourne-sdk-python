# RateBreakdownComponent

A tax-characterised payout line within a CashElection on a CashDividendEvent.  Each line carries a rate-type classifier and a per-unit amount in the parent election's currency.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **rate_type** | **str** | Required | Free-string distribution rate-type code (e.g. UNFR, FLFR, PID). |
| **dividend_rate** | **float** | Required | Per-unit amount for this line, in the parent election&#39;s dividend currency. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RateBreakdownComponent import RateBreakdownComponent

instance = RateBreakdownComponent(
    rate_type="...",  # required — Free-string distribution rate-type code (e.g. UNFR, FLFR, PID).
    dividend_rate=0.0  # required — Per-unit amount for this line, in the parent election&#39;s dividend currency.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

