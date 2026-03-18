# ShareClassPnlBreakdown

The breakdown of PnL for a Share Class on a specified date.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **apportioned_non_class_specific_pnl** | [Dict[str, ShareClassAmount]](ShareClassAmount.md) | Required | Bucket of detail for PnL within the queried period not explicitly allocated to any share class but has been apportioned to the share class. |
| **class_pnl** | [Dict[str, ShareClassAmount]](ShareClassAmount.md) | Required | Bucket of detail for PnL specific to the share class within the queried period. |
| **total_pnl** | [Dict[str, ShareClassAmount]](ShareClassAmount.md) | Required | Bucket of detail for the sum of class PnL and PnL not specific to a class within the queried period. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ShareClassPnlBreakdown import ShareClassPnlBreakdown

instance = ShareClassPnlBreakdown(
    apportioned_non_class_specific_pnl=ShareClassAmount(...),  # required — Bucket of detail for PnL within the queried period not explicitly allocated to any share class but has been apportioned to the share class.
    class_pnl=ShareClassAmount(...),  # required — Bucket of detail for PnL specific to the share class within the queried period.
    total_pnl=ShareClassAmount(...)  # required — Bucket of detail for the sum of class PnL and PnL not specific to a class within the queried period.
)
```


## Related Models

- [ShareClassAmount](ShareClassAmount.md) — used in `apportioned_non_class_specific_pnl`
- [ShareClassAmount](ShareClassAmount.md) — used in `class_pnl`
- [ShareClassAmount](ShareClassAmount.md) — used in `total_pnl`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

