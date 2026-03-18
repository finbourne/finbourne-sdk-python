# CorporateActionTransitionRequest

A 'transition' within a corporate action, representing a set of output movements paired to a single input position
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **input_transition** | [CorporateActionTransitionComponentRequest](CorporateActionTransitionComponentRequest.md) | Optional | *No description available.* |
| **output_transitions** | [List[CorporateActionTransitionComponentRequest]](CorporateActionTransitionComponentRequest.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CorporateActionTransitionRequest import CorporateActionTransitionRequest

instance = CorporateActionTransitionRequest(
    input_transition=CorporateActionTransitionComponentRequest(...),  # optional
    output_transitions=[]  # optional
)
```


## Related Models

- [CorporateActionTransitionComponentRequest](CorporateActionTransitionComponentRequest.md)
- [CorporateActionTransitionComponentRequest](CorporateActionTransitionComponentRequest.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

