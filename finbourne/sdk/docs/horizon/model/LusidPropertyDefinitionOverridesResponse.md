# LusidPropertyDefinitionOverridesResponse

An item that has been updated as a result of setting LusidPropertyDefinitionOverrides.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **action** | **str** | Required | The action performed on this property. \&quot;upsert\&quot; for setting values for new and existing             properties. \&quot;delete\&quot; for existing properties that were removed |
| **write_error** | **str** | Optional |  |
| **write_error_detail** | **str** | Optional |  |
| **display_name_override** | **str** | Optional |  |
| **description_override** | **str** | Optional |  |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.LusidPropertyDefinitionOverridesResponse import LusidPropertyDefinitionOverridesResponse

instance = LusidPropertyDefinitionOverridesResponse(
    action="...",  # required — The action performed on this property. \&quot;upsert\&quot; for setting values for new and existing             properties. \&quot;delete\&quot; for existing properties that were removed
    write_error="...",  # optional — 
    write_error_detail="...",  # optional — 
    display_name_override="...",  # optional — 
    description_override="..."  # optional — 
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

