# FixedLegAllOfOverrides

Any overriding data for notionals, spreads or rates that would affect generation of a leg.  This supports the case where an amortisation schedule is given but otherwise generation is allowed as usual.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **amortization** | **List[float]** | Optional | *No description available.* |
| **spreads** | **List[float]** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FixedLegAllOfOverrides import FixedLegAllOfOverrides

instance = FixedLegAllOfOverrides(
    amortization=,  # optional
    spreads=  # optional
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

