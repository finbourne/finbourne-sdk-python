# WebhookNotificationTypeResponse

Holds readonly information about a Webhook notification
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Optional | The type of delivery mechanism for this notification |
| **http_method** | **str** | Optional | The HTTP method such as GET, POST, etc. to use on the request |
| **url** | **str** | Optional | The URL to send the request to |
| **authentication_type** | **str** | Optional | The type of authentication to use on the request |
| **authentication_configuration_item_paths** | **Dict[str, Optional[str]]** | Optional | The paths of the Configuration Store configuration items that contain the authentication configuration. Each authentication type requires different keys: - Lusid - None required - BasicAuth - Requires &#39;Username&#39; and &#39;Password&#39; - BearerToken - Requires &#39;BearerToken&#39; and optionally &#39;BearerScheme&#39;              e.g. the following would be valid assuming that the config is present in the configuration store at the specified paths:                  \&quot;authenticationType\&quot;: \&quot;BasicAuth\&quot;,     \&quot;authenticationConfigurationItemPaths\&quot;: {         \&quot;Username\&quot;: \&quot;config://personal/myUserId/WebhookConfigurations/ExampleService/AdminUser\&quot;,         \&quot;Password\&quot;: \&quot;config://personal/myUserId/WebhookConfigurations/ExampleService/AdminPassword\&quot;     } |
| **content_type** | **str** | Optional | The type of the content e.g. Json |
| **content** | **object** | Optional | The content of the request |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.notifications.models.WebhookNotificationTypeResponse import WebhookNotificationTypeResponse

instance = WebhookNotificationTypeResponse(
    type="...",  # optional — The type of delivery mechanism for this notification
    http_method="...",  # optional — The HTTP method such as GET, POST, etc. to use on the request
    url="...",  # optional — The URL to send the request to
    authentication_type="...",  # optional — The type of authentication to use on the request
    authentication_configuration_item_paths=,  # optional — The paths of the Configuration Store configuration items that contain the authentication configuration. Each authentication type requires different keys: - Lusid - None required - BasicAuth - Requires &#39;Username&#39; and &#39;Password&#39; - BearerToken - Requires &#39;BearerToken&#39; and optionally &#39;BearerScheme&#39;              e.g. the following would be valid assuming that the config is present in the configuration store at the specified paths:                  \&quot;authenticationType\&quot;: \&quot;BasicAuth\&quot;,     \&quot;authenticationConfigurationItemPaths\&quot;: {         \&quot;Username\&quot;: \&quot;config://personal/myUserId/WebhookConfigurations/ExampleService/AdminUser\&quot;,         \&quot;Password\&quot;: \&quot;config://personal/myUserId/WebhookConfigurations/ExampleService/AdminPassword\&quot;     }
    content_type="...",  # optional — The type of the content e.g. Json
    content=  # optional — The content of the request
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

