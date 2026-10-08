# UpdatePropertyDefinitionRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **display_name** | **str** | Required | The display name of the property. |
| **property_description** | **str** | Optional | Describes the property |
| **custom_entity_types** | **List[str]** | Optional | The custom entity types that properties relating to this property definition can be applied to. |
| **value_format** | **str** | Optional | The format in which values for this property definition should be represented. Available values: Text, Html. |
| **qualifier_definitions** | [List[QualifierDefinitionRequest]](QualifierDefinitionRequest.md) | Optional | The qualifiers declared against this property definition. Omit this field, or supply it as null, to leave the declared qualifiers unchanged. Otherwise the supplied array replaces the stored array in full, so a qualifier omitted from it is no longer declared and can no longer be set, and an empty array clears every declaration. Stored qualifier values are retained in every case and become readable again if the same keys are re-declared with the same data types. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpdatePropertyDefinitionRequest import UpdatePropertyDefinitionRequest

instance = UpdatePropertyDefinitionRequest(
    display_name="...",  # required — The display name of the property.
    property_description="...",  # optional — Describes the property
    custom_entity_types=,  # optional — The custom entity types that properties relating to this property definition can be applied to.
    value_format="...",  # optional — The format in which values for this property definition should be represented. Available values: Text, Html.
    qualifier_definitions=[]  # optional — The qualifiers declared against this property definition. Omit this field, or supply it as null, to leave the declared qualifiers unchanged. Otherwise the supplied array replaces the stored array in full, so a qualifier omitted from it is no longer declared and can no longer be set, and an empty array clears every declaration. Stored qualifier values are retained in every case and become readable again if the same keys are re-declared with the same data types.
)
```

- [QualifierDefinitionRequest](QualifierDefinitionRequest.md) — used in `qualifier_definitions`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

