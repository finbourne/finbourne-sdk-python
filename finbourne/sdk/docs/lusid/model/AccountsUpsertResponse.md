# AccountsUpsertResponse

The upsert accounts response
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **accounts** | [List[Account]](Account.md) | Optional | The Accounts which have been upserted. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AccountsUpsertResponse import AccountsUpsertResponse

instance = AccountsUpsertResponse(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    version=Version(...),  # optional
    accounts=[],  # optional — The Accounts which have been upserted.
    links=[]  # optional
)
```

- [Version](Version.md)
- [Account](Account.md) — used in `accounts`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

