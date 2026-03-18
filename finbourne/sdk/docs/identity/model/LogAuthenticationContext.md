# LogAuthenticationContext

Represents a LogAuthenticationContext resource in the Okta API
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **authentication_provider** | **str** | Optional | *No description available.* |
| **credential_provider** | **List[str]** | Optional | *No description available.* |
| **credential_type** | **List[str]** | Optional | *No description available.* |
| **issuer** | [LogIssuer](LogIssuer.md) | Optional | *No description available.* |
| **interface** | **str** | Optional | *No description available.* |
| **authentication_step** | **int** | Optional | *No description available.* |
| **external_session_id** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.LogAuthenticationContext import LogAuthenticationContext

instance = LogAuthenticationContext(
    authentication_provider="...",  # optional
    credential_provider=,  # optional
    credential_type=,  # optional
    issuer=LogIssuer(...),  # optional
    interface="...",  # optional
    authentication_step=0,  # optional
    external_session_id="..."  # optional
)
```

- [LogIssuer](LogIssuer.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

