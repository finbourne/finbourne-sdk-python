# CalculationInfo

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **calculation_method** | **str** | Required | Method of calculating the fees or commission among: BasisPoints, Percentage, Rate, Flat etc. |
| **multiplier** | **str** | Required | Field by which to multiply the numerical amount. Eg: Quantity, Value |
| **calculation_amount** | **float** | Required | Numerical fee amount |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CalculationInfo import CalculationInfo

instance = CalculationInfo(
    calculation_method="...",  # required — Method of calculating the fees or commission among: BasisPoints, Percentage, Rate, Flat etc.
    multiplier="...",  # required — Field by which to multiply the numerical amount. Eg: Quantity, Value
    calculation_amount=0.0  # required — Numerical fee amount
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

