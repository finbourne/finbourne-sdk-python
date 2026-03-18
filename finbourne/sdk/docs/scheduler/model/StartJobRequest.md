# StartJobRequest

Job start definition
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **arguments** | **Dict[str, Optional[str]]** | Optional | All arguments needed for the Job to run |
| **notifications** | [List[Notification]](Notification.md) | Optional | Notifications for this Job |
| **use_as_auth** | **str** | Optional | Id of user associated with schedule. All calls to FINBOURNE services as part of execution of this schedule will be authenticated as this  user. Can be null, in which case we&#39;ll default to that of the user  making this request |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.scheduler.models.StartJobRequest import StartJobRequest

instance = StartJobRequest(
    arguments=,  # optional — All arguments needed for the Job to run
    notifications=[],  # optional — Notifications for this Job
    use_as_auth="..."  # optional — Id of user associated with schedule. All calls to FINBOURNE services as part of execution of this schedule will be authenticated as this  user. Can be null, in which case we&#39;ll default to that of the user  making this request
)
```

- [Notification](Notification.md) — used in `notifications`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

