# LusidPropertyToVendorFieldMapping

The mapping of a LUSID Property from the Vendor Field that would populate it
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **var_property** | [LusidPropertyDefinition](LusidPropertyDefinition.md) | Required | *No description available.* |
| **vendor_field** | **str** | Required | *No description available.* |
| **vendor_package** | **str** | Required | *No description available.* |
| **vendor_namespace** | **str** | Required | *No description available.* |
| **optionality** | **str** | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.LusidPropertyToVendorFieldMapping import LusidPropertyToVendorFieldMapping

instance = LusidPropertyToVendorFieldMapping(
    var_property=LusidPropertyDefinition(...),  # required
    vendor_field="...",  # required
    vendor_package="...",  # required
    vendor_namespace="...",  # required
    optionality="..."  # required
)
```


## Related Models

- [LusidPropertyDefinition](LusidPropertyDefinition.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

