# SetInstanceOptionalPropertyMappingResponse

Response for SetInstanceOptionalPropertyMapping.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **property_overrides** | [Dict[str, LusidPropertyDefinitionOverridesByType]](LusidPropertyDefinitionOverridesByType.md) | Required | The full, current optional property mapping for the instance, after the write. |
| **warnings** | **List[str]** | Required | Advisory warnings about a write that succeeded regardless, e.g. a future-dated effectiveFromOverride, or another enabled instance of the same integration holding a different effectiveFromOverride for the same property. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.SetInstanceOptionalPropertyMappingResponse import SetInstanceOptionalPropertyMappingResponse

instance = SetInstanceOptionalPropertyMappingResponse(
    property_overrides=LusidPropertyDefinitionOverridesByType(...),  # required — The full, current optional property mapping for the instance, after the write.
    warnings=  # required — Advisory warnings about a write that succeeded regardless, e.g. a future-dated effectiveFromOverride, or another enabled instance of the same integration holding a different effectiveFromOverride for the same property.
)
```


## Related Models

- [LusidPropertyDefinitionOverridesByType](LusidPropertyDefinitionOverridesByType.md) — used in `property_overrides`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

