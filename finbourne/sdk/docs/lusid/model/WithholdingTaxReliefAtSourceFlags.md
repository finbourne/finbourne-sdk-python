# WithholdingTaxReliefAtSourceFlags

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **treaty_ras** | **bool** | Required | Whether relief at source applies at the treaty rate. |
| **better_ras** | **bool** | Required | Whether relief at source applies at the better rate. |
| **enhanced_ras** | **bool** | Required | Whether relief at source applies at the enhanced rate. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.WithholdingTaxReliefAtSourceFlags import WithholdingTaxReliefAtSourceFlags

instance = WithholdingTaxReliefAtSourceFlags(
    treaty_ras=True,  # required — Whether relief at source applies at the treaty rate.
    better_ras=True,  # required — Whether relief at source applies at the better rate.
    enhanced_ras=True  # required — Whether relief at source applies at the enhanced rate.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

