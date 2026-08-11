# CreateChildTaskConfiguration

Create Child Task Configuration
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **task_definition_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **task_definition_as_at** | **datetime** | Optional | TaskDefinition AsAt timestamp |
| **initial_trigger** | **str** | Optional | The Initial Trigger for automatic start |
| **child_task_fields** | [Dict[str, FieldMapping]](FieldMapping.md) | Optional | Field Mappings |
| **map_stacking_key_from** | **str** | Optional | If present, the value of this field on the parent task will be the Stacking Key on any created child tasks |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.CreateChildTaskConfiguration import CreateChildTaskConfiguration

instance = CreateChildTaskConfiguration(
    task_definition_id=ResourceId(...),  # required
    task_definition_as_at=datetime.now(),  # optional — TaskDefinition AsAt timestamp
    initial_trigger="...",  # optional — The Initial Trigger for automatic start
    child_task_fields=FieldMapping(...),  # optional — Field Mappings
    map_stacking_key_from="..."  # optional — If present, the value of this field on the parent task will be the Stacking Key on any created child tasks
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [FieldMapping](FieldMapping.md) — used in `child_task_fields`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

