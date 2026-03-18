# PropertyMapping

Mapping from a set of VendorFields to a LUSID Property
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **var_property** | [LusidPropertyDefinition](LusidPropertyDefinition.md) | Required | *No description available.* |
| **vendor_fields** | [List[VendorField]](VendorField.md) | Required | Fields that will be used to map to this Property Definition |
| **optionality** | **str** | Required | Whether the Property is Mandatory, Suggested or Optional |
| **entity_type** | **str** | Required | The LUSID Entity this is valid for |
| **entity_sub_type** | **str** | Optional | The LUSID Entity sub type this is valid for |
| **transformation_description** | **str** | Optional | The transformation, if required, to map from VendorFields to the LUSID Property |
| **versions** | **List[str]** | Required | The versions of the Vendor integration this mapping is valid for |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.PropertyMapping import PropertyMapping

instance = PropertyMapping(
    var_property=LusidPropertyDefinition(...),  # required
    vendor_fields=[],  # required — Fields that will be used to map to this Property Definition
    optionality="...",  # required — Whether the Property is Mandatory, Suggested or Optional
    entity_type="...",  # required — The LUSID Entity this is valid for
    entity_sub_type="...",  # optional — The LUSID Entity sub type this is valid for
    transformation_description="...",  # optional — The transformation, if required, to map from VendorFields to the LUSID Property
    versions=  # required — The versions of the Vendor integration this mapping is valid for
)
```


## Related Models

- [LusidPropertyDefinition](LusidPropertyDefinition.md)
- [VendorField](VendorField.md) — used in `vendor_fields`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

