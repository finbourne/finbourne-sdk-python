# ComplianceRuleBreakdownRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **group_status** | **str** | Required | *No description available.* |
| **results_used** | **Dict[str, float]** | Required | *No description available.* |
| **properties_used** | **Dict[str, Optional[List[ModelProperty]]]** | Required | *No description available.* |
| **missing_data_information** | **List[str]** | Required | *No description available.* |
| **lineage** | [List[LineageMember]](LineageMember.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ComplianceRuleBreakdownRequest import ComplianceRuleBreakdownRequest

instance = ComplianceRuleBreakdownRequest(
    group_status="...",  # required
    results_used=,  # required
    properties_used=,  # required
    missing_data_information=,  # required
    lineage=[]  # required
)
```

- [LineageMember](LineageMember.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

