# IntellisenseResponse

Available intellisense response information
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **auto_complete_list** | [List[IntellisenseItem]](IntellisenseItem.md) | Required | The available items at this point |
| **try_again_soon_for_more** | **bool** | Required | Should the caller try again soon? (true means a cache is being built and this is a preliminary response!) |
| **sql_with_marker** | **str** | Required | The SQL this is for with characters indicating the location the pop-up is for |
| **start_replacement_position** | [CursorPosition](CursorPosition.md) | Required | *No description available.* |
| **end_replacement_position** | [CursorPosition](CursorPosition.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.IntellisenseResponse import IntellisenseResponse

instance = IntellisenseResponse(
    auto_complete_list=[],  # required — The available items at this point
    try_again_soon_for_more=True,  # required — Should the caller try again soon? (true means a cache is being built and this is a preliminary response!)
    sql_with_marker="...",  # required — The SQL this is for with characters indicating the location the pop-up is for
    start_replacement_position=CursorPosition(...),  # required
    end_replacement_position=CursorPosition(...)  # required
)
```


## Related Models

- [IntellisenseItem](IntellisenseItem.md) — used in `auto_complete_list`
- [CursorPosition](CursorPosition.md)
- [CursorPosition](CursorPosition.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

