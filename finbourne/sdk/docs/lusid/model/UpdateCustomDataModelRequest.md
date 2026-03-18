# UpdateCustomDataModelRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **display_name** | **str** | Required | The name of the Custom Data Model. |
| **description** | **str** | Optional | A description for the Custom Data Model. |
| **parent_data_model** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **conditions** | **str** | Optional | The conditions that the bound entity must meet to be valid. |
| **properties** | [List[CustomDataModelPropertySpecification]](CustomDataModelPropertySpecification.md) | Optional | The properties that are required or allowed on the bound entity. |
| **identifier_types** | [List[CustomDataModelIdentifierTypeSpecification]](CustomDataModelIdentifierTypeSpecification.md) | Optional | The identifier types that are required or allowed on the bound entity. |
| **attribute_aliases** | [List[Alias]](Alias.md) | Optional | The aliases for property keys, identifier types, and fields on the bound entity. |
| **recommended_sort_by** | [List[RecommendedSortBy]](RecommendedSortBy.md) | Optional | The preferred default sorting instructions. |
| **supplemental_property_keys** | **List[str]** | Optional | Additional property keys that should be decorated on the bound entity. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpdateCustomDataModelRequest import UpdateCustomDataModelRequest

instance = UpdateCustomDataModelRequest(
    display_name="...",  # required — The name of the Custom Data Model.
    description="...",  # optional — A description for the Custom Data Model.
    parent_data_model=ResourceId(...),  # optional
    conditions="...",  # optional — The conditions that the bound entity must meet to be valid.
    properties=[],  # optional — The properties that are required or allowed on the bound entity.
    identifier_types=[],  # optional — The identifier types that are required or allowed on the bound entity.
    attribute_aliases=[],  # optional — The aliases for property keys, identifier types, and fields on the bound entity.
    recommended_sort_by=[],  # optional — The preferred default sorting instructions.
    supplemental_property_keys=  # optional — Additional property keys that should be decorated on the bound entity.
)
```

- [ResourceId](ResourceId.md)
- [CustomDataModelPropertySpecification](CustomDataModelPropertySpecification.md) — used in `properties`
- [CustomDataModelIdentifierTypeSpecification](CustomDataModelIdentifierTypeSpecification.md) — used in `identifier_types`
- [Alias](Alias.md) — used in `attribute_aliases`
- [RecommendedSortBy](RecommendedSortBy.md) — used in `recommended_sort_by`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

