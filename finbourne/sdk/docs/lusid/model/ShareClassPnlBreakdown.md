# ShareClassPnlBreakdown

The breakdown of PnL for a Share Class on a specified date.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **apportioned_non_class_specific_pnl** | [../model/Dict[str, ShareClassAmount]](ShareClassAmount.md) | Required | Bucket of detail for PnL within the queried period not explicitly allocated to any share class but has been apportioned to the share class. |
| **class_pnl** | [../model/Dict[str, ShareClassAmount]](ShareClassAmount.md) | Required | Bucket of detail for PnL specific to the share class within the queried period. |
| **group_apportioned_pnl** | [../model/Dict[str, ShareClassAmount]](ShareClassAmount.md) | Required | Bucket of detail for the share class&#39;s apportioned share of PnL allocated to the allocation groups it belongs to, within the queried period. |
| **total_pnl** | [../model/Dict[str, ShareClassAmount]](ShareClassAmount.md) | Required | Bucket of detail for the total PnL within the queried period: the sum of the class-specific, apportioned non-class-specific and allocation-group-apportioned PnL. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ShareClassPnlBreakdown import ShareClassPnlBreakdown

instance = ShareClassPnlBreakdown(
    apportioned_non_class_specific_pnl=ShareClassAmount(...),  # required — Bucket of detail for PnL within the queried period not explicitly allocated to any share class but has been apportioned to the share class.
    class_pnl=ShareClassAmount(...),  # required — Bucket of detail for PnL specific to the share class within the queried period.
    group_apportioned_pnl=ShareClassAmount(...),  # required — Bucket of detail for the share class&#39;s apportioned share of PnL allocated to the allocation groups it belongs to, within the queried period.
    total_pnl=ShareClassAmount(...)  # required — Bucket of detail for the total PnL within the queried period: the sum of the class-specific, apportioned non-class-specific and allocation-group-apportioned PnL.
)
```


## Related Models

- [ShareClassAmount](ShareClassAmount.md) — used in `apportioned_non_class_specific_pnl`
- [ShareClassAmount](ShareClassAmount.md) — used in `class_pnl`
- [ShareClassAmount](ShareClassAmount.md) — used in `group_apportioned_pnl`
- [ShareClassAmount](ShareClassAmount.md) — used in `total_pnl`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

