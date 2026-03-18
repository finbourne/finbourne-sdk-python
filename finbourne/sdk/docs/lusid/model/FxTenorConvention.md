# FxTenorConvention

A wrapper of conventions that should be used when interpreting tenors in the context of FX.  For instance, can be used to control how tenors are interpreted on an FxForwardTenorCurveData instance.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **calendar_code** | **str** | Required | The code of the holiday calendar that should be used when interpreting FX tenors. |
| **spot_days** | **int** | Required | The minimum number of business days that must pass within this calendar when calculating the spot date. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FxTenorConvention import FxTenorConvention

instance = FxTenorConvention(
    calendar_code="...",  # required — The code of the holiday calendar that should be used when interpreting FX tenors.
    spot_days=0  # required — The minimum number of business days that must pass within this calendar when calculating the spot date.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

