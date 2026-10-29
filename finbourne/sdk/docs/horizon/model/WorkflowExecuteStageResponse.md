# WorkflowExecuteStageResponse

One stage of a staged integration.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Required | *No description available.* |
| **steps** | **List[str]** | Required | The steps that run for this stage. |
| **parameters** | **List[str]** | Required | Names of every parameter this stage accepts. |
| **rules** | **List[str]** | Required | Cross-field rules the stage enforces, in plain text. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.WorkflowExecuteStageResponse import WorkflowExecuteStageResponse

instance = WorkflowExecuteStageResponse(
    name="...",  # required
    steps=,  # required — The steps that run for this stage.
    parameters=,  # required — Names of every parameter this stage accepts.
    rules=  # required — Cross-field rules the stage enforces, in plain text.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

