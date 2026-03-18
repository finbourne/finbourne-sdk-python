# Attempt

Details of an attempt of delivery.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **attempt_number** | **int** | Required | The attempt number of the delivery. |
| **attempt_time** | **datetime** | Required | The time that the delivery was attempted. |
| **status** | [AttemptStatus](AttemptStatus.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.notifications.models.Attempt import Attempt

instance = Attempt(
    attempt_number=0,  # required — The attempt number of the delivery.
    attempt_time=datetime.now(),  # required — The time that the delivery was attempted.
    status=AttemptStatus(...)  # required
)
```

- [AttemptStatus](AttemptStatus.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

