# IndexModelOptions

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **portfolio_scaling** | **str** | Required | Available values: Sum, AbsoluteSum, Unity. |
| **lookthrough_portfolio_relationship_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **model_options_type** | **str** | Required | Available values: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, CdsModelOptions. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.IndexModelOptions import IndexModelOptions

instance = IndexModelOptions(
    portfolio_scaling="...",  # required — Available values: Sum, AbsoluteSum, Unity.
    lookthrough_portfolio_relationship_id=ResourceId(...),  # optional
    model_options_type="..."  # required — Available values: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, CdsModelOptions.
)
```

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

