# ErrorHighlightRequest

Request for Error highlighting
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **lines** | **List[str]** | Required | The lines of text the user currently has in the editor |
| **ensure_some_text_is_selected** | **bool** | Optional | If an editor requires some selection of non-whitespace this can be set to true to force at least one visible character to be selected. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.ErrorHighlightRequest import ErrorHighlightRequest

instance = ErrorHighlightRequest(
    lines=,  # required — The lines of text the user currently has in the editor
    ensure_some_text_is_selected=True  # optional — If an editor requires some selection of non-whitespace this can be set to true to force at least one visible character to be selected.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

