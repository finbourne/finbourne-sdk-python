# HorizonIntegration

Configuration for a Worker that executes a Horizon integration instance
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Required | The type of worker |
| **integration_instance_id** | **str** | Required | The id of the Horizon integration instance the worker executes. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.workflow.models.HorizonIntegration import HorizonIntegration

instance = HorizonIntegration(
    type="...",  # required — The type of worker
    integration_instance_id="..."  # required — The id of the Horizon integration instance the worker executes.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

