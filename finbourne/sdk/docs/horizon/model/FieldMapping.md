# FieldMapping

Mapping from a set of Vendor Fields to a LUSID core entity field
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **field_name** | **str** | Required | The LUSID core entity field |
| **default_value** | **str** | Optional | Default value if needed |
| **vendor_fields** | [List[VendorField]](VendorField.md) | Required | Fields that will be used to map to this field |
| **transformation_description** | **str** | Optional | The transformation, if required, to map from VendorFields to the LUSID Property |
| **entity_type** | **str** | Required | The LUSID Entity this is valid for |
| **entity_sub_type** | **str** | Optional | The LUSID Entity sub type this is valid for |
| **versions** | **List[str]** | Required | The versions of the Vendor integration this mapping is valid for |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.FieldMapping import FieldMapping

instance = FieldMapping(
    field_name="...",  # required — The LUSID core entity field
    default_value="...",  # optional — Default value if needed
    vendor_fields=[],  # required — Fields that will be used to map to this field
    transformation_description="...",  # optional — The transformation, if required, to map from VendorFields to the LUSID Property
    entity_type="...",  # required — The LUSID Entity this is valid for
    entity_sub_type="...",  # optional — The LUSID Entity sub type this is valid for
    versions=  # required — The versions of the Vendor integration this mapping is valid for
)
```

- [VendorField](VendorField.md) — used in `vendor_fields`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

