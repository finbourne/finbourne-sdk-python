# MarginAccounts

The custodian account each party's collateral is held in.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **we_post** | **str** | Optional | The code of the custodian account, within each applicable portfolio, that holds collateral we post. Empty means collateral we post is not held in a custodian account the item knows of. |
| **they_post** | **str** | Optional | The code of the custodian account, within each applicable portfolio, that holds collateral the counterparty posts. Empty means collateral they post is not held in a custodian account the item knows of. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.MarginAccounts import MarginAccounts

instance = MarginAccounts(
    we_post="...",  # optional — The code of the custodian account, within each applicable portfolio, that holds collateral we post. Empty means collateral we post is not held in a custodian account the item knows of.
    they_post="..."  # optional — The code of the custodian account, within each applicable portfolio, that holds collateral the counterparty posts. Empty means collateral they post is not held in a custodian account the item knows of.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

