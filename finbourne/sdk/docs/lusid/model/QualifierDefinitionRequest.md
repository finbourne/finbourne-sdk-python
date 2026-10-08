# QualifierDefinitionRequest

A qualifier to declare against a single-value property definition.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **key** | **str** | Required | The key by which the qualifier is addressed, for example &#39;direction&#39;. Addressed in filters, sort orders and derivation formulae as Properties[{propertyKey}].Qualifiers[{qualifierKey}]. Validated under the same rules as a property code. |
| **display_name** | **str** | Required | The display name of the qualifier. |
| **description** | **str** | Optional | Describes the qualifier. Optional; null where not supplied. |
| **data_type_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **is_required** | **bool** | Optional | Whether a value for this qualifier must be supplied when a value of the property is written. Defaults to false, and is returned as a boolean rather than as null. Validated on write only, so setting it true does not retroactively invalidate values stored before the change. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.QualifierDefinitionRequest import QualifierDefinitionRequest

instance = QualifierDefinitionRequest(
    key="...",  # required — The key by which the qualifier is addressed, for example &#39;direction&#39;. Addressed in filters, sort orders and derivation formulae as Properties[{propertyKey}].Qualifiers[{qualifierKey}]. Validated under the same rules as a property code.
    display_name="...",  # required — The display name of the qualifier.
    description="...",  # optional — Describes the qualifier. Optional; null where not supplied.
    data_type_id=ResourceId(...),  # required
    is_required=True  # optional — Whether a value for this qualifier must be supplied when a value of the property is written. Defaults to false, and is returned as a boolean rather than as null. Validated on write only, so setting it true does not retroactively invalidate values stored before the change.
)
```

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

