# LusidField

A field on a LUSID entity
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **field_name** | **str** | Required | The name of the LUSID field. |
| **default_value** | **str** | Optional | The default value for the field. |
| **vendor_packages** | **List[str]** | Required | The vendor package that contributes to this LUSID field. |
| **vendor_namespaces** | **List[str]** | Required | The vendor namespace that contributes to this LUSID field. |
| **vendor_fields** | **List[str]** | Required | The underlying fields on the vendor package that contribute to this LUSID field |
| **transformation_description** | **str** | Optional | A description of how the vendor package&#39;s field(s) get mapped to the LUSID field |
| **entity_type** | **str** | Required | LUSID Entity this refers to (e.g. Instrument) |
| **entity_sub_type** | **str** | Optional | Sub-Entity this field refers to (e.g. Equity) |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.LusidField import LusidField

instance = LusidField(
    field_name="...",  # required — The name of the LUSID field.
    default_value="...",  # optional — The default value for the field.
    vendor_packages=,  # required — The vendor package that contributes to this LUSID field.
    vendor_namespaces=,  # required — The vendor namespace that contributes to this LUSID field.
    vendor_fields=,  # required — The underlying fields on the vendor package that contribute to this LUSID field
    transformation_description="...",  # optional — A description of how the vendor package&#39;s field(s) get mapped to the LUSID field
    entity_type="...",  # required — LUSID Entity this refers to (e.g. Instrument)
    entity_sub_type="..."  # optional — Sub-Entity this field refers to (e.g. Equity)
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

