# RecombineStep

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **label** | **str** | Required | The label of the compliance step |
| **parameters** | [List[ComplianceTemplateParameter]](ComplianceTemplateParameter.md) | Required | Parameters required for the step |
| **compliance_step_type** | **str** | Required | . The available values are: FilterStep, GroupByStep, GroupFilterStep, BranchStep, RecombineStep, CheckStep, PercentCheckStep |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RecombineStep import RecombineStep

instance = RecombineStep(
    label="...",  # required — The label of the compliance step
    parameters=[],  # required — Parameters required for the step
    compliance_step_type="..."  # required — . The available values are: FilterStep, GroupByStep, GroupFilterStep, BranchStep, RecombineStep, CheckStep, PercentCheckStep
)
```

- [ComplianceTemplateParameter](ComplianceTemplateParameter.md) — used in `parameters`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

