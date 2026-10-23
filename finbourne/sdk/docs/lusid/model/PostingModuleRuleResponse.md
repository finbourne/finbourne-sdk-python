# PostingModuleRuleResponse

A version of a Posting rule
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **rule_id** | **str** | Required | The identifier for the Posting Rule. |
| **general_ledger_account_code** | **str** | Required | The general ledger account to post the Activity credit or debit to. |
| **rule_filter** | **str** | Required | The filter syntax for the Posting Rule. See https://support.lusid.com/docs/assigning-economic-activity-to-general-ledger-accounts-using-posting-rules for more information on filter syntax. |
| **effective_from** | **datetime** | Optional | The inclusive accounting date from which the Posting Rule applies. If not set, the rule applies from the beginning of time. |
| **effective_until** | **datetime** | Optional | The exclusive accounting date until which the Posting Rule applies. If not set, the rule applies until the end of time. |
| **version** | **int** | Optional | The version of the Posting Rule. Starts at 1 and increases each time the rule is superseded. |
| **original_rule_id** | **str** | Optional | The identifier of the Posting Rule that this rule was created to supersede, if any. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PostingModuleRuleResponse import PostingModuleRuleResponse

instance = PostingModuleRuleResponse(
    rule_id="...",  # required — The identifier for the Posting Rule.
    general_ledger_account_code="...",  # required — The general ledger account to post the Activity credit or debit to.
    rule_filter="...",  # required — The filter syntax for the Posting Rule. See https://support.lusid.com/docs/assigning-economic-activity-to-general-ledger-accounts-using-posting-rules for more information on filter syntax.
    effective_from=datetime.now(),  # optional — The inclusive accounting date from which the Posting Rule applies. If not set, the rule applies from the beginning of time.
    effective_until=datetime.now(),  # optional — The exclusive accounting date until which the Posting Rule applies. If not set, the rule applies until the end of time.
    version=0,  # optional — The version of the Posting Rule. Starts at 1 and increases each time the rule is superseded.
    original_rule_id="..."  # optional — The identifier of the Posting Rule that this rule was created to supersede, if any.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

