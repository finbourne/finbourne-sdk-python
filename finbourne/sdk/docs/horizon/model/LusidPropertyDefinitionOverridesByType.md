# LusidPropertyDefinitionOverridesByType

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **display_name_override** | **str** | Optional | *No description available.* |
| **description_override** | **str** | Optional | *No description available.* |
| **entity_type** | **str** | Optional | *No description available.* |
| **entity_sub_type** | **List[str]** | Optional | *No description available.* |
| **vendor_package** | **List[str]** | Optional | *No description available.* |
| **effective_from_override** | **str** | Optional | ISO-8601 instant to use as the property value&#39;s effectiveFrom instead of the date the integration derives, e.g. \&quot;0001-01-01T00:00:00Z\&quot;. Only accepted for integrations reporting supportsEffectiveFromOverride, and only for TimeVariant property definitions. Omit to leave any stored value untouched; send an empty string to clear it. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.LusidPropertyDefinitionOverridesByType import LusidPropertyDefinitionOverridesByType

instance = LusidPropertyDefinitionOverridesByType(
    display_name_override="...",  # optional
    description_override="...",  # optional
    entity_type="...",  # optional
    entity_sub_type=,  # optional
    vendor_package=,  # optional
    effective_from_override="..."  # optional — ISO-8601 instant to use as the property value&#39;s effectiveFrom instead of the date the integration derives, e.g. \&quot;0001-01-01T00:00:00Z\&quot;. Only accepted for integrations reporting supportsEffectiveFromOverride, and only for TimeVariant property definitions. Omit to leave any stored value untouched; send an empty string to clear it.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

