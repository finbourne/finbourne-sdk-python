# WorkflowRunResultResponse

A single declared field and the value this run published for it.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Required | *No description available.* |
| **type** | **str** | Required | One of the Workflow field types: String, Decimal, DateTime, Boolean, LusidUserId. |
| **value** | **str** | Optional | The published value, or null when the run published nothing for this field. |
| **display_name** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.WorkflowRunResultResponse import WorkflowRunResultResponse

instance = WorkflowRunResultResponse(
    name="...",  # required
    type="...",  # required — One of the Workflow field types: String, Decimal, DateTime, Boolean, LusidUserId.
    value="...",  # optional — The published value, or null when the run published nothing for this field.
    display_name="..."  # optional
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

