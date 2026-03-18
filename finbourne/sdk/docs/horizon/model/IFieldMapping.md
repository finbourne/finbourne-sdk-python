# IFieldMapping

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **default_value** | **str** | Optional | *No description available.* |
| **entity_sub_type** | **str** | Optional | *No description available.* |
| **entity_type** | **str** | Required | *No description available.* |
| **field_name** | **str** | Required | *No description available.* |
| **transformation_description** | **str** | Optional | *No description available.* |
| **vendor_fields** | [List[VendorField]](VendorField.md) | Required | *No description available.* |
| **versions** | **List[str]** | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.IFieldMapping import IFieldMapping

instance = IFieldMapping(
    default_value="...",  # optional
    entity_sub_type="...",  # optional
    entity_type="...",  # required
    field_name="...",  # required
    transformation_description="...",  # optional
    vendor_fields=[],  # required
    versions=  # required
)
```

- [VendorField](VendorField.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

