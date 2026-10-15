# PackPostingRule

A posting rule on a partnership configuration pack.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **rule_id** | **str** | Required | The posting rule identifier. |
| **transaction_type** | **str** | Required | The transaction type. |
| **debit_account** | **str** | Required | The account debited. |
| **credit_account** | **str** | Required | The account credited. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PackPostingRule import PackPostingRule

instance = PackPostingRule(
    rule_id="...",  # required — The posting rule identifier.
    transaction_type="...",  # required — The transaction type.
    debit_account="...",  # required — The account debited.
    credit_account="..."  # required — The account credited.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

