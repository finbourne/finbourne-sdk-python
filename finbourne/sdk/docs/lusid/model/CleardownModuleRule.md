# CleardownModuleRule

A Cleardown rule
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **rule_id** | **str** | Required | The identifier for the Cleardown Rule. |
| **general_ledger_account_code** | **str** | Required | The account to post the residual P&amp;L to. |
| **rule_filter** | **str** | Required | The filter syntax for the Cleardown Rule. See https://support.lusid.com/docs/assigning-economic-activity-to-general-ledger-accounts-using-posting-rules for more information on filter syntax. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CleardownModuleRule import CleardownModuleRule

instance = CleardownModuleRule(
    rule_id="...",  # required — The identifier for the Cleardown Rule.
    general_ledger_account_code="...",  # required — The account to post the residual P&amp;L to.
    rule_filter="..."  # required — The filter syntax for the Cleardown Rule. See https://support.lusid.com/docs/assigning-economic-activity-to-general-ledger-accounts-using-posting-rules for more information on filter syntax.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

