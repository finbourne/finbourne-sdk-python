# TaxFundReconciliationResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **fund_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **period** | [TaxAccountingPeriod](TaxAccountingPeriod.md) | Optional | *No description available.* |
| **company_total** | **float** | Optional | The company-level total of lines A, D and LR. |
| **sum_of_fund_proxies** | **float** | Optional | The sum of the member funds&#39; notional totals. |
| **differences** | [List[TaxReconciliationDifferenceRow]](TaxReconciliationDifferenceRow.md) | Optional | The explained differences between the two sides, by holding. |
| **unexplained** | **float** | Optional | The part of the difference not explained by any category. Nil when the reconciliation is complete. |
| **company_line_d** | **float** | Optional | Line D at company level. |
| **funds_line_d** | **float** | Optional | The sum of line D across the member funds. |
| **company_line_lr** | **float** | Optional | Line LR at company level. |
| **funds_line_lr** | **float** | Optional | The sum of line LR across the member funds. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TaxFundReconciliationResponse import TaxFundReconciliationResponse

instance = TaxFundReconciliationResponse(
    fund_id=ResourceId(...),  # optional
    period=TaxAccountingPeriod(...),  # optional
    company_total=0.0,  # optional — The company-level total of lines A, D and LR.
    sum_of_fund_proxies=0.0,  # optional — The sum of the member funds&#39; notional totals.
    differences=[],  # optional — The explained differences between the two sides, by holding.
    unexplained=0.0,  # optional — The part of the difference not explained by any category. Nil when the reconciliation is complete.
    company_line_d=0.0,  # optional — Line D at company level.
    funds_line_d=0.0,  # optional — The sum of line D across the member funds.
    company_line_lr=0.0,  # optional — Line LR at company level.
    funds_line_lr=0.0  # optional — The sum of line LR across the member funds.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [TaxAccountingPeriod](TaxAccountingPeriod.md)
- [TaxReconciliationDifferenceRow](TaxReconciliationDifferenceRow.md) — used in `differences`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

