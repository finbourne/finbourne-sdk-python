# AccountHolderIdentifier

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **key** | **str** | Required | A client-defined key used to identify the Account Holder, unique within the Investment Account |
| **scope** | **str** | Required | The scope in which the Investor Record lies. |
| **identifiers** | **Dict[str, Optional[str]]** | Required | Single Account Holder identifier that should target the desired Investor Record. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AccountHolderIdentifier import AccountHolderIdentifier

instance = AccountHolderIdentifier(
    key="...",  # required — A client-defined key used to identify the Account Holder, unique within the Investment Account
    scope="...",  # required — The scope in which the Investor Record lies.
    identifiers=  # required — Single Account Holder identifier that should target the desired Investor Record.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

