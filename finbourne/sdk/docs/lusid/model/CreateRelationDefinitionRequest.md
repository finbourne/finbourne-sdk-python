# CreateRelationDefinitionRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **scope** | **str** | Required | The scope that the relation exists in. |
| **code** | **str** | Required | The code of the relation. Together with the scope this uniquely defines the relation. |
| **source_entity_domain** | **str** | Required | The entity domain of the source entity object must be, allowed values are \&quot;Portfolio\&quot; and \&quot;Person\&quot; |
| **target_entity_domain** | **str** | Required | The entity domain of the target entity object must be, allowed values are \&quot;Portfolio\&quot; and \&quot;Person\&quot; |
| **display_name** | **str** | Required | The display name of the relation. |
| **outward_description** | **str** | Required | The description to relate source entity object and target entity object. |
| **inward_description** | **str** | Required | The description to relate target entity object and source entity object. |
| **life_time** | **str** | Optional | Describes how the relations can change over time, allowed values are \&quot;Perpetual\&quot; and \&quot;TimeVariant\&quot; |
| **constraint_style** | **str** | Optional | Describes the uniqueness and cardinality for relations with a specific source entity object and relations under this definition. Allowed values are \&quot;Property\&quot; and \&quot;Collection\&quot;, defaults to \&quot;Collection\&quot; if not specified. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CreateRelationDefinitionRequest import CreateRelationDefinitionRequest

instance = CreateRelationDefinitionRequest(
    scope="...",  # required — The scope that the relation exists in.
    code="...",  # required — The code of the relation. Together with the scope this uniquely defines the relation.
    source_entity_domain="...",  # required — The entity domain of the source entity object must be, allowed values are \&quot;Portfolio\&quot; and \&quot;Person\&quot;
    target_entity_domain="...",  # required — The entity domain of the target entity object must be, allowed values are \&quot;Portfolio\&quot; and \&quot;Person\&quot;
    display_name="...",  # required — The display name of the relation.
    outward_description="...",  # required — The description to relate source entity object and target entity object.
    inward_description="...",  # required — The description to relate target entity object and source entity object.
    life_time="...",  # optional — Describes how the relations can change over time, allowed values are \&quot;Perpetual\&quot; and \&quot;TimeVariant\&quot;
    constraint_style="..."  # optional — Describes the uniqueness and cardinality for relations with a specific source entity object and relations under this definition. Allowed values are \&quot;Property\&quot; and \&quot;Collection\&quot;, defaults to \&quot;Collection\&quot; if not specified.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

