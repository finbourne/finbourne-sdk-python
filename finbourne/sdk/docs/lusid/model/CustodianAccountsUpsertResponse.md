# CustodianAccountsUpsertResponse

The upsert accounts response
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **custodian_accounts** | [List[CustodianAccount]](CustodianAccount.md) | Optional | The Custodian Accounts which have been upserted. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CustodianAccountsUpsertResponse import CustodianAccountsUpsertResponse

instance = CustodianAccountsUpsertResponse(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    version=Version(...),  # optional
    custodian_accounts=[],  # optional — The Custodian Accounts which have been upserted.
    links=[]  # optional
)
```

- [Version](Version.md)
- [CustodianAccount](CustodianAccount.md) — used in `custodian_accounts`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

