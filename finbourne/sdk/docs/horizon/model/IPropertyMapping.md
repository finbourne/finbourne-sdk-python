# IPropertyMapping

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **entity_sub_type** | **str** | Optional | *No description available.* |
| **entity_type** | **str** | Required | *No description available.* |
| **optionality** | **str** | Required | *No description available.* |
| **var_property** | [LusidPropertyDefinition](LusidPropertyDefinition.md) | Required | *No description available.* |
| **transformation_description** | **str** | Optional | *No description available.* |
| **vendor_fields** | [List[VendorField]](VendorField.md) | Required | *No description available.* |
| **versions** | **List[str]** | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.IPropertyMapping import IPropertyMapping

instance = IPropertyMapping(
    entity_sub_type="...",  # optional
    entity_type="...",  # required
    optionality="...",  # required
    var_property=LusidPropertyDefinition(...),  # required
    transformation_description="...",  # optional
    vendor_fields=[],  # required
    versions=  # required
)
```

- [LusidPropertyDefinition](LusidPropertyDefinition.md)
- [VendorField](VendorField.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

