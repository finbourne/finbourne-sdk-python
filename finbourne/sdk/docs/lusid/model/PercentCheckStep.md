# PercentCheckStep

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **label** | **str** | Required | The label of the compliance step |
| **limit_check_parameters** | [List[ComplianceTemplateParameter]](ComplianceTemplateParameter.md) | Required | Parameters required for an absolute limit check |
| **warning_check_parameters** | [List[ComplianceTemplateParameter]](ComplianceTemplateParameter.md) | Required | Parameters required for a warning limit check |
| **compliance_step_type** | **str** | Required | . The available values are: FilterStep, GroupByStep, GroupFilterStep, BranchStep, RecombineStep, CheckStep, PercentCheckStep |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PercentCheckStep import PercentCheckStep

instance = PercentCheckStep(
    label="...",  # required — The label of the compliance step
    limit_check_parameters=[],  # required — Parameters required for an absolute limit check
    warning_check_parameters=[],  # required — Parameters required for a warning limit check
    compliance_step_type="..."  # required — . The available values are: FilterStep, GroupByStep, GroupFilterStep, BranchStep, RecombineStep, CheckStep, PercentCheckStep
)
```

- [ComplianceTemplateParameter](ComplianceTemplateParameter.md) — used in `limit_check_parameters`
- [ComplianceTemplateParameter](ComplianceTemplateParameter.md) — used in `warning_check_parameters`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

