# DataQualityCheckResult

Represents the result of a data quality check operation
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **check_definition_scope** | **str** | Optional | The scope of the check definition |
| **check_definition_code** | **str** | Optional | The code of the check definition |
| **check_definition_display_name** | **str** | Optional | The display name of the check definition |
| **check_run_as_at** | **datetime** | Optional | The timestamp when the check was run |
| **result_type** | **str** | Optional | The type of result from the check |
| **rule_set_key** | **str** | Optional | The key identifying the ruleset |
| **rule_set_display_name** | **str** | Optional | The display name of the ruleset |
| **rule_key** | **str** | Optional | The key identifying the rule (for RuleInvalid, RuleBreached, RuleBreachesOverLimit) |
| **rule_display_name** | **str** | Optional | The display name of the rule (for RuleInvalid, RuleBreached, RuleBreachesOverLimit) |
| **rule_description** | **str** | Optional | The description of the rule (for RuleInvalid, RuleBreached, RuleBreachesOverLimit) |
| **rule_formula** | **str** | Optional | The formula of the rule (for RuleInvalid, RuleBreached, RuleBreachesOverLimit) |
| **severity** | **int** | Optional | The severity level |
| **lusid_entity** | [LusidEntityResult](LusidEntityResult.md) | Optional | *No description available.* |
| **count_rule_breaches** | **int** | Optional | The count of rule breaches (1 for RuleBreached, multiple for RuleBreachesOverLimit) |
| **error_detail** | **str** | Optional | Error details (for RulesetInvalid, RuleInvalid) |
| **result_id** | **str** | Optional | Unique identifier for the result in format: {{GUID of Check Definition}}-{{resultType}}-{{rulesetKey}}-{{ruleKey}}-{{entity GUID}} |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.DataQualityCheckResult import DataQualityCheckResult

instance = DataQualityCheckResult(
    check_definition_scope="...",  # optional — The scope of the check definition
    check_definition_code="...",  # optional — The code of the check definition
    check_definition_display_name="...",  # optional — The display name of the check definition
    check_run_as_at=datetime.now(),  # optional — The timestamp when the check was run
    result_type="...",  # optional — The type of result from the check
    rule_set_key="...",  # optional — The key identifying the ruleset
    rule_set_display_name="...",  # optional — The display name of the ruleset
    rule_key="...",  # optional — The key identifying the rule (for RuleInvalid, RuleBreached, RuleBreachesOverLimit)
    rule_display_name="...",  # optional — The display name of the rule (for RuleInvalid, RuleBreached, RuleBreachesOverLimit)
    rule_description="...",  # optional — The description of the rule (for RuleInvalid, RuleBreached, RuleBreachesOverLimit)
    rule_formula="...",  # optional — The formula of the rule (for RuleInvalid, RuleBreached, RuleBreachesOverLimit)
    severity=0,  # optional — The severity level
    lusid_entity=LusidEntityResult(...),  # optional
    count_rule_breaches=0,  # optional — The count of rule breaches (1 for RuleBreached, multiple for RuleBreachesOverLimit)
    error_detail="...",  # optional — Error details (for RulesetInvalid, RuleInvalid)
    result_id="..."  # optional — Unique identifier for the result in format: {{GUID of Check Definition}}-{{resultType}}-{{rulesetKey}}-{{ruleKey}}-{{entity GUID}}
)
```

- [LusidEntityResult](LusidEntityResult.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

