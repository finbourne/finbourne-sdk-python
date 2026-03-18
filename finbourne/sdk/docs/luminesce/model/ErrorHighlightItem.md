# ErrorHighlightItem

Representation of a sql error
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **start** | [CursorPosition](CursorPosition.md) | Required | *No description available.* |
| **stop** | [CursorPosition](CursorPosition.md) | Required | *No description available.* |
| **no_viable_alternative_start** | [CursorPosition](CursorPosition.md) | Optional | *No description available.* |
| **length** | **int** | Required | The length of the error token counting line breaks if any |
| **message** | **str** | Required | The error message |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.ErrorHighlightItem import ErrorHighlightItem

instance = ErrorHighlightItem(
    start=CursorPosition(...),  # required
    stop=CursorPosition(...),  # required
    no_viable_alternative_start=CursorPosition(...),  # optional
    length=0,  # required — The length of the error token counting line breaks if any
    message="..."  # required — The error message
)
```


## Related Models

- [CursorPosition](CursorPosition.md)
- [CursorPosition](CursorPosition.md)
- [CursorPosition](CursorPosition.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

