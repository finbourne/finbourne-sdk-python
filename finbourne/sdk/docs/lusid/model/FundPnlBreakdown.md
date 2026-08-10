# FundPnlBreakdown

The breakdown of PnL for a Fund on a specified date.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **non_class_specific_pnl** | [../model/Dict[str, FundAmount]](FundAmount.md) | Required | Bucket of detail for PnL within the queried period that is not specific to any share class. |
| **aggregated_class_pnl** | [../model/Dict[str, FundAmount]](FundAmount.md) | Required | Bucket of detail for the sum of class PnL across all share classes in a fund and within the queried period. |
| **aggregated_group_pnl** | [../model/Dict[str, FundAmount]](FundAmount.md) | Required | Bucket of detail for the sum, across all share classes, of PnL allocated to allocation groups and apportioned to their member share classes, within the queried period. |
| **total_pnl** | [../model/Dict[str, FundAmount]](FundAmount.md) | Required | Bucket of detail for the total PnL within the queried period: the sum of the class-specific, apportioned non-class-specific and allocation-group-apportioned PnL. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundPnlBreakdown import FundPnlBreakdown

instance = FundPnlBreakdown(
    non_class_specific_pnl=FundAmount(...),  # required — Bucket of detail for PnL within the queried period that is not specific to any share class.
    aggregated_class_pnl=FundAmount(...),  # required — Bucket of detail for the sum of class PnL across all share classes in a fund and within the queried period.
    aggregated_group_pnl=FundAmount(...),  # required — Bucket of detail for the sum, across all share classes, of PnL allocated to allocation groups and apportioned to their member share classes, within the queried period.
    total_pnl=FundAmount(...)  # required — Bucket of detail for the total PnL within the queried period: the sum of the class-specific, apportioned non-class-specific and allocation-group-apportioned PnL.
)
```


## Related Models

- [FundAmount](FundAmount.md) — used in `non_class_specific_pnl`
- [FundAmount](FundAmount.md) — used in `aggregated_class_pnl`
- [FundAmount](FundAmount.md) — used in `aggregated_group_pnl`
- [FundAmount](FundAmount.md) — used in `total_pnl`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

