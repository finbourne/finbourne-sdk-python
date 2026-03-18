# TaskStateDefinition

A Task Definition/Task has a given set of States
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Required | The Name of this State |
| **display_name** | **str** | Optional | The display name of this State |
| **description** | **str** | Optional | The description of this State |
| **category** | **str** | Optional | The category of this State |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.TaskStateDefinition import TaskStateDefinition

instance = TaskStateDefinition(
    name="...",  # required — The Name of this State
    display_name="...",  # optional — The display name of this State
    description="...",  # optional — The description of this State
    category="..."  # optional — The category of this State
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

