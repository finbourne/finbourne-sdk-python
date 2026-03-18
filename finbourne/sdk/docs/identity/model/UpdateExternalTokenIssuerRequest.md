# UpdateExternalTokenIssuerRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **issuer** | **str** | Optional | *No description available.* |
| **audience** | **str** | Optional | *No description available.* |
| **description** | **str** | Optional | *No description available.* |
| **claim_mappings** | [ClaimMappings](ClaimMappings.md) | Optional | *No description available.* |
| **logout_url** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.identity.models.UpdateExternalTokenIssuerRequest import UpdateExternalTokenIssuerRequest

instance = UpdateExternalTokenIssuerRequest(
    issuer="...",  # optional
    audience="...",  # optional
    description="...",  # optional
    claim_mappings=ClaimMappings(...),  # optional
    logout_url="..."  # optional
)
```

- [ClaimMappings](ClaimMappings.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

