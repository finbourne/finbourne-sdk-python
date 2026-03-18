# DecoratedComplianceRunSummary

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **run_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **details** | [List[ComplianceRuleResultDetail]](ComplianceRuleResultDetail.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.DecoratedComplianceRunSummary import DecoratedComplianceRunSummary

instance = DecoratedComplianceRunSummary(
    run_id=ResourceId(...),  # required
    details=[]  # required
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ComplianceRuleResultDetail](ComplianceRuleResultDetail.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

