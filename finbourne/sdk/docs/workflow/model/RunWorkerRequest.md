# RunWorkerRequest

Request to Create a new worker
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **parameters** | [List[ParameterValue]](ParameterValue.md) | Required | The Parameter and their values. |
| **worker_timeout** | **int** | Optional | The timeout in seconds for the worker |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.RunWorkerRequest import RunWorkerRequest

instance = RunWorkerRequest(
    parameters=[],  # required — The Parameter and their values.
    worker_timeout=0  # optional — The timeout in seconds for the worker
)
```


## Related Models

- [ParameterValue](ParameterValue.md) — used in `parameters`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

