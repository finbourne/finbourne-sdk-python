# PolicySelectorDefinition

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **identity_restriction** | **Dict[str, Optional[str]]** | Optional | *No description available.* |
| **restriction_selectors** | [List[SelectorDefinition]](SelectorDefinition.md) | Optional | *No description available.* |
| **actions** | [List[ActionId]](ActionId.md) | Required | *No description available.* |
| **name** | **str** | Optional | *No description available.* |
| **description** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.access.models.PolicySelectorDefinition import PolicySelectorDefinition

instance = PolicySelectorDefinition(
    identity_restriction=,  # optional
    restriction_selectors=[],  # optional
    actions=[],  # required
    name="...",  # optional
    description="..."  # optional
)
```

- [SelectorDefinition](SelectorDefinition.md)
- [ActionId](ActionId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

