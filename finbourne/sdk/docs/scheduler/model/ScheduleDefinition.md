# ScheduleDefinition

Schedule
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **schedule_identifier** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **job_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **name** | **str** | Optional | A display name for this Schedule |
| **description** | **str** | Optional | A description of the Schedule |
| **author** | **str** | Optional | Name of the author of this schedule |
| **owner** | **str** | Optional | Name of owner of this schedule |
| **use_as_auth** | **str** | Optional | User to runs schedule when automatically run and authenticates  requests in the schedule |
| **arguments** | **Dict[str, Optional[str]]** | Optional | All arguments specified by this Schedule that will be passed in to the Job |
| **trigger** | [Trigger](Trigger.md) | Optional | *No description available.* |
| **notifications** | [List[Notification]](Notification.md) | Optional | Notifications for this Schedule |
| **enabled** | **bool** | Optional | The status of this schedule |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.scheduler.models.ScheduleDefinition import ScheduleDefinition

instance = ScheduleDefinition(
    schedule_identifier=ResourceId(...),  # required
    job_id=ResourceId(...),  # optional
    name="...",  # optional — A display name for this Schedule
    description="...",  # optional — A description of the Schedule
    author="...",  # optional — Name of the author of this schedule
    owner="...",  # optional — Name of owner of this schedule
    use_as_auth="...",  # optional — User to runs schedule when automatically run and authenticates  requests in the schedule
    arguments=,  # optional — All arguments specified by this Schedule that will be passed in to the Job
    trigger=Trigger(...),  # optional
    notifications=[],  # optional — Notifications for this Schedule
    enabled=True  # optional — The status of this schedule
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [Trigger](Trigger.md)
- [Notification](Notification.md) — used in `notifications`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

