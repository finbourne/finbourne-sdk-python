# StagedModificationsInfo

The staged modifications metadata.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **count_pending** | **int** | Required | The number of staged modifications for the entity with a status of Pending for the requested asAt. |
| **href_pending** | **str** | Required | Link to the list staged modifications endpoint, filtered by entityType, entityUniqueId and status (&#x3D; Pending). |
| **ids_previewed** | **List[str]** | Optional | An array of the ids of any StagedModifications being previewed. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.StagedModificationsInfo import StagedModificationsInfo

instance = StagedModificationsInfo(
    count_pending=0,  # required — The number of staged modifications for the entity with a status of Pending for the requested asAt.
    href_pending="...",  # required — Link to the list staged modifications endpoint, filtered by entityType, entityUniqueId and status (&#x3D; Pending).
    ids_previewed=  # optional — An array of the ids of any StagedModifications being previewed.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

