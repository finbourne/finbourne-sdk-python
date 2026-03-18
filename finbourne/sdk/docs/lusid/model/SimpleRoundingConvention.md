# SimpleRoundingConvention

Certain bonds will follow certain rounding conventions.  For example, Thai government bonds will round accrued interest and cashflow values 2dp, whereas for  French government bonds, the rounding is to 7dp.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **precision** | **int** | Optional | The precision of the rounding. The decimal places or significant figures to which the rounding takes place.  Defaults to 0 if not set. |
| **rounding_type** | **str** | Optional | The type of rounding.  e.g. Round Up, Round Down    Supported string (enumeration) values are: [Down, Up, Nearest].  Defaults to \&quot;None\&quot; if not set. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SimpleRoundingConvention import SimpleRoundingConvention

instance = SimpleRoundingConvention(
    precision=0,  # optional — The precision of the rounding. The decimal places or significant figures to which the rounding takes place.  Defaults to 0 if not set.
    rounding_type="..."  # optional — The type of rounding.  e.g. Round Up, Round Down    Supported string (enumeration) values are: [Down, Up, Nearest].  Defaults to \&quot;None\&quot; if not set.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

