# CreateScheduleRequest

Create a schedule definition
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **schedule_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **job_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **name** | **str** | Required | A display name for this Schedule |
| **description** | **str** | Required | A description of the Schedule |
| **author** | **str** | Optional | Name of the author of this schedule |
| **owner** | **str** | Optional | Name of owner of this schedule |
| **arguments** | **Dict[str, Optional[str]]** | Optional | All arguments specified by this Schedule that will be passed in to the Job |
| **trigger** | [Trigger](Trigger.md) | Optional | *No description available.* |
| **notifications** | [List[Notification]](Notification.md) | Optional | Notifications for this Schedule |
| **enabled** | **bool** | Optional | Specify whether schedule is enabled or not Defaults to true |
| **use_as_auth** | **str** | Optional | Id of user associated with schedule. All calls to FINBOURNE services as part of execution of this schedule will be authenticated as this  user. Can be null, in which case we&#39;ll default to that of the user  making this request |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.scheduler.models.CreateScheduleRequest import CreateScheduleRequest

instance = CreateScheduleRequest(
    schedule_id=ResourceId(...),  # required
    job_id=ResourceId(...),  # required
    name="...",  # required — A display name for this Schedule
    description="...",  # required — A description of the Schedule
    author="...",  # optional — Name of the author of this schedule
    owner="...",  # optional — Name of owner of this schedule
    arguments=,  # optional — All arguments specified by this Schedule that will be passed in to the Job
    trigger=Trigger(...),  # optional
    notifications=[],  # optional — Notifications for this Schedule
    enabled=True,  # optional — Specify whether schedule is enabled or not Defaults to true
    use_as_auth="..."  # optional — Id of user associated with schedule. All calls to FINBOURNE services as part of execution of this schedule will be authenticated as this  user. Can be null, in which case we&#39;ll default to that of the user  making this request
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [Trigger](Trigger.md)
- [Notification](Notification.md) — used in `notifications`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

