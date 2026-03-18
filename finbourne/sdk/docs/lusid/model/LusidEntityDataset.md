# LusidEntityDataset

Contains the run-time parameters that are appropriate for check definitions  with datasetSchema.type = \"LusidEntity\"
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **as_at** | **datetime** | Optional | The asAt date to fetch the data. Nullable. Defaults to latest. |
| **effective_at** | **datetime** | Optional | The effectiveAt date to fetch the data. Nullable. Defaults to latest. |
| **scope** | **str** | Optional | The scope of the entities to check. Required. |
| **as_at_modified_since** | **datetime** | Optional | Nullable. Filters the dataset for version.asAtModified greater than or equal to this value. |
| **selector_attribute** | **str** | Optional | An attribute (field name, propertyKey or identifierKey) to use to sub-divide the dataset. |
| **selector_value** | **str** | Optional | The value of the above attribute used to sub-divide the dataset. |
| **return_identifier_key** | **str** | Optional | The preferred identifier to return for entities with multiple external identifiers. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.LusidEntityDataset import LusidEntityDataset

instance = LusidEntityDataset(
    as_at=datetime.now(),  # optional — The asAt date to fetch the data. Nullable. Defaults to latest.
    effective_at=datetime.now(),  # optional — The effectiveAt date to fetch the data. Nullable. Defaults to latest.
    scope="...",  # optional — The scope of the entities to check. Required.
    as_at_modified_since=datetime.now(),  # optional — Nullable. Filters the dataset for version.asAtModified greater than or equal to this value.
    selector_attribute="...",  # optional — An attribute (field name, propertyKey or identifierKey) to use to sub-divide the dataset.
    selector_value="...",  # optional — The value of the above attribute used to sub-divide the dataset.
    return_identifier_key="..."  # optional — The preferred identifier to return for entities with multiple external identifiers.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

