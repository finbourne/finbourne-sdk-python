# IntegrationLogActivity

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **timestamp** | **datetime** | Required | *No description available.* |
| **resulting_status** | **str** | Required | *No description available.* |
| **message_type** | **str** | Optional | *No description available.* |
| **description** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.IntegrationLogActivity import IntegrationLogActivity

instance = IntegrationLogActivity(
    timestamp=datetime.now(),  # required
    resulting_status="...",  # required
    message_type="...",  # optional
    description="..."  # optional
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

