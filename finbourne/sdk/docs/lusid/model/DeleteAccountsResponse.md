# DeleteAccountsResponse

The delete accounts response
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **account_ids** | **List[str]** | Optional | The Accounts which have been soft/hard deleted. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.DeleteAccountsResponse import DeleteAccountsResponse

instance = DeleteAccountsResponse(
    version=Version(...),  # optional
    account_ids=,  # optional — The Accounts which have been soft/hard deleted.
    links=[]  # optional
)
```


## Related Models

- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

