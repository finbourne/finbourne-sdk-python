# Trigger

Holds different kinds of triggers A schedule may only have one type of trigger
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **time_trigger** | [TimeTrigger](TimeTrigger.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.scheduler.models.Trigger import Trigger

instance = Trigger(
    time_trigger=TimeTrigger(...)  # optional
)
```


## Related Models

- [TimeTrigger](TimeTrigger.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

