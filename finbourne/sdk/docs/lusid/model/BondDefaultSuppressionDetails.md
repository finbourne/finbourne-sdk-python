# BondDefaultSuppressionDetails

How much of each component of a bond keeps paying after a default, as a fraction from 0.0 (fully  suppressed) to 1.0 (unaffected). An unset field means 1.0. Omitting the whole section is different: that  suppresses coupons and principal outright and leaves interest accruing.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **accrual_percentage** | **float** | Optional | Fraction of the computed accrued interest returned from the default onwards, between 0.0 and 1.0.  Accrued interest supplied through a results store is returned unchanged. Optional, defaulting to 1.0. |
| **coupon_percentage** | **float** | Optional | Fraction of each coupon from the default onwards that is still paid, between 0.0 and 1.0. Optional,  defaulting to 1.0. |
| **principal_percentage** | **float** | Optional | Fraction of each principal repayment from the default onwards still paid, between 0.0 and 1.0.  Optional, defaulting to 1.0. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BondDefaultSuppressionDetails import BondDefaultSuppressionDetails

instance = BondDefaultSuppressionDetails(
    accrual_percentage=0.0,  # optional — Fraction of the computed accrued interest returned from the default onwards, between 0.0 and 1.0.  Accrued interest supplied through a results store is returned unchanged. Optional, defaulting to 1.0.
    coupon_percentage=0.0,  # optional — Fraction of each coupon from the default onwards that is still paid, between 0.0 and 1.0. Optional,  defaulting to 1.0.
    principal_percentage=0.0  # optional — Fraction of each principal repayment from the default onwards still paid, between 0.0 and 1.0.  Optional, defaulting to 1.0.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

