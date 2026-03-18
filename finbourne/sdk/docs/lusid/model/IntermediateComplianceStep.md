# IntermediateComplianceStep

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **label** | **str** | Required | The label of the compliance step |
| **grouped_parameters** | **Dict[str, Optional[List[ComplianceTemplateParameter]]]** | Required | Parameters required for the step |
| **compliance_step_type** | **str** | Required | . The available values are: FilterStep, GroupByStep, GroupFilterStep, BranchStep, RecombineStep, CheckStep, PercentCheckStep |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.IntermediateComplianceStep import IntermediateComplianceStep

instance = IntermediateComplianceStep(
    label="...",  # required — The label of the compliance step
    grouped_parameters=,  # required — Parameters required for the step
    compliance_step_type="..."  # required — . The available values are: FilterStep, GroupByStep, GroupFilterStep, BranchStep, RecombineStep, CheckStep, PercentCheckStep
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

