# Trigger

Response defining a trigger for an instance.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Required | *No description available.* |
| **cron_expression** | **str** | Required | *No description available.* |
| **time_zone** | **str** | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.Trigger import Trigger

instance = Trigger(
    type="...",  # required
    cron_expression="...",  # required
    time_zone="..."  # required
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

