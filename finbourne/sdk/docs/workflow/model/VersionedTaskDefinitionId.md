# VersionedTaskDefinitionId

A Task Definition Id with an optional asAt timestamp identifying a specific version
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **task_definition_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **task_definition_as_at** | **datetime** | Optional | The asAt time of this version of the Task Definition. Null means the latest version. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.VersionedTaskDefinitionId import VersionedTaskDefinitionId

instance = VersionedTaskDefinitionId(
    task_definition_id=ResourceId(...),  # optional
    task_definition_as_at=datetime.now()  # optional — The asAt time of this version of the Task Definition. Null means the latest version.
)
```


## Related Models

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

