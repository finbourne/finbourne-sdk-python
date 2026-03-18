# BatchUpdateTasksResponse

Defines a representation of tasks that have been updated
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **values** | [List[Task]](Task.md) | Optional | Successful tasks brought back from the BatchUpdate call *(read-only)* |
| **failed** | [List[ErrorDetail]](ErrorDetail.md) | Optional | Individual failures for each task returned from the BatchUpdate call *(read-only)* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.BatchUpdateTasksResponse import BatchUpdateTasksResponse

instance = BatchUpdateTasksResponse(
    values=[],  # optional — Successful tasks brought back from the BatchUpdate call
    failed=[],  # optional — Individual failures for each task returned from the BatchUpdate call
    links=[]  # optional
)
```


## Related Models

- [Task](Task.md) — used in `values`
- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

