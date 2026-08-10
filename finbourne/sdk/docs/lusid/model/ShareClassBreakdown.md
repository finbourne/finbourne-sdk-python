# ShareClassBreakdown

The Valuation Point Data for a Share Class on a specified date.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **back_out** | [../model/Dict[str, ShareClassAmount]](ShareClassAmount.md) | Required | Bucket of detail for the Valuation Point where data points have been &#39;backed out&#39;. |
| **dealing** | [../model/ShareClassDealingBreakdown](ShareClassDealingBreakdown.md) | Required | *No description available.* |
| **pn_l** | [../model/ShareClassPnlBreakdown](ShareClassPnlBreakdown.md) | Required | *No description available.* |
| **gav** | [../model/ShareClassAmount](ShareClassAmount.md) | Required | *No description available.* |
| **fees** | [../model/Dict[str, FeeAccrual]](FeeAccrual.md) | Required | Bucket of detail for any &#39;Fees&#39; that have been charged in the selected period. |
| **nav** | [../model/ShareClassAmount](ShareClassAmount.md) | Required | *No description available.* |
| **unitisation** | [../model/UnitisationData](UnitisationData.md) | Optional | *No description available.* |
| **miscellaneous** | [../model/Dict[str, ShareClassAmount]](ShareClassAmount.md) | Optional | Not used directly by the LUSID engines but serves as a holding area for any custom derived data points that may be useful in, for example, fee calculations). |
| **share_class_to_fund_fx_rate** | **float** | Required | The fx rate from the Share Class currency to the fund currency at this valuation point. |
| **capital_ratio** | **float** | Required | The proportion of the fund&#39;s non-class-specific P&amp;L apportioned to this share class. Sums to 1 across the fund&#39;s share classes. |
| **previous_share_class_breakdown** | [../model/PreviousShareClassBreakdown](PreviousShareClassBreakdown.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ShareClassBreakdown import ShareClassBreakdown

instance = ShareClassBreakdown(
    back_out=ShareClassAmount(...),  # required — Bucket of detail for the Valuation Point where data points have been &#39;backed out&#39;.
    dealing=ShareClassDealingBreakdown(...),  # required
    pn_l=ShareClassPnlBreakdown(...),  # required
    gav=ShareClassAmount(...),  # required
    fees=FeeAccrual(...),  # required — Bucket of detail for any &#39;Fees&#39; that have been charged in the selected period.
    nav=ShareClassAmount(...),  # required
    unitisation=UnitisationData(...),  # optional
    miscellaneous=ShareClassAmount(...),  # optional — Not used directly by the LUSID engines but serves as a holding area for any custom derived data points that may be useful in, for example, fee calculations).
    share_class_to_fund_fx_rate=0.0,  # required — The fx rate from the Share Class currency to the fund currency at this valuation point.
    capital_ratio=0.0,  # required — The proportion of the fund&#39;s non-class-specific P&amp;L apportioned to this share class. Sums to 1 across the fund&#39;s share classes.
    previous_share_class_breakdown=PreviousShareClassBreakdown(...)  # required
)
```


## Related Models

- [ShareClassAmount](ShareClassAmount.md) — used in `back_out`
- [ShareClassDealingBreakdown](ShareClassDealingBreakdown.md)
- [ShareClassPnlBreakdown](ShareClassPnlBreakdown.md)
- [ShareClassAmount](ShareClassAmount.md)
- [FeeAccrual](FeeAccrual.md) — used in `fees`
- [ShareClassAmount](ShareClassAmount.md)
- [UnitisationData](UnitisationData.md)
- [ShareClassAmount](ShareClassAmount.md) — used in `miscellaneous`
- [PreviousShareClassBreakdown](PreviousShareClassBreakdown.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

