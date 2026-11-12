# ComplianceSummaryRuleResultWithContributions

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **rule_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **status** | **str** | Required | *No description available.* |
| **check_type** | **str** | Optional | The kind of check the rule applied across its groups: \&quot;PercentCheck\&quot; or \&quot;Check\&quot;. Static per rule. Absent for a  rule no check reached. |
| **affected_portfolios** | [List[ResourceId]](ResourceId.md) | Required | *No description available.* |
| **affected_orders** | [List[ResourceId]](ResourceId.md) | Optional | The orders the rule affected. Omitted for a holdings-based run. |
| **groups** | [List[ComplianceRuleBreakdownWithContributions]](ComplianceRuleBreakdownWithContributions.md) | Required | *No description available.* |
| **other_positions_considered** | [List[ComplianceRuleContribution]](ComplianceRuleContribution.md) | Optional | The rest of the basis the rule was measured against but did not directly evaluate — the positions in  the referenced/denominator (or initial) group that are not in a group&#39;s contributions. Together with those  contributions this forms the whole basis, with no overlap, so a breach can be explained against the full picture  (e.g. the non-equity remainder behind an equity limit). Omitted when the rule evaluated everything it considered. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ComplianceSummaryRuleResultWithContributions import ComplianceSummaryRuleResultWithContributions

instance = ComplianceSummaryRuleResultWithContributions(
    rule_id=ResourceId(...),  # required
    status="...",  # required
    check_type="...",  # optional — The kind of check the rule applied across its groups: \&quot;PercentCheck\&quot; or \&quot;Check\&quot;. Static per rule. Absent for a  rule no check reached.
    affected_portfolios=[],  # required
    affected_orders=[],  # optional — The orders the rule affected. Omitted for a holdings-based run.
    groups=[],  # required
    other_positions_considered=[]  # optional — The rest of the basis the rule was measured against but did not directly evaluate — the positions in  the referenced/denominator (or initial) group that are not in a group&#39;s contributions. Together with those  contributions this forms the whole basis, with no overlap, so a breach can be explained against the full picture  (e.g. the non-equity remainder behind an equity limit). Omitted when the rule evaluated everything it considered.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md) — used in `affected_orders`
- [ComplianceRuleBreakdownWithContributions](ComplianceRuleBreakdownWithContributions.md)
- [ComplianceRuleContribution](ComplianceRuleContribution.md) — used in `other_positions_considered`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

