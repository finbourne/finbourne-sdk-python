# FundPartnersTotals

Totals across every register line of the fund, independent of paging. Commitments are totalled per commitment  currency; amounts in different currencies are never added together.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **committed_by_currency** | **Dict[str, float]** | Required | The total committed capital across all partners, per commitment currency, keyed by currency code. Commitments in different currencies are not added together. |
| **partner_count** | **int** | Required | The number of partners (register lines) in the fund. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundPartnersTotals import FundPartnersTotals

instance = FundPartnersTotals(
    committed_by_currency=,  # required — The total committed capital across all partners, per commitment currency, keyed by currency code. Commitments in different currencies are not added together.
    partner_count=0  # required — The number of partners (register lines) in the fund.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

