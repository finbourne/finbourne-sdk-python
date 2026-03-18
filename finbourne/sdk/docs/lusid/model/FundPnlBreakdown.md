# FundPnlBreakdown

The breakdown of PnL for a Fund on a specified date.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **non_class_specific_pnl** | [Dict[str, FundAmount]](FundAmount.md) | Required | Bucket of detail for PnL within the queried period that is not specific to any share class. |
| **aggregated_class_pnl** | [Dict[str, FundAmount]](FundAmount.md) | Required | Bucket of detail for the sum of class PnL across all share classes in a fund and within the queried period. |
| **total_pnl** | [Dict[str, FundAmount]](FundAmount.md) | Required | Bucket of detail for the sum of class PnL and PnL not specific to a class within the queried period. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundPnlBreakdown import FundPnlBreakdown

instance = FundPnlBreakdown(
    non_class_specific_pnl=FundAmount(...),  # required — Bucket of detail for PnL within the queried period that is not specific to any share class.
    aggregated_class_pnl=FundAmount(...),  # required — Bucket of detail for the sum of class PnL across all share classes in a fund and within the queried period.
    total_pnl=FundAmount(...)  # required — Bucket of detail for the sum of class PnL and PnL not specific to a class within the queried period.
)
```


## Related Models

- [FundAmount](FundAmount.md) — used in `non_class_specific_pnl`
- [FundAmount](FundAmount.md) — used in `aggregated_class_pnl`
- [FundAmount](FundAmount.md) — used in `total_pnl`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

