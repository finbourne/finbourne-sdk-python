# WorkflowResultFieldsTaskResponse

One of the instance's enabled RunWorkflow post-process tasks.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Required | *No description available.* |
| **trigger_on** | **str** | Required | When this task fires: OnSuccess, OnFailure or Always. |
| **result_fields** | **List[str]** | Required | Names of the fields this particular task declares. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.WorkflowResultFieldsTaskResponse import WorkflowResultFieldsTaskResponse

instance = WorkflowResultFieldsTaskResponse(
    name="...",  # required
    trigger_on="...",  # required — When this task fires: OnSuccess, OnFailure or Always.
    result_fields=  # required — Names of the fields this particular task declares.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

