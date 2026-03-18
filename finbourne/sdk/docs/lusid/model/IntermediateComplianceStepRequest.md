# IntermediateComplianceStepRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **label** | **str** | Required | The label of the compliance step |
| **compliance_step_type_request** | **str** | Required | . The available values are: FilterStepRequest, GroupByStepRequest, GroupFilterStepRequest, BranchStepRequest, CheckStepRequest, PercentCheckStepRequest |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.IntermediateComplianceStepRequest import IntermediateComplianceStepRequest

instance = IntermediateComplianceStepRequest(
    label="...",  # required — The label of the compliance step
    compliance_step_type_request="..."  # required — . The available values are: FilterStepRequest, GroupByStepRequest, GroupFilterStepRequest, BranchStepRequest, CheckStepRequest, PercentCheckStepRequest
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

