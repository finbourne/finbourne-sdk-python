# RecResultReview

The per-result review axis: the workflow state and the recorded review decision. Always present,  including on Match and Cross.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **status** | **str** | Required | The review workflow state: NotRequired, Required or Reviewed. Available values: NotRequired, Required, Reviewed. |
| **decision** | **str** | Optional | The recorded review decision. Null until a decision is made. Available values: Acknowledge, FixAtSource, FixAsGroup, Accept, ForceMatch, Tolerate. |
| **decision_group** | [RecResultDecisionGroup](RecResultDecisionGroup.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecResultReview import RecResultReview

instance = RecResultReview(
    status="...",  # required — The review workflow state: NotRequired, Required or Reviewed. Available values: NotRequired, Required, Reviewed.
    decision="...",  # optional — The recorded review decision. Null until a decision is made. Available values: Acknowledge, FixAtSource, FixAsGroup, Accept, ForceMatch, Tolerate.
    decision_group=RecResultDecisionGroup(...)  # optional
)
```

- [RecResultDecisionGroup](RecResultDecisionGroup.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

