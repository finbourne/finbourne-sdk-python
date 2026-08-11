# ChildTaskDefinitionEdge

Represents a parent-child relationship between two Task Definitions in a Workflow
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **parent** | [VersionedTaskDefinitionId](VersionedTaskDefinitionId.md) | Optional | *No description available.* |
| **child** | [VersionedTaskDefinitionId](VersionedTaskDefinitionId.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.ChildTaskDefinitionEdge import ChildTaskDefinitionEdge

instance = ChildTaskDefinitionEdge(
    parent=VersionedTaskDefinitionId(...),  # optional
    child=VersionedTaskDefinitionId(...)  # optional
)
```


## Related Models

- [VersionedTaskDefinitionId](VersionedTaskDefinitionId.md)
- [VersionedTaskDefinitionId](VersionedTaskDefinitionId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

