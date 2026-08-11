# BackgroundQueryProgressResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **has_data** | **bool** | Optional | Is there currently data for this Query? |
| **row_count** | **int** | Optional | Number of rows of data held. -1 if none as yet. |
| **status** | [TaskStatus](TaskStatus.md) | Optional | *No description available.* |
| **state** | [BackgroundQueryState](BackgroundQueryState.md) | Optional | *No description available.* |
| **progress** | **str** | Optional | The full progress log (up to this point at least) |
| **feedback** | [List[FeedbackEventArgs]](FeedbackEventArgs.md) | Optional | Individual Feedback Messages (to replace Progress).  A given message will be returned from only one call. |
| **query** | **str** | Optional | The LuminesceSql of the original request |
| **query_name** | **str** | Optional | The QueryName given in the original request |
| **columns_available** | [List[Column]](Column.md) | Optional | When HasData is true this is the schema of columns that will be returned if the data is requested |
| **lineage** | [TableLineage](TableLineage.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.BackgroundQueryProgressResponse import BackgroundQueryProgressResponse

instance = BackgroundQueryProgressResponse(
    has_data=True,  # optional — Is there currently data for this Query?
    row_count=0,  # optional — Number of rows of data held. -1 if none as yet.
    status=TaskStatus(...),  # optional
    state=BackgroundQueryState(...),  # optional
    progress="...",  # optional — The full progress log (up to this point at least)
    feedback=[],  # optional — Individual Feedback Messages (to replace Progress).  A given message will be returned from only one call.
    query="...",  # optional — The LuminesceSql of the original request
    query_name="...",  # optional — The QueryName given in the original request
    columns_available=[],  # optional — When HasData is true this is the schema of columns that will be returned if the data is requested
    lineage=TableLineage(...)  # optional
)
```

- [TaskStatus](TaskStatus.md)
- [BackgroundQueryState](BackgroundQueryState.md)
- [FeedbackEventArgs](FeedbackEventArgs.md) — used in `feedback`
- [Column](Column.md) — used in `columns_available`
- [TableLineage](TableLineage.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

