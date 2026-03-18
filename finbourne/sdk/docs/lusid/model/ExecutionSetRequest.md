# ExecutionSetRequest

A request to create or update multiple Executions.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **requests** | [List[ExecutionRequest]](ExecutionRequest.md) | Optional | A collection of ExecutionRequests. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ExecutionSetRequest import ExecutionSetRequest

instance = ExecutionSetRequest(
    requests=[]  # optional — A collection of ExecutionRequests.
)
```


## Related Models

- [ExecutionRequest](ExecutionRequest.md) — used in `requests`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

