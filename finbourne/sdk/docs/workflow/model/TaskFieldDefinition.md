# TaskFieldDefinition

Defines a Task Definition Field
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Required | The name of this Field |
| **type** | **str** | Required | The value type for the field. Available values are: \&quot;String\&quot;, \&quot;Decimal\&quot;, \&quot;DateTime\&quot;, \&quot;Boolean\&quot;) |
| **read_only_states** | [ReadOnlyStates](ReadOnlyStates.md) | Optional | *No description available.* |
| **value_constraints** | [ValueConstraints](ValueConstraints.md) | Optional | *No description available.* |
| **display_name** | **str** | Optional | Display name for field definition |
| **description** | **str** | Optional | Description for field definition |
| **category** | **str** | Optional | Category for field definition |
| **contains_url** | **bool** | Optional | Field contains url |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.TaskFieldDefinition import TaskFieldDefinition

instance = TaskFieldDefinition(
    name="...",  # required — The name of this Field
    type="...",  # required — The value type for the field. Available values are: \&quot;String\&quot;, \&quot;Decimal\&quot;, \&quot;DateTime\&quot;, \&quot;Boolean\&quot;)
    read_only_states=ReadOnlyStates(...),  # optional
    value_constraints=ValueConstraints(...),  # optional
    display_name="...",  # optional — Display name for field definition
    description="...",  # optional — Description for field definition
    category="...",  # optional — Category for field definition
    contains_url=True  # optional — Field contains url
)
```

- [ReadOnlyStates](ReadOnlyStates.md)
- [ValueConstraints](ValueConstraints.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

