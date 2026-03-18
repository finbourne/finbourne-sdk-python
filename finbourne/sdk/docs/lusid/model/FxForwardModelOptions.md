# FxForwardModelOptions

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **forward_rate_observable_type** | **str** | Required | The available values are: ForwardPoints, ForwardRate, RatesCurve, FxForwardCurve, Invalid |
| **discounting_method** | **str** | Required | The available values are: Standard, ConstantTimeValueOfMoney, Invalid |
| **convert_to_report_ccy** | **bool** | Required | Convert all FX flows to the report currency  By setting this all FX forwards will be priced using Forward Curves that have Report Currency as the base. |
| **model_options_type** | **str** | Required | The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, CdsModelOptions |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FxForwardModelOptions import FxForwardModelOptions

instance = FxForwardModelOptions(
    forward_rate_observable_type="...",  # required — The available values are: ForwardPoints, ForwardRate, RatesCurve, FxForwardCurve, Invalid
    discounting_method="...",  # required — The available values are: Standard, ConstantTimeValueOfMoney, Invalid
    convert_to_report_ccy=True,  # required — Convert all FX flows to the report currency  By setting this all FX forwards will be priced using Forward Curves that have Report Currency as the base.
    model_options_type="..."  # required — The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, CdsModelOptions
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

