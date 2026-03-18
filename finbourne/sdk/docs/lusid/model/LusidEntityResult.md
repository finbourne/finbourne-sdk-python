# LusidEntityResult

Represents LUSID entity details for a data quality check result
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **as_at** | **datetime** | Optional | The as-at timestamp for the entity |
| **effective_at** | **datetime** | Optional | The effective-at timestamp for the entity |
| **entity_type** | **str** | Optional | The type of the LUSID entity |
| **scope** | **str** | Optional | The scope of the entity |
| **identifier_key** | **str** | Optional | The identifier key for the entity |
| **identifier_value** | **str** | Optional | The identifier value for the entity |
| **entity_unique_id** | **str** | Optional | The unique identifier for the entity |
| **display_name** | **str** | Optional | The display name of the entity |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.LusidEntityResult import LusidEntityResult

instance = LusidEntityResult(
    as_at=datetime.now(),  # optional — The as-at timestamp for the entity
    effective_at=datetime.now(),  # optional — The effective-at timestamp for the entity
    entity_type="...",  # optional — The type of the LUSID entity
    scope="...",  # optional — The scope of the entity
    identifier_key="...",  # optional — The identifier key for the entity
    identifier_value="...",  # optional — The identifier value for the entity
    entity_unique_id="...",  # optional — The unique identifier for the entity
    display_name="..."  # optional — The display name of the entity
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

