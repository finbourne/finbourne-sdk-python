# WorkflowResultFieldResponse

A single declared field.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Required | *No description available.* |
| **type** | **str** | Required | One of the Workflow field types: String, Decimal, DateTime, Boolean, LusidUserId. |
| **display_name** | **str** | Optional | *No description available.* |
| **description** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.WorkflowResultFieldResponse import WorkflowResultFieldResponse

instance = WorkflowResultFieldResponse(
    name="...",  # required
    type="...",  # required — One of the Workflow field types: String, Decimal, DateTime, Boolean, LusidUserId.
    display_name="...",  # optional
    description="..."  # optional
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

