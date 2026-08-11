# AuthenticationInformation

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **issuer_url** | **str** | Required | *No description available.* |
| **fallback_issuer_urls** | **List[str]** | Optional | *No description available.* |
| **saml_identity_provider_id** | **str** | Optional | *No description available.* |
| **support** | [SupportAccessExpiry](SupportAccessExpiry.md) | Optional | *No description available.* |
| **support_access_expiry_with_role** | [List[SupportAccessExpiryWithRole]](SupportAccessExpiryWithRole.md) | Optional | *No description available.* |
| **status** | **bool** | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.AuthenticationInformation import AuthenticationInformation

instance = AuthenticationInformation(
    issuer_url="...",  # required
    fallback_issuer_urls=,  # optional
    saml_identity_provider_id="...",  # optional
    support=SupportAccessExpiry(...),  # optional
    support_access_expiry_with_role=[],  # optional
    status=True,  # optional
    links=[]  # optional
)
```

- [SupportAccessExpiry](SupportAccessExpiry.md)
- [SupportAccessExpiryWithRole](SupportAccessExpiryWithRole.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

