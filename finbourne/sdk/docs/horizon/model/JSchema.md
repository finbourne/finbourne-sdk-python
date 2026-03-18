# JSchema

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **schema_version** | **str** | Optional | *No description available.* |
| **valid** | **bool** | Optional | *No description available.* |
| **reference** | **str** | Optional | *No description available.* |
| **ref** | [JSchema](JSchema.md) | Optional | *No description available.* |
| **recursive_reference** | **str** | Optional | *No description available.* |
| **recursive_anchor** | **bool** | Optional | *No description available.* |
| **id** | **str** | Optional | *No description available.* |
| **anchor** | **str** | Optional | *No description available.* |
| **type** | [JSchemaType](JSchemaType.md) | Optional | *No description available.* |
| **default** | **object** | Optional | *No description available.* |
| **properties** | [Dict[str, JSchema]](JSchema.md) | Required | *No description available.* *(read-only)* |
| **items** | [List[JSchema]](JSchema.md) | Required | *No description available.* *(read-only)* |
| **items_position_validation** | **bool** | Required | *No description available.* |
| **required** | **List[str]** | Required | *No description available.* *(read-only)* |
| **all_of** | [List[JSchema]](JSchema.md) | Required | *No description available.* *(read-only)* |
| **any_of** | [List[JSchema]](JSchema.md) | Required | *No description available.* *(read-only)* |
| **one_of** | [List[JSchema]](JSchema.md) | Required | *No description available.* *(read-only)* |
| **var_if** | [JSchema](JSchema.md) | Optional | *No description available.* |
| **then** | [JSchema](JSchema.md) | Optional | *No description available.* |
| **var_else** | [JSchema](JSchema.md) | Optional | *No description available.* |
| **var_not** | [JSchema](JSchema.md) | Optional | *No description available.* |
| **contains** | [JSchema](JSchema.md) | Optional | *No description available.* |
| **property_names** | [JSchema](JSchema.md) | Optional | *No description available.* |
| **enum** | **List[object]** | Required | *No description available.* *(read-only)* |
| **const** | **object** | Optional | *No description available.* |
| **unique_items** | **bool** | Required | *No description available.* |
| **minimum_length** | **int** | Optional | *No description available.* |
| **maximum_length** | **int** | Optional | *No description available.* |
| **exclusive_minimum** | **bool** | Required | *No description available.* |
| **exclusive_maximum** | **bool** | Required | *No description available.* |
| **minimum_items** | **int** | Optional | *No description available.* |
| **maximum_items** | **int** | Optional | *No description available.* |
| **minimum_properties** | **int** | Optional | *No description available.* |
| **maximum_properties** | **int** | Optional | *No description available.* |
| **minimum_contains** | **int** | Optional | *No description available.* |
| **maximum_contains** | **int** | Optional | *No description available.* |
| **content_encoding** | **str** | Optional | *No description available.* |
| **content_media_type** | **str** | Optional | *No description available.* |
| **write_only** | **bool** | Optional | *No description available.* |
| **read_only** | **bool** | Optional | *No description available.* |
| **extension_data** | **Dict[str, object]** | Required | *No description available.* *(read-only)* |
| **title** | **str** | Optional | *No description available.* |
| **description** | **str** | Optional | *No description available.* |
| **multiple_of** | **float** | Optional | *No description available.* |
| **pattern** | **str** | Optional | *No description available.* |
| **dependencies** | **Dict[str, object]** | Required | *No description available.* *(read-only)* |
| **dependent_required** | **Dict[str, List[str]]** | Required | *No description available.* *(read-only)* |
| **dependent_schemas** | [Dict[str, JSchema]](JSchema.md) | Required | *No description available.* *(read-only)* |
| **pattern_properties** | [Dict[str, JSchema]](JSchema.md) | Required | *No description available.* *(read-only)* |
| **additional_properties** | [JSchema](JSchema.md) | Optional | *No description available.* |
| **allow_additional_properties** | **bool** | Required | *No description available.* |
| **allow_additional_properties_specified** | **bool** | Required | *No description available.* |
| **unevaluated_properties** | [JSchema](JSchema.md) | Optional | *No description available.* |
| **allow_unevaluated_properties** | **bool** | Optional | *No description available.* |
| **additional_items** | [JSchema](JSchema.md) | Optional | *No description available.* |
| **allow_additional_items** | **bool** | Required | *No description available.* |
| **allow_additional_items_specified** | **bool** | Required | *No description available.* |
| **unevaluated_items** | [JSchema](JSchema.md) | Optional | *No description available.* |
| **allow_unevaluated_items** | **bool** | Optional | *No description available.* |
| **format** | **str** | Optional | *No description available.* |
| **validators** | **List[object]** | Required | *No description available.* *(read-only)* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.JSchema import JSchema

instance = JSchema(
    schema_version="...",  # optional
    valid=True,  # optional
    reference="...",  # optional
    ref=JSchema(...),  # optional
    recursive_reference="...",  # optional
    recursive_anchor=True,  # optional
    id="...",  # optional
    anchor="...",  # optional
    type=JSchemaType(...),  # optional
    default=,  # optional
    properties=JSchema(...),  # required
    items=[],  # required
    items_position_validation=True,  # required
    required=,  # required
    all_of=[],  # required
    any_of=[],  # required
    one_of=[],  # required
    var_if=JSchema(...),  # optional
    then=JSchema(...),  # optional
    var_else=JSchema(...),  # optional
    var_not=JSchema(...),  # optional
    contains=JSchema(...),  # optional
    property_names=JSchema(...),  # optional
    enum=,  # required
    const=,  # optional
    unique_items=True,  # required
    minimum_length=0,  # optional
    maximum_length=0,  # optional
    exclusive_minimum=True,  # required
    exclusive_maximum=True,  # required
    minimum_items=0,  # optional
    maximum_items=0,  # optional
    minimum_properties=0,  # optional
    maximum_properties=0,  # optional
    minimum_contains=0,  # optional
    maximum_contains=0,  # optional
    content_encoding="...",  # optional
    content_media_type="...",  # optional
    write_only=True,  # optional
    read_only=True,  # optional
    extension_data=,  # required
    title="...",  # optional
    description="...",  # optional
    multiple_of=0.0,  # optional
    pattern="...",  # optional
    dependencies=,  # required
    dependent_required=,  # required
    dependent_schemas=JSchema(...),  # required
    pattern_properties=JSchema(...),  # required
    additional_properties=JSchema(...),  # optional
    allow_additional_properties=True,  # required
    allow_additional_properties_specified=True,  # required
    unevaluated_properties=JSchema(...),  # optional
    allow_unevaluated_properties=True,  # optional
    additional_items=JSchema(...),  # optional
    allow_additional_items=True,  # required
    allow_additional_items_specified=True,  # required
    unevaluated_items=JSchema(...),  # optional
    allow_unevaluated_items=True,  # optional
    format="...",  # optional
    validators=  # required
)
```

- [JSchema](JSchema.md)
- [JSchemaType](JSchemaType.md)
- [JSchema](JSchema.md)
- [JSchema](JSchema.md)
- [JSchema](JSchema.md)
- [JSchema](JSchema.md)
- [JSchema](JSchema.md)
- [JSchema](JSchema.md)
- [JSchema](JSchema.md)
- [JSchema](JSchema.md)
- [JSchema](JSchema.md)
- [JSchema](JSchema.md)
- [JSchema](JSchema.md)
- [JSchema](JSchema.md)
- [JSchema](JSchema.md)
- [JSchema](JSchema.md)
- [JSchema](JSchema.md)
- [JSchema](JSchema.md)
- [JSchema](JSchema.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

