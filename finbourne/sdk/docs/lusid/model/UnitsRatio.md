# UnitsRatio

The number of units you have after the event (output) for a given number of units you have prior to the event (input).
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **input** | **float** | Required | Input amount.  Denominator of the Ratio |
| **output** | **float** | Required | Output amount. Numerator of the Ratio |
| **unit_scale_type** | **str** | Optional | Determines how units are scaled when processing the event.  Supported values: [NEWO, ADEX]. Available values: NEWO, ADEX. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UnitsRatio import UnitsRatio

instance = UnitsRatio(
    input=0.0,  # required — Input amount.  Denominator of the Ratio
    output=0.0,  # required — Output amount. Numerator of the Ratio
    unit_scale_type="..."  # optional — Determines how units are scaled when processing the event.  Supported values: [NEWO, ADEX]. Available values: NEWO, ADEX.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

