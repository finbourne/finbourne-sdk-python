# ComplianceRuleBreakdownWithContributions

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **group_status** | **str** | Required | The status of this subset of results. |
| **results_used** | **Dict[str, float]** | Required | Dictionary of AddressKey (as string) and their corresponding decimal values, that were used in this rule. |
| **properties_used** | **Dict[str, Optional[List[ModelProperty]]]** | Required | Dictionary of PropertyKey (as string) and their corresponding Properties, that were used in this rule |
| **missing_data_information** | **List[str]** | Required | List of string information detailing data that was missing from contributions processed in this rule |
| **lineage** | [List[LineageMember]](LineageMember.md) | Required | *No description available.* |
| **contributions** | [List[ComplianceRuleContribution]](ComplianceRuleContribution.md) | Required | The per-position contributions aggregated into this rule breakdown group. Empty when the run  genuinely produced no contributions; a run with no recorded breakdown (e.g. one that predates  this feature) returns a 404 rather than this response. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ComplianceRuleBreakdownWithContributions import ComplianceRuleBreakdownWithContributions

instance = ComplianceRuleBreakdownWithContributions(
    group_status="...",  # required — The status of this subset of results.
    results_used=,  # required — Dictionary of AddressKey (as string) and their corresponding decimal values, that were used in this rule.
    properties_used=,  # required — Dictionary of PropertyKey (as string) and their corresponding Properties, that were used in this rule
    missing_data_information=,  # required — List of string information detailing data that was missing from contributions processed in this rule
    lineage=[],  # required
    contributions=[]  # required — The per-position contributions aggregated into this rule breakdown group. Empty when the run  genuinely produced no contributions; a run with no recorded breakdown (e.g. one that predates  this feature) returns a 404 rather than this response.
)
```

- [LineageMember](LineageMember.md)
- [ComplianceRuleContribution](ComplianceRuleContribution.md) — used in `contributions`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

