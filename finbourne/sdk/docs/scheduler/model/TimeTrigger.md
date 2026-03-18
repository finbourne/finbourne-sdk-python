# TimeTrigger

Time-based trigger
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **expression** | **str** | Optional | Cron expression |
| **time_zone** | **str** | Optional | Time zone of the Cron expression. If not provided, defaults to UTC |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.scheduler.models.TimeTrigger import TimeTrigger

instance = TimeTrigger(
    expression="...",  # optional — Cron expression
    time_zone="..."  # optional — Time zone of the Cron expression. If not provided, defaults to UTC
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

