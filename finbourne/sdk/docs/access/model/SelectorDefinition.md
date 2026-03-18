# SelectorDefinition

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **metadata_selector_definition** | [MetadataSelectorDefinition](MetadataSelectorDefinition.md) | Optional | *No description available.* |
| **id_selector_definition** | [IdSelectorDefinition](IdSelectorDefinition.md) | Optional | *No description available.* |
| **match_all_selector_definition** | [MatchAllSelectorDefinition](MatchAllSelectorDefinition.md) | Optional | *No description available.* |
| **policy_selector_definition** | [PolicySelectorDefinition](PolicySelectorDefinition.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.access.models.SelectorDefinition import SelectorDefinition

instance = SelectorDefinition(
    metadata_selector_definition=MetadataSelectorDefinition(...),  # optional
    id_selector_definition=IdSelectorDefinition(...),  # optional
    match_all_selector_definition=MatchAllSelectorDefinition(...),  # optional
    policy_selector_definition=PolicySelectorDefinition(...)  # optional
)
```


## Related Models

- [MetadataSelectorDefinition](MetadataSelectorDefinition.md)
- [IdSelectorDefinition](IdSelectorDefinition.md)
- [MatchAllSelectorDefinition](MatchAllSelectorDefinition.md)
- [PolicySelectorDefinition](PolicySelectorDefinition.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

