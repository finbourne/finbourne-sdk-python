# BackgroundQueryListItem

A background query the calling user currently has available to them
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **execution_id** | **str** | Optional | ExecutionId of the query |
| **query** | **str** | Optional | The LuminesceSql of the original request |
| **query_name** | **str** | Optional | The QueryName given in the original request |
| **state** | [BackgroundQueryState](BackgroundQueryState.md) | Optional | *No description available.* |
| **when** | **datetime** | Optional | When the state of this query (and so its data) was last updated (UTC) |
| **expires_at** | **datetime** | Optional | When the query (and its data) may be removed (UTC) |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.BackgroundQueryListItem import BackgroundQueryListItem

instance = BackgroundQueryListItem(
    execution_id="...",  # optional — ExecutionId of the query
    query="...",  # optional — The LuminesceSql of the original request
    query_name="...",  # optional — The QueryName given in the original request
    state=BackgroundQueryState(...),  # optional
    when=datetime.now(),  # optional — When the state of this query (and so its data) was last updated (UTC)
    expires_at=datetime.now()  # optional — When the query (and its data) may be removed (UTC)
)
```

- [BackgroundQueryState](BackgroundQueryState.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

