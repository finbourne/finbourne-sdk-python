# UpdateWorkerRequest

Request to Update a new worker
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **display_name** | **str** | Required | Human readable name |
| **description** | **str** | Optional | Human readable description |
| **worker_configuration** | **object** | Required | Information about how the worker should be executed |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.UpdateWorkerRequest import UpdateWorkerRequest

instance = UpdateWorkerRequest(
    display_name="...",  # required — Human readable name
    description="...",  # optional — Human readable description
    worker_configuration=  # required — Information about how the worker should be executed
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

