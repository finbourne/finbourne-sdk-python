# ManualEventBody

The body of the manual event
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **subject** | **str** | Required | The subject of the manual event |
| **message** | **str** | Required | The message of the manual event |
| **json_message** | **object** | Optional | The JSON message of the manual event |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.notifications.models.ManualEventBody import ManualEventBody

instance = ManualEventBody(
    subject="...",  # required — The subject of the manual event
    message="...",  # required — The message of the manual event
    json_message=  # optional — The JSON message of the manual event
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

