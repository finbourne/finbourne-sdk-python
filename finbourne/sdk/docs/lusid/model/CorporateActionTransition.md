# CorporateActionTransition

A 'transition' within a corporate action, representing a set of output movements paired to a single input position
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **input_transition** | [CorporateActionTransitionComponent](CorporateActionTransitionComponent.md) | Optional | *No description available.* |
| **output_transitions** | [List[CorporateActionTransitionComponent]](CorporateActionTransitionComponent.md) | Optional | What will be generated relative to the input transition |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CorporateActionTransition import CorporateActionTransition

instance = CorporateActionTransition(
    input_transition=CorporateActionTransitionComponent(...),  # optional
    output_transitions=[]  # optional — What will be generated relative to the input transition
)
```


## Related Models

- [CorporateActionTransitionComponent](CorporateActionTransitionComponent.md)
- [CorporateActionTransitionComponent](CorporateActionTransitionComponent.md) — used in `output_transitions`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

