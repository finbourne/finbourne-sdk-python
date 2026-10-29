# WorkflowExecuteParameterResponse

A single execute parameter.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Required | *No description available.* |
| **type** | **str** | Required | One of the Workflow field types: String, Decimal, DateTime, Boolean. |
| **required** | **bool** | Required | Whether every run must supply the parameter, whatever its stage. |
| **display_name** | **str** | Required | *No description available.* |
| **description** | **str** | Required | *No description available.* |
| **format** | **str** | Optional | The shape a String value must take, e.g. YYYY-MM, when it has one. |
| **allowed_values** | **List[str]** | Optional | The closed set of accepted values, when there is one. |
| **required_for_stages** | **List[str]** | Required | The stages for which the parameter is mandatory. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.horizon.models.WorkflowExecuteParameterResponse import WorkflowExecuteParameterResponse

instance = WorkflowExecuteParameterResponse(
    name="...",  # required
    type="...",  # required — One of the Workflow field types: String, Decimal, DateTime, Boolean.
    required=True,  # required — Whether every run must supply the parameter, whatever its stage.
    display_name="...",  # required
    description="...",  # required
    format="...",  # optional — The shape a String value must take, e.g. YYYY-MM, when it has one.
    allowed_values=,  # optional — The closed set of accepted values, when there is one.
    required_for_stages=  # required — The stages for which the parameter is mandatory.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

