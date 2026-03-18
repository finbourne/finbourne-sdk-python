# ExternalTokenIssuerResponse

Response DTO exposed to client for an external token issuer.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Optional | The External Token Issuer Code |
| **issuer** | **str** | Optional | Issuer of the External Token Issuer |
| **audience** | **str** | Optional | Audience of the External Token Issuer |
| **description** | **str** | Optional | The Description of the External Token Issuer |
| **claim_mappings** | [ClaimMappings](ClaimMappings.md) | Optional | *No description available.* |
| **logout_url** | **str** | Optional | The LogoutUrl of the External Token Issuer |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.ExternalTokenIssuerResponse import ExternalTokenIssuerResponse

instance = ExternalTokenIssuerResponse(
    code="...",  # optional — The External Token Issuer Code
    issuer="...",  # optional — Issuer of the External Token Issuer
    audience="...",  # optional — Audience of the External Token Issuer
    description="...",  # optional — The Description of the External Token Issuer
    claim_mappings=ClaimMappings(...),  # optional
    logout_url="..."  # optional — The LogoutUrl of the External Token Issuer
)
```

- [ClaimMappings](ClaimMappings.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

