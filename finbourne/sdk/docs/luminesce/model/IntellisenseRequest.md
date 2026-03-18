# IntellisenseRequest

Representation of a request for IntellisenseItems
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **lines** | **List[str]** | Required | The lines of text the user currently has in the editor |
| **position** | [CursorPosition](CursorPosition.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.IntellisenseRequest import IntellisenseRequest

instance = IntellisenseRequest(
    lines=,  # required — The lines of text the user currently has in the editor
    position=CursorPosition(...)  # required
)
```

- [CursorPosition](CursorPosition.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

