# UpdateRelationalDatasetDetails

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **display_name** | **str** | Required | A user-friendly display name for the relational dataset definition. |
| **description** | **str** | Optional | A detailed description of the relational dataset definition and its purpose. |
| **applicable_entity_types** | [ApplicableEntityTypes](ApplicableEntityTypes.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpdateRelationalDatasetDetails import UpdateRelationalDatasetDetails

instance = UpdateRelationalDatasetDetails(
    display_name="...",  # required — A user-friendly display name for the relational dataset definition.
    description="...",  # optional — A detailed description of the relational dataset definition and its purpose.
    applicable_entity_types=ApplicableEntityTypes(...)  # optional
)
```

- [ApplicableEntityTypes](ApplicableEntityTypes.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

