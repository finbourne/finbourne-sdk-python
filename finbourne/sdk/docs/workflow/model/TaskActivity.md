# TaskActivity

Information about what tasks to create/update when receiving events

## oneOf Type

`TaskActivity` can be one of the following types:

* [CreateNewTaskActivity](./CreateNewTaskActivity.md)
* [UpdateMatchingTasksActivity](./UpdateMatchingTasksActivity.md)

## Usage

### Creating from a compatible type

```python
from finbourne.sdk.services.workflow.models.TaskActivity import TaskActivity

# Construct using any of the compatible types above
create_new_task_activity_instance = workflow.models.create_new_task_activity.CreateNewTaskActivity(
                        initial_trigger = '', 
                        type = 'CreateNewTask', 
                        correlation_ids = [
                            workflow.models.event_handler_mapping.EventHandlerMapping(
                                map_from = '', 
                                set_to = '', )
                            ], 
                        task_fields = {
                            'key' : workflow.models.field_mapping.FieldMapping(
                                map_from = '', 
                                set_to = null, )
                            }, 
                        schedule_dependent_task_fields = {
                            'key' : workflow.models.scheduled_time_adjustment.ScheduledTimeAdjustment(
                                date_adjustment = workflow.models.date_adjustment.DateAdjustment(
                                    delta_days = 56, 
                                    business_day_adjustment = '', ), 
                                time_adjustment = workflow.models.time_adjustment.TimeAdjustment(
                                    set_to = workflow.models.specified_time.SpecifiedTime(
                                        hours = 56, 
                                        minutes = 56, 
                                        type = 'Specified', ), ), )
                            }, )

instance = TaskActivity(create_new_task_activity_instance)
```

## Related Models

- [CreateNewTaskActivity](./CreateNewTaskActivity.md)
- [UpdateMatchingTasksActivity](./UpdateMatchingTasksActivity.md)

[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

