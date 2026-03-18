# OAuthApplication

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | **str** | Required | *No description available.* |
| **type** | **str** | Required | *No description available.* |
| **display_name** | **str** | Required | *No description available.* |
| **secret** | **str** | Optional | *No description available.* |
| **client_id** | **str** | Required | *No description available.* |
| **issuer** | **str** | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.OAuthApplication import OAuthApplication

instance = OAuthApplication(
    id="...",  # required
    type="...",  # required
    display_name="...",  # required
    secret="...",  # optional
    client_id="...",  # required
    issuer="..."  # required
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

