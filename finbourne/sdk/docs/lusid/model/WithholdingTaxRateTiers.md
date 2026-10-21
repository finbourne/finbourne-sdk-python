# WithholdingTaxRateTiers

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **country_rate** | **float** | Required | The statutory rate of the matched row, before relief. |
| **treaty_rate** | **float** | Optional | The treaty rate of the matched row. Null when the tier does not apply. |
| **better_rate** | **float** | Optional | The better rate of the matched row. Null when the tier does not apply. |
| **enhanced_rate** | **float** | Optional | The enhanced rate of the matched row. Null when the tier does not apply. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.WithholdingTaxRateTiers import WithholdingTaxRateTiers

instance = WithholdingTaxRateTiers(
    country_rate=0.0,  # required — The statutory rate of the matched row, before relief.
    treaty_rate=0.0,  # optional — The treaty rate of the matched row. Null when the tier does not apply.
    better_rate=0.0,  # optional — The better rate of the matched row. Null when the tier does not apply.
    enhanced_rate=0.0  # optional — The enhanced rate of the matched row. Null when the tier does not apply.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

