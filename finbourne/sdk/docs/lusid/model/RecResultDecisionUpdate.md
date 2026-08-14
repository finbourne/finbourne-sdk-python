# RecResultDecisionUpdate

The decision update within a batch review item. Omitting the object leaves the existing decision  untouched; a null value nullifies it (dissolving any group).
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **value** | **str** | Optional | The decision value. Null nullifies the decision. Available values: Acknowledge, FixAtSource, FixAsGroup, Accept, ForceMatch, Tolerate. |
| **affirm** | **bool** | Optional | Whether to affirm an existing decision (e.g. after revisions were requested). |
| **core_rules_excused** | **List[str]** | Optional | The ruleNames of the core rules excused by a ForceMatch. Identical on every group member; non-null only for ForceMatch. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecResultDecisionUpdate import RecResultDecisionUpdate

instance = RecResultDecisionUpdate(
    value="...",  # optional — The decision value. Null nullifies the decision. Available values: Acknowledge, FixAtSource, FixAsGroup, Accept, ForceMatch, Tolerate.
    affirm=True,  # optional — Whether to affirm an existing decision (e.g. after revisions were requested).
    core_rules_excused=  # optional — The ruleNames of the core rules excused by a ForceMatch. Identical on every group member; non-null only for ForceMatch.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

