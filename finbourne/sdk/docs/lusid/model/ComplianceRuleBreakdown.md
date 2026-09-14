# ComplianceRuleBreakdown

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **group_status** | **str** | Required | The status of this subset of results. |
| **results_used** | **Dict[str, float]** | Required | Dictionary of AddressKey (as string) and their corresponding decimal values, that were used in this rule. |
| **formula_values** | **Dict[str, float]** | Optional | The value each formula within the check criterion evaluated to for this group. Empty where the criterion  compares a single value or is not numerical, since the operand values already recorded describe those. |
| **properties_used** | **Dict[str, Optional[List[ModelProperty]]]** | Required | Dictionary of PropertyKey (as string) and their corresponding Properties, that were used in this rule |
| **missing_data_information** | **List[str]** | Required | List of string information detailing data that was missing from contributions processed in this rule |
| **lineage** | [List[LineageMember]](LineageMember.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ComplianceRuleBreakdown import ComplianceRuleBreakdown

instance = ComplianceRuleBreakdown(
    group_status="...",  # required — The status of this subset of results.
    results_used=,  # required — Dictionary of AddressKey (as string) and their corresponding decimal values, that were used in this rule.
    formula_values=,  # optional — The value each formula within the check criterion evaluated to for this group. Empty where the criterion  compares a single value or is not numerical, since the operand values already recorded describe those.
    properties_used=,  # required — Dictionary of PropertyKey (as string) and their corresponding Properties, that were used in this rule
    missing_data_information=,  # required — List of string information detailing data that was missing from contributions processed in this rule
    lineage=[]  # required
)
```

- [LineageMember](LineageMember.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

