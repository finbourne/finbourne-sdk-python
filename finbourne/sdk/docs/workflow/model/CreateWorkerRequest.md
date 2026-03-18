# CreateWorkerRequest

Request to Create a new worker
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **display_name** | **str** | Required | Human readable name |
| **description** | **str** | Optional | Human readable description |
| **worker_configuration** | [WorkerConfiguration](WorkerConfiguration.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.CreateWorkerRequest import CreateWorkerRequest

instance = CreateWorkerRequest(
    id=ResourceId(...),  # required
    display_name="...",  # required — Human readable name
    description="...",  # optional — Human readable description
    worker_configuration=WorkerConfiguration(...)  # required
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [WorkerConfiguration](WorkerConfiguration.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

