# PackAccount

An account on a partnership configuration pack's chart of accounts.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Required | The account code. |
| **name** | **str** | Required | The account name. |
| **type** | **str** | Required | The account type: Asset, Liability, Capital, Income or Expense. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PackAccount import PackAccount

instance = PackAccount(
    code="...",  # required — The account code.
    name="...",  # required — The account name.
    type="..."  # required — The account type: Asset, Liability, Capital, Income or Expense.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

