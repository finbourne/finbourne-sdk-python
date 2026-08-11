# LogClientInfo

Represents a LogClientInfo resource in the Okta API
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **user_agent** | [LogUserAgent](LogUserAgent.md) | Optional | *No description available.* |
| **zone** | **str** | Optional | *No description available.* |
| **device** | **str** | Optional | *No description available.* |
| **id** | **str** | Optional | *No description available.* |
| **ip_address** | **str** | Optional | *No description available.* |
| **geographical_context** | [LogGeographicalContext](LogGeographicalContext.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.LogClientInfo import LogClientInfo

instance = LogClientInfo(
    user_agent=LogUserAgent(...),  # optional
    zone="...",  # optional
    device="...",  # optional
    id="...",  # optional
    ip_address="...",  # optional
    geographical_context=LogGeographicalContext(...)  # optional
)
```


## Related Models

- [LogUserAgent](LogUserAgent.md)
- [LogGeographicalContext](LogGeographicalContext.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

