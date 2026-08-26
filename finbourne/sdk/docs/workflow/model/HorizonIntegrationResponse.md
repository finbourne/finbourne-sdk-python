# HorizonIntegrationResponse

Readonly configuration for the Horizon Integration Worker
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Optional | The type of worker |
| **integration_instance_id** | **str** | Optional | The id of the Horizon integration instance the worker executes. Null on the library worker. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.HorizonIntegrationResponse import HorizonIntegrationResponse

instance = HorizonIntegrationResponse(
    type="...",  # optional — The type of worker
    integration_instance_id="..."  # optional — The id of the Horizon integration instance the worker executes. Null on the library worker.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

