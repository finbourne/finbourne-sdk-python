# RecInstanceId

Identifies a rec instance, and how it was created.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instance_id_type** | **str** | Required | How the instance was created. Available values: WorkflowServiceTaskId, Manual. |
| **instance_id_value** | **str** | Required | The instance identifier value (a GUID). |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecInstanceId import RecInstanceId

instance = RecInstanceId(
    instance_id_type="...",  # required — How the instance was created. Available values: WorkflowServiceTaskId, Manual.
    instance_id_value="..."  # required — The instance identifier value (a GUID).
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

