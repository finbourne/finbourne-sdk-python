# CdsModelOptions

Model options for credit default instrument.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **use_factors_for_current_notional** | **bool** | Required | Determines if calculations that use current notional apply use a constituent weight factor from a quote representing a default. |
| **model_options_type** | **str** | Required | Available values: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, CdsModelOptions. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CdsModelOptions import CdsModelOptions

instance = CdsModelOptions(
    use_factors_for_current_notional=True,  # required — Determines if calculations that use current notional apply use a constituent weight factor from a quote representing a default.
    model_options_type="..."  # required — Available values: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, CdsModelOptions.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

