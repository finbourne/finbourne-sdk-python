# PostingModuleRule

A Posting rule
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **rule_id** | **str** | Required | The identifier for the Posting Rule. |
| **general_ledger_account_code** | **str** | Required | The general ledger account to post the Activity credit or debit to. |
| **rule_filter** | **str** | Required | The filter syntax for the Posting Rule. See https://support.lusid.com/knowledgebase/article/KA-02140 for more information on filter syntax. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PostingModuleRule import PostingModuleRule

instance = PostingModuleRule(
    rule_id="...",  # required — The identifier for the Posting Rule.
    general_ledger_account_code="...",  # required — The general ledger account to post the Activity credit or debit to.
    rule_filter="..."  # required — The filter syntax for the Posting Rule. See https://support.lusid.com/knowledgebase/article/KA-02140 for more information on filter syntax.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

