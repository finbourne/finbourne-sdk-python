# CreateRelationshipDefinitionRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **scope** | **str** | Required | The scope that the relationship definition exists in. |
| **code** | **str** | Required | The code of the relationship definition. Together with the scope this uniquely defines the relationship definition. |
| **source_entity_type** | **str** | Required | The entity type of the source entity object. Allowed values are &#39;Portfolio&#39;, &#39;PortfolioGroup&#39;, &#39;Person&#39;, &#39;LegalEntity&#39;, &#39;Instrument&#39; or a custom entity type prefixed with &#39;~&#39;. |
| **target_entity_type** | **str** | Required | The entity type of the target entity object. Allowed values are &#39;Portfolio&#39;, &#39;PortfolioGroup&#39;, &#39;Person&#39;, &#39;LegalEntity&#39;, &#39;Instrument&#39; or a custom entity type prefixed with &#39;~&#39;. |
| **display_name** | **str** | Required | The display name of the relationship definition. |
| **outward_description** | **str** | Required | The description to relate source entity object and target entity object. |
| **inward_description** | **str** | Required | The description to relate target entity object and source entity object. |
| **life_time** | **str** | Optional | Describes how the relationships can change over time. Default value: Perpetual. Available values: Perpetual, TimeVariant. |
| **relationship_cardinality** | **str** | Optional | Describes the cardinality of the relationship with a specific source entity object and relationships under this definition. Default value: ManyToMany. Available values: ManyToOne, ManyToMany. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CreateRelationshipDefinitionRequest import CreateRelationshipDefinitionRequest

instance = CreateRelationshipDefinitionRequest(
    scope="...",  # required — The scope that the relationship definition exists in.
    code="...",  # required — The code of the relationship definition. Together with the scope this uniquely defines the relationship definition.
    source_entity_type="...",  # required — The entity type of the source entity object. Allowed values are &#39;Portfolio&#39;, &#39;PortfolioGroup&#39;, &#39;Person&#39;, &#39;LegalEntity&#39;, &#39;Instrument&#39; or a custom entity type prefixed with &#39;~&#39;.
    target_entity_type="...",  # required — The entity type of the target entity object. Allowed values are &#39;Portfolio&#39;, &#39;PortfolioGroup&#39;, &#39;Person&#39;, &#39;LegalEntity&#39;, &#39;Instrument&#39; or a custom entity type prefixed with &#39;~&#39;.
    display_name="...",  # required — The display name of the relationship definition.
    outward_description="...",  # required — The description to relate source entity object and target entity object.
    inward_description="...",  # required — The description to relate target entity object and source entity object.
    life_time="...",  # optional — Describes how the relationships can change over time. Default value: Perpetual. Available values: Perpetual, TimeVariant.
    relationship_cardinality="..."  # optional — Describes the cardinality of the relationship with a specific source entity object and relationships under this definition. Default value: ManyToMany. Available values: ManyToOne, ManyToMany.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

