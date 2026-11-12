# ComplianceRuleBreakdownWithContributions

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **group_id** | **int** | Required | A stable identifier for this group within the rule, matching the same group in the rule-result endpoint. |
| **status** | **str** | Required | The status of this subset of results. |
| **group_key** | [ComplianceGroupKey](ComplianceGroupKey.md) | Optional | *No description available.* |
| **nav** | **float** | Optional | The portfolio net asset value the group sits within. Absent where no contribution carried it. |
| **results** | **Dict[str, float]** | Optional | The valuation result totals the group aggregated. Omitted when empty. |
| **comparisons** | [List[ComplianceComparison]](ComplianceComparison.md) | Optional | Every leaf comparison the check criterion made for this group, drawn from both the hard and the soft limit.  Omitted for a group no check reached. |
| **properties** | **Dict[str, Optional[List[ModelProperty]]]** | Optional | The property values the group aggregated. Omitted when empty. |
| **formula_values** | **Dict[str, float]** | Optional | The value each formula within the check criterion evaluated to for this group. Omitted when empty. |
| **contributions** | [List[ComplianceRuleContribution]](ComplianceRuleContribution.md) | Required | The per-position contributions aggregated into this rule breakdown group. Empty when the run  genuinely produced no contributions; a run with no recorded breakdown (e.g. one that predates  this feature) returns a 404 rather than this response. |
| **missing_data_information** | **List[str]** | Optional | List of string information detailing data that was missing from contributions processed in this rule. Omitted when empty. |
| **contribution_count** | **int** | Required | The number of contributions aggregated into this group, before any cap. |
| **contributions_truncated** | **bool** | Required | Whether the reported contributions were capped below ContributionCount. Always false today. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ComplianceRuleBreakdownWithContributions import ComplianceRuleBreakdownWithContributions

instance = ComplianceRuleBreakdownWithContributions(
    group_id=0,  # required — A stable identifier for this group within the rule, matching the same group in the rule-result endpoint.
    status="...",  # required — The status of this subset of results.
    group_key=ComplianceGroupKey(...),  # optional
    nav=0.0,  # optional — The portfolio net asset value the group sits within. Absent where no contribution carried it.
    results=,  # optional — The valuation result totals the group aggregated. Omitted when empty.
    comparisons=[],  # optional — Every leaf comparison the check criterion made for this group, drawn from both the hard and the soft limit.  Omitted for a group no check reached.
    properties=,  # optional — The property values the group aggregated. Omitted when empty.
    formula_values=,  # optional — The value each formula within the check criterion evaluated to for this group. Omitted when empty.
    contributions=[],  # required — The per-position contributions aggregated into this rule breakdown group. Empty when the run  genuinely produced no contributions; a run with no recorded breakdown (e.g. one that predates  this feature) returns a 404 rather than this response.
    missing_data_information=,  # optional — List of string information detailing data that was missing from contributions processed in this rule. Omitted when empty.
    contribution_count=0,  # required — The number of contributions aggregated into this group, before any cap.
    contributions_truncated=True  # required — Whether the reported contributions were capped below ContributionCount. Always false today.
)
```

- [ComplianceGroupKey](ComplianceGroupKey.md)
- [ComplianceComparison](ComplianceComparison.md) — used in `comparisons`
- [ComplianceRuleContribution](ComplianceRuleContribution.md) — used in `contributions`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

