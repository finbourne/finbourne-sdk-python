# CarryTierAmount

A partner's carry split by waterfall tier.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **tier** | **str** | Required | The waterfall tier. |
| **realised** | **float** | Required | The carry realised in the tier. |
| **hypothetical** | **float** | Required | The carry the tier would pay if the fund liquidated at the period end. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CarryTierAmount import CarryTierAmount

instance = CarryTierAmount(
    tier="...",  # required — The waterfall tier.
    realised=0.0,  # required — The carry realised in the tier.
    hypothetical=0.0  # required — The carry the tier would pay if the fund liquidated at the period end.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

