# ApplicableEntity

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **entity_type** | **str** | Required | The type of entity (e.g., Instrument, Portfolio) that this DataSeries applies to. |
| **entity_scope** | **str** | Optional | The scope of the entity. |
| **identifier_scope** | **str** | Optional | The scope of the identifier used to uniquely identify the entity. |
| **identifier_type** | **str** | Optional | The type of identifier (e.g., Figi, Isin) used to uniquely identify the entity. |
| **identifier_value** | **str** | Optional | The value of the identifier used to uniquely identify the entity. |
| **sub_entity_id** | **str** | Optional | An optional sub-entity identifier, if applicable. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ApplicableEntity import ApplicableEntity

instance = ApplicableEntity(
    entity_type="...",  # required — The type of entity (e.g., Instrument, Portfolio) that this DataSeries applies to.
    entity_scope="...",  # optional — The scope of the entity.
    identifier_scope="...",  # optional — The scope of the identifier used to uniquely identify the entity.
    identifier_type="...",  # optional — The type of identifier (e.g., Figi, Isin) used to uniquely identify the entity.
    identifier_value="...",  # optional — The value of the identifier used to uniquely identify the entity.
    sub_entity_id="..."  # optional — An optional sub-entity identifier, if applicable.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

