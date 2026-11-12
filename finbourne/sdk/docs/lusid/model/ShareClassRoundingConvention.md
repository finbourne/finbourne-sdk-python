# ShareClassRoundingConvention

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **precision** | **int** | Optional | The precision of the rounding: the number of decimal places, or of significant figures when PrecisionType is SignificantFigures. At most 28, and at least 1 for SignificantFigures. Defaults to 0. |
| **rounding_type** | **str** | Optional | The type of rounding, applied at the last decimal place or significant figure. Defaults to None, which leaves the value unrounded. Available values: None, Down, Up, Nearest. |
| **precision_type** | **str** | Optional | What Precision counts: DecimalPlaces (the default) or SignificantFigures. A SignificantFigures convention is not copied onto an instrument created for the share class. Available values: DecimalPlaces, SignificantFigures. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ShareClassRoundingConvention import ShareClassRoundingConvention

instance = ShareClassRoundingConvention(
    precision=0,  # optional — The precision of the rounding: the number of decimal places, or of significant figures when PrecisionType is SignificantFigures. At most 28, and at least 1 for SignificantFigures. Defaults to 0.
    rounding_type="...",  # optional — The type of rounding, applied at the last decimal place or significant figure. Defaults to None, which leaves the value unrounded. Available values: None, Down, Up, Nearest.
    precision_type="..."  # optional — What Precision counts: DecimalPlaces (the default) or SignificantFigures. A SignificantFigures convention is not copied onto an instrument created for the share class. Available values: DecimalPlaces, SignificantFigures.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

