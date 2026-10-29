# CustomMultiQueryListItem

A custom multi-query the calling user currently has results of available to them
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **execution_id** | **str** | Optional | ExecutionId of the multi-query, its queries having ExecutionIds of &#x60;{ExecutionId}_{Name}&#x60; |
| **query_name** | **str** | Optional | The QueryName given in the original request |
| **state** | [BackgroundQueryState](BackgroundQueryState.md) | Optional | *No description available.* |
| **started_at** | **datetime** | Optional | When it was started (UTC) |
| **when** | **datetime** | Optional | When the state of it was last updated (UTC) |
| **expires_at** | **datetime** | Optional | When it (and the data of its queries) may be removed (UTC) |
| **exported_to** | **str** | Optional | The Drive path its results were saved to once done, if it was started with an &#x60;export&#x60; and they were |
| **queries** | [List[CustomMultiQueryListItemQuery]](CustomMultiQueryListItemQuery.md) | Optional | Its queries whose results may be fetched (those that are external results), in request order |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.CustomMultiQueryListItem import CustomMultiQueryListItem

instance = CustomMultiQueryListItem(
    execution_id="...",  # optional — ExecutionId of the multi-query, its queries having ExecutionIds of &#x60;{ExecutionId}_{Name}&#x60;
    query_name="...",  # optional — The QueryName given in the original request
    state=BackgroundQueryState(...),  # optional
    started_at=datetime.now(),  # optional — When it was started (UTC)
    when=datetime.now(),  # optional — When the state of it was last updated (UTC)
    expires_at=datetime.now(),  # optional — When it (and the data of its queries) may be removed (UTC)
    exported_to="...",  # optional — The Drive path its results were saved to once done, if it was started with an &#x60;export&#x60; and they were
    queries=[]  # optional — Its queries whose results may be fetched (those that are external results), in request order
)
```

- [BackgroundQueryState](BackgroundQueryState.md)
- [CustomMultiQueryListItemQuery](CustomMultiQueryListItemQuery.md) — used in `queries`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

