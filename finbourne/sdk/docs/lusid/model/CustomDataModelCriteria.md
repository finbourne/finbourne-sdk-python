# CustomDataModelCriteria

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **conditions** | **List[str]** | Optional | The conditions that the bound entity must meet to be valid. |
| **properties** | [List[CustomDataModelPropertySpecificationWithDisplayName]](CustomDataModelPropertySpecificationWithDisplayName.md) | Optional | The properties that are required or allowed on the bound entity. |
| **identifier_types** | [List[CustomDataModelIdentifierTypeSpecificationWithDisplayName]](CustomDataModelIdentifierTypeSpecificationWithDisplayName.md) | Optional | The identifier types that are required or allowed on the bound entity. |
| **attribute_aliases** | [List[Alias]](Alias.md) | Optional | The aliases for property keys, identifier types, and fields on the bound entity. |
| **recommended_sort_by** | [List[RecommendedSortBy]](RecommendedSortBy.md) | Optional | The preferred default sorting instructions. |
| **supplemental_property_keys** | **List[str]** | Optional | Additional property keys that should be decorated on the bound entity. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CustomDataModelCriteria import CustomDataModelCriteria

instance = CustomDataModelCriteria(
    conditions=,  # optional — The conditions that the bound entity must meet to be valid.
    properties=[],  # optional — The properties that are required or allowed on the bound entity.
    identifier_types=[],  # optional — The identifier types that are required or allowed on the bound entity.
    attribute_aliases=[],  # optional — The aliases for property keys, identifier types, and fields on the bound entity.
    recommended_sort_by=[],  # optional — The preferred default sorting instructions.
    supplemental_property_keys=  # optional — Additional property keys that should be decorated on the bound entity.
)
```

- [CustomDataModelPropertySpecificationWithDisplayName](CustomDataModelPropertySpecificationWithDisplayName.md) — used in `properties`
- [CustomDataModelIdentifierTypeSpecificationWithDisplayName](CustomDataModelIdentifierTypeSpecificationWithDisplayName.md) — used in `identifier_types`
- [Alias](Alias.md) — used in `attribute_aliases`
- [RecommendedSortBy](RecommendedSortBy.md) — used in `recommended_sort_by`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

