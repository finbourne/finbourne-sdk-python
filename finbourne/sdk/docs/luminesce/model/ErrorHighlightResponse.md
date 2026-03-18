# ErrorHighlightResponse

Response for error highlighting
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **errors** | [List[ErrorHighlightItem]](ErrorHighlightItem.md) | Required | The errors within the Sql |
| **sql_with_marker** | **str** | Required | The SQL this is for, with characters indicating the error locations |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.ErrorHighlightResponse import ErrorHighlightResponse

instance = ErrorHighlightResponse(
    errors=[],  # required — The errors within the Sql
    sql_with_marker="..."  # required — The SQL this is for, with characters indicating the error locations
)
```


## Related Models

- [ErrorHighlightItem](ErrorHighlightItem.md) — used in `errors`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

