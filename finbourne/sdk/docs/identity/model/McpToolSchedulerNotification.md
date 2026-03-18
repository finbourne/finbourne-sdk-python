# McpToolSchedulerNotification

A notification configuration for a scheduler job
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Required | The type of notification (e.g., \&quot;Email\&quot;, \&quot;Webhook\&quot;) |
| **target** | **str** | Required | The target of the notification (e.g., email address, webhook URL) |
| **trigger** | **str** | Required | When to send the notification (e.g., \&quot;OnSuccess\&quot;, \&quot;OnFailure\&quot;, \&quot;Always\&quot;) |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.McpToolSchedulerNotification import McpToolSchedulerNotification

instance = McpToolSchedulerNotification(
    type="...",  # required — The type of notification (e.g., \&quot;Email\&quot;, \&quot;Webhook\&quot;)
    target="...",  # required — The target of the notification (e.g., email address, webhook URL)
    trigger="..."  # required — When to send the notification (e.g., \&quot;OnSuccess\&quot;, \&quot;OnFailure\&quot;, \&quot;Always\&quot;)
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

