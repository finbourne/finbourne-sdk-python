# FundPartnersTotals

Totals across every register line of the fund, independent of paging.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **committed** | **float** | Required | The total committed capital across all partners. |
| **partner_count** | **int** | Required | The number of partners (register lines) in the fund. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundPartnersTotals import FundPartnersTotals

instance = FundPartnersTotals(
    committed=0.0,  # required — The total committed capital across all partners.
    partner_count=0  # required — The number of partners (register lines) in the fund.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

