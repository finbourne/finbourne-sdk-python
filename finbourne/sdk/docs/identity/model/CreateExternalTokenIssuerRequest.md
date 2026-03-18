# CreateExternalTokenIssuerRequest

Client input for creating an external token issuer.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Required | *No description available.* |
| **issuer** | **str** | Required | *No description available.* |
| **audience** | **str** | Required | *No description available.* |
| **description** | **str** | Optional | *No description available.* |
| **claim_mappings** | [ClaimMappings](ClaimMappings.md) | Optional | *No description available.* |
| **logout_url** | **str** | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.CreateExternalTokenIssuerRequest import CreateExternalTokenIssuerRequest

instance = CreateExternalTokenIssuerRequest(
    code="...",  # required
    issuer="...",  # required
    audience="...",  # required
    description="...",  # optional
    claim_mappings=ClaimMappings(...),  # optional
    logout_url="..."  # required
)
```

- [ClaimMappings](ClaimMappings.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

