# ComplianceSummaryRuleResultWithContributions

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **rule_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **template_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **variation** | **str** | Required | *No description available.* |
| **rule_status** | **str** | Required | *No description available.* |
| **affected_portfolios** | [List[ResourceId]](ResourceId.md) | Required | *No description available.* |
| **affected_orders** | [List[ResourceId]](ResourceId.md) | Required | *No description available.* |
| **parameters_used** | **Dict[str, Optional[str]]** | Required | *No description available.* |
| **rule_breakdown** | [List[ComplianceRuleBreakdownWithContributions]](ComplianceRuleBreakdownWithContributions.md) | Required | *No description available.* |
| **other_positions_considered** | [List[ComplianceRuleContribution]](ComplianceRuleContribution.md) | Required | The rest of the basis the rule was measured against but did not directly evaluate — the positions in  the referenced/denominator (or initial) group that are not in the RuleBreakdown&#39;s  contributions. Together with those contributions this forms the whole basis, with no overlap, so a  breach can be explained against the full picture (e.g. the non-equity remainder behind an equity limit).  Empty when the rule evaluated everything it considered. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ComplianceSummaryRuleResultWithContributions import ComplianceSummaryRuleResultWithContributions

instance = ComplianceSummaryRuleResultWithContributions(
    rule_id=ResourceId(...),  # required
    template_id=ResourceId(...),  # required
    variation="...",  # required
    rule_status="...",  # required
    affected_portfolios=[],  # required
    affected_orders=[],  # required
    parameters_used=,  # required
    rule_breakdown=[],  # required
    other_positions_considered=[]  # required — The rest of the basis the rule was measured against but did not directly evaluate — the positions in  the referenced/denominator (or initial) group that are not in the RuleBreakdown&#39;s  contributions. Together with those contributions this forms the whole basis, with no overlap, so a  breach can be explained against the full picture (e.g. the non-equity remainder behind an equity limit).  Empty when the rule evaluated everything it considered.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ComplianceRuleBreakdownWithContributions](ComplianceRuleBreakdownWithContributions.md)
- [ComplianceRuleContribution](ComplianceRuleContribution.md) — used in `other_positions_considered`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

