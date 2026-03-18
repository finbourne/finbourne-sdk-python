# IdSelectorDefinition

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **identifier** | **Dict[str, Optional[str]]** | Required | *No description available.* |
| **actions** | [List[ActionId]](ActionId.md) | Required | *No description available.* |
| **name** | **str** | Optional | *No description available.* |
| **description** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.access.models.IdSelectorDefinition import IdSelectorDefinition

instance = IdSelectorDefinition(
    identifier=,  # required
    actions=[],  # required
    name="...",  # optional
    description="..."  # optional
)
```

- [ActionId](ActionId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

