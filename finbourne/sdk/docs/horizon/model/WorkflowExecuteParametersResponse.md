# WorkflowExecuteParametersResponse

The execute parameters a Workflow-driven integration instance accepts on executewithparams.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instance_id** | **str** | Required | The instance these parameters belong to. |
| **integration_type** | **str** | Required | The integration type of the instance, e.g. ta-tax-processes. |
| **parameters** | [List[WorkflowExecuteParameterResponse]](WorkflowExecuteParameterResponse.md) | Required | Every parameter the integration accepts, each listed once. |
| **stages** | [List[WorkflowExecuteStageResponse]](WorkflowExecuteStageResponse.md) | Required | Per-stage breakdown of the steps that run and the parameters accepted. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.WorkflowExecuteParametersResponse import WorkflowExecuteParametersResponse

instance = WorkflowExecuteParametersResponse(
    instance_id="...",  # required — The instance these parameters belong to.
    integration_type="...",  # required — The integration type of the instance, e.g. ta-tax-processes.
    parameters=[],  # required — Every parameter the integration accepts, each listed once.
    stages=[]  # required — Per-stage breakdown of the steps that run and the parameters accepted.
)
```

- [WorkflowExecuteParameterResponse](WorkflowExecuteParameterResponse.md) — used in `parameters`
- [WorkflowExecuteStageResponse](WorkflowExecuteStageResponse.md) — used in `stages`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

