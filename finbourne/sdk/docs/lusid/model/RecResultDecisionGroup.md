# RecResultDecisionGroup

The group-decision detail carried on every member of a FixAsGroup or ForceMatch decision.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **group_number** | **int** | Required | Server-allocated, monotonic group number, unique within the RecResultSet and never reused. |
| **core_rules_excused** | **List[str]** | Optional | The ruleNames of the core rules excused by a ForceMatch. Identical on every group member; non-null only for ForceMatch. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecResultDecisionGroup import RecResultDecisionGroup

instance = RecResultDecisionGroup(
    group_number=0,  # required — Server-allocated, monotonic group number, unique within the RecResultSet and never reused.
    core_rules_excused=  # optional — The ruleNames of the core rules excused by a ForceMatch. Identical on every group member; non-null only for ForceMatch.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

