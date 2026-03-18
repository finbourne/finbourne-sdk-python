# FundValuationPointData

The Valuation Point Data for a Fund on a specified date.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **back_out** | [Dict[str, FundAmount]](FundAmount.md) | Required | Bucket of detail for the Valuation Point where data points have been &#39;backed out&#39;. |
| **dealing** | [Dict[str, FundAmount]](FundAmount.md) | Required | Bucket of detail for any &#39;Dealing&#39; that has occured inside the queried period. |
| **pn_l** | [FundPnlBreakdown](FundPnlBreakdown.md) | Required | *No description available.* |
| **gav** | **float** | Required | The Gross Asset Value of the Fund or Share Class at the Valuation Point. This is effectively a summation of all Trial balance entries linked to accounts of types &#39;Asset&#39; and &#39;Liabilities&#39;. |
| **fees** | [Dict[str, FeeAccrual]](FeeAccrual.md) | Required | Bucket of detail for any &#39;Fees&#39; that have been charged in the selected period. |
| **nav** | **float** | Required | The Net Asset Value of the Fund or Share Class at the Valuation Point. This represents the GAV with any fees applied in the period. |
| **miscellaneous** | [Dict[str, FundAmount]](FundAmount.md) | Optional | Not used directly by the LUSID engines but serves as a holding area for any custom derived data points that may be useful in, for example, fee calculations). |
| **previous_valuation_point_data** | [PreviousFundValuationPointData](PreviousFundValuationPointData.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundValuationPointData import FundValuationPointData

instance = FundValuationPointData(
    back_out=FundAmount(...),  # required — Bucket of detail for the Valuation Point where data points have been &#39;backed out&#39;.
    dealing=FundAmount(...),  # required — Bucket of detail for any &#39;Dealing&#39; that has occured inside the queried period.
    pn_l=FundPnlBreakdown(...),  # required
    gav=0.0,  # required — The Gross Asset Value of the Fund or Share Class at the Valuation Point. This is effectively a summation of all Trial balance entries linked to accounts of types &#39;Asset&#39; and &#39;Liabilities&#39;.
    fees=FeeAccrual(...),  # required — Bucket of detail for any &#39;Fees&#39; that have been charged in the selected period.
    nav=0.0,  # required — The Net Asset Value of the Fund or Share Class at the Valuation Point. This represents the GAV with any fees applied in the period.
    miscellaneous=FundAmount(...),  # optional — Not used directly by the LUSID engines but serves as a holding area for any custom derived data points that may be useful in, for example, fee calculations).
    previous_valuation_point_data=PreviousFundValuationPointData(...)  # optional
)
```


## Related Models

- [FundAmount](FundAmount.md) — used in `back_out`
- [FundAmount](FundAmount.md) — used in `dealing`
- [FundPnlBreakdown](FundPnlBreakdown.md)
- [FeeAccrual](FeeAccrual.md) — used in `fees`
- [FundAmount](FundAmount.md) — used in `miscellaneous`
- [PreviousFundValuationPointData](PreviousFundValuationPointData.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

