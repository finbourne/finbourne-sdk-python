# BackgroundQueryCancelResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **had_data** | **bool** | Optional | *No description available.* |
| **previous_status** | [TaskStatus](TaskStatus.md) | Optional | *No description available.* |
| **previous_state** | [BackgroundQueryState](BackgroundQueryState.md) | Optional | *No description available.* |
| **progress** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.luminesce.models.BackgroundQueryCancelResponse import BackgroundQueryCancelResponse

instance = BackgroundQueryCancelResponse(
    had_data=True,  # optional
    previous_status=TaskStatus(...),  # optional
    previous_state=BackgroundQueryState(...),  # optional
    progress="..."  # optional
)
```

- [TaskStatus](TaskStatus.md)
- [BackgroundQueryState](BackgroundQueryState.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

