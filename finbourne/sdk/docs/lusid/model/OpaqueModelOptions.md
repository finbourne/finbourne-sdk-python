# OpaqueModelOptions

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **data** | **Dict[str, Optional[object]]** | Required | *No description available.* |
| **model_options_type** | **str** | Required | The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, CdsModelOptions |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.OpaqueModelOptions import OpaqueModelOptions

instance = OpaqueModelOptions(
    data=,  # required
    model_options_type="..."  # required — The available values are: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, CdsModelOptions
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

