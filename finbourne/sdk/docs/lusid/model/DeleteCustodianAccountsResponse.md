# DeleteCustodianAccountsResponse

The delete custodian accounts response
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **custodian_account_ids** | [List[ResourceId]](ResourceId.md) | Optional | The Custodian Accounts which have been soft/hard deleted. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.DeleteCustodianAccountsResponse import DeleteCustodianAccountsResponse

instance = DeleteCustodianAccountsResponse(
    version=Version(...),  # optional
    custodian_account_ids=[],  # optional — The Custodian Accounts which have been soft/hard deleted.
    links=[]  # optional
)
```


## Related Models

- [Version](Version.md)
- [ResourceId](ResourceId.md) — used in `custodian_account_ids`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

