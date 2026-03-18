# FundingLegOptions

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **expected_funding_leg_notional** | **str** | Required | Assumption made on future expected notional of the funding leg. |
| **model_options_type** | **str** | Required | The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, CdsModelOptions |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundingLegOptions import FundingLegOptions

instance = FundingLegOptions(
    expected_funding_leg_notional="...",  # required — Assumption made on future expected notional of the funding leg.
    model_options_type="..."  # required — The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, CdsModelOptions
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

