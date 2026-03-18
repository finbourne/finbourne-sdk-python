# CurveOptions

Options for configuring how ComplexMarketData representing a 'curve' is interpreted.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **day_count_convention** | **str** | Optional | Day count convention of the curve. Defaults to \&quot;Act360\&quot;. |
| **front_extrapolation_type** | **str** | Optional | What type of extrapolation is used to build the curve  Imagine that the curve is facing the observer(you), then the \&quot;front\&quot; direction is the closest point on the curve onward.    example: 0D tenor to past  Defaults to \&quot;Flat\&quot;. Supported string (enumeration) values are: [None, Flat, Linear]. |
| **back_extrapolation_type** | **str** | Optional | What type of extrapolation is used to build the curve.    Imagine that the curve is facing the observer(you), then the \&quot;back\&quot; direction is the furthest point on the curve onward.  example: 30Y tenor to infinity    Defaults to \&quot;Flat\&quot;. Supported string (enumeration) values are: [None, Flat, Linear]. |
| **market_data_options_type** | **str** | Required | The available values are: CurveOptions |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CurveOptions import CurveOptions

instance = CurveOptions(
    day_count_convention="...",  # optional — Day count convention of the curve. Defaults to \&quot;Act360\&quot;.
    front_extrapolation_type="...",  # optional — What type of extrapolation is used to build the curve  Imagine that the curve is facing the observer(you), then the \&quot;front\&quot; direction is the closest point on the curve onward.    example: 0D tenor to past  Defaults to \&quot;Flat\&quot;. Supported string (enumeration) values are: [None, Flat, Linear].
    back_extrapolation_type="...",  # optional — What type of extrapolation is used to build the curve.    Imagine that the curve is facing the observer(you), then the \&quot;back\&quot; direction is the furthest point on the curve onward.  example: 30Y tenor to infinity    Defaults to \&quot;Flat\&quot;. Supported string (enumeration) values are: [None, Flat, Linear].
    market_data_options_type="..."  # required — The available values are: CurveOptions
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

