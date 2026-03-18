# RoundingConvention

Certain bonds will follow certain rounding conventions.  For example, Thai government bonds will round accrued interest and cashflow values 2dp, whereas for  French government bonds, the rounding is to 7dp.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **face_value** | **float** | Optional | The face value to round against.  The number to be rounded is scaled to this face value before being rounded, and then re-scaled to the holding amount.  For example if rounding an accrued interest value using a FaceValue of 1,000, but 10,000 units are held,  then the initial calculated value would be divided by 10,000, then multiplied by 1,000 and rounded per the convention.  The result of this would then be divided by 1,000 and multiplied by 10,000 to get the final value. |
| **precision** | **int** | Optional | The precision of the rounding.  The decimal places to which the rounding takes place.  Defaults to 0 if not set. |
| **rounding_target** | **str** | Optional | The target of the rounding convention.  Accepted values are &#39;AccruedInterest&#39;, &#39;Cashflows&#39;, or &#39;All&#39;    Supported string (enumeration) values are: [All, AccruedInterest, Cashflows].  Defaults to \&quot;All\&quot; if not set. |
| **rounding_type** | **str** | Optional | The type of rounding.  e.g. Round Up, Round Down    Supported string (enumeration) values are: [Down, Up, Floor, Ceiling, Nearest].  Defaults to \&quot;Nearest\&quot; if not set. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RoundingConvention import RoundingConvention

instance = RoundingConvention(
    face_value=0.0,  # optional — The face value to round against.  The number to be rounded is scaled to this face value before being rounded, and then re-scaled to the holding amount.  For example if rounding an accrued interest value using a FaceValue of 1,000, but 10,000 units are held,  then the initial calculated value would be divided by 10,000, then multiplied by 1,000 and rounded per the convention.  The result of this would then be divided by 1,000 and multiplied by 10,000 to get the final value.
    precision=0,  # optional — The precision of the rounding.  The decimal places to which the rounding takes place.  Defaults to 0 if not set.
    rounding_target="...",  # optional — The target of the rounding convention.  Accepted values are &#39;AccruedInterest&#39;, &#39;Cashflows&#39;, or &#39;All&#39;    Supported string (enumeration) values are: [All, AccruedInterest, Cashflows].  Defaults to \&quot;All\&quot; if not set.
    rounding_type="..."  # optional — The type of rounding.  e.g. Round Up, Round Down    Supported string (enumeration) values are: [Down, Up, Floor, Ceiling, Nearest].  Defaults to \&quot;Nearest\&quot; if not set.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

