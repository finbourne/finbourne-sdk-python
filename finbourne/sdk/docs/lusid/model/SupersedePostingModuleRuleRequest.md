# SupersedePostingModuleRuleRequest

The next version of a Posting Rule, which takes over from its latest version on an accounting date
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **rule_id** | **str** | Required | The identifier of the Posting Rule. At most one rule in the request may have the ruleId of the superseded rule. If it does, the existing rule is capped so that it stops applying from this rule&#39;s EffectiveFrom, and this rule is created as its next version. Otherwise this rule is created as a new rule. |
| **effective_from** | **datetime** | Required | The inclusive accounting date from which this rule applies. If this rule has the ruleId of the superseded rule, the superseded rule&#39;s latest version stops applying from this date, unless it already ends by then; it is never extended. |
| **effective_until** | **datetime** | Optional | The exclusive accounting date until which this rule applies. If not set, it applies until the end of time. |
| **general_ledger_account_code** | **str** | Required | The general ledger account this rule posts the Activity credit or debit to. |
| **rule_filter** | **str** | Required | The filter syntax for this rule. See https://support.lusid.com/docs/assigning-economic-activity-to-general-ledger-accounts-using-posting-rules for more information on filter syntax. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SupersedePostingModuleRuleRequest import SupersedePostingModuleRuleRequest

instance = SupersedePostingModuleRuleRequest(
    rule_id="...",  # required — The identifier of the Posting Rule. At most one rule in the request may have the ruleId of the superseded rule. If it does, the existing rule is capped so that it stops applying from this rule&#39;s EffectiveFrom, and this rule is created as its next version. Otherwise this rule is created as a new rule.
    effective_from=datetime.now(),  # required — The inclusive accounting date from which this rule applies. If this rule has the ruleId of the superseded rule, the superseded rule&#39;s latest version stops applying from this date, unless it already ends by then; it is never extended.
    effective_until=datetime.now(),  # optional — The exclusive accounting date until which this rule applies. If not set, it applies until the end of time.
    general_ledger_account_code="...",  # required — The general ledger account this rule posts the Activity credit or debit to.
    rule_filter="..."  # required — The filter syntax for this rule. See https://support.lusid.com/docs/assigning-economic-activity-to-general-ledger-accounts-using-posting-rules for more information on filter syntax.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

