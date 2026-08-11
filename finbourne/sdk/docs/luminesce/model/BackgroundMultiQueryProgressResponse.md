# BackgroundMultiQueryProgressResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **progress** | **str** | Optional | The full progress log (up to this point at least) |
| **feedback** | [List[FeedbackEventArgs]](FeedbackEventArgs.md) | Optional | Individual Feedback Messages (to replace Progress).  A given message will be returned from only one call. |
| **status** | [TaskStatus](TaskStatus.md) | Optional | *No description available.* |
| **queries** | [List[BackgroundQueryProgressResponse]](BackgroundQueryProgressResponse.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.BackgroundMultiQueryProgressResponse import BackgroundMultiQueryProgressResponse

instance = BackgroundMultiQueryProgressResponse(
    progress="...",  # optional — The full progress log (up to this point at least)
    feedback=[],  # optional — Individual Feedback Messages (to replace Progress).  A given message will be returned from only one call.
    status=TaskStatus(...),  # optional
    queries=[]  # optional
)
```

- [FeedbackEventArgs](FeedbackEventArgs.md) — used in `feedback`
- [TaskStatus](TaskStatus.md)
- [BackgroundQueryProgressResponse](BackgroundQueryProgressResponse.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

