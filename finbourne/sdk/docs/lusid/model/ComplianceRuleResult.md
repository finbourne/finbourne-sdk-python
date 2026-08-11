# ComplianceRuleResult

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **rule_id** | **str** | Required | The unique identifierof a compliance rule |
| **rule_name** | **str** | Required | The User-given name of the rule |
| **rule_description** | **str** | Required | The User-given description of the rule |
| **portfolio** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **passed** | **bool** | Required | The result of an individual compliance run, true if passed |
| **result_value** | **float** | Required | The calculation result that was used to confirm a pass/fail |
| **rule_information_match** | **str** | Required | The value matched by the rule |
| **rule_information_key** | **str** | Required | The property key matched by the rule |
| **rule_lower_limit** | **float** | Required | The lower limit of the rule |
| **rule_upper_limit** | **float** | Required | The upper limit of the rule |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ComplianceRuleResult import ComplianceRuleResult

instance = ComplianceRuleResult(
    rule_id="...",  # required — The unique identifierof a compliance rule
    rule_name="...",  # required — The User-given name of the rule
    rule_description="...",  # required — The User-given description of the rule
    portfolio=ResourceId(...),  # required
    passed=True,  # required — The result of an individual compliance run, true if passed
    result_value=0.0,  # required — The calculation result that was used to confirm a pass/fail
    rule_information_match="...",  # required — The value matched by the rule
    rule_information_key="...",  # required — The property key matched by the rule
    rule_lower_limit=0.0,  # required — The lower limit of the rule
    rule_upper_limit=0.0  # required — The upper limit of the rule
)
```

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

