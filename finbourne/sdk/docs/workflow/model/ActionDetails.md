# ActionDetails

Abstracts the kinds of Actions available

## oneOf Type

`ActionDetails` can be one of the following types:

* [CreateChildTasksAction](./CreateChildTasksAction.md)
* [RunWorkerAction](./RunWorkerAction.md)
* [TriggerChildTasksAction](./TriggerChildTasksAction.md)
* [TriggerParentTaskAction](./TriggerParentTaskAction.md)

## Usage

### Creating from a compatible type

```python
from finbourne.sdk.services.workflow.models.ActionDetails import ActionDetails

# Construct using any of the compatible types above
create_child_tasks_action_instance = workflow.models.create_child_tasks_action.CreateChildTasksAction(
                        type = 'CreateChildTasks', 
                        child_task_configurations = [
                            workflow.models.create_child_task_configuration.CreateChildTaskConfiguration(
                                task_definition_id = workflow.models.resource_id.ResourceId(
                                    scope = '', 
                                    code = '', ), 
                                task_definition_as_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                initial_trigger = 'z', 
                                child_task_fields = {
                                    'key' : workflow.models.field_mapping.FieldMapping(
                                        map_from = '', 
                                        set_to = null, )
                                    }, 
                                map_stacking_key_from = '', )
                            ], )

instance = ActionDetails(create_child_tasks_action_instance)
```

## Related Models

- [CreateChildTasksAction](./CreateChildTasksAction.md)
- [RunWorkerAction](./RunWorkerAction.md)
- [TriggerChildTasksAction](./TriggerChildTasksAction.md)
- [TriggerParentTaskAction](./TriggerParentTaskAction.md)

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

