# ComplianceBreachedOrderInfo

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **order_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **list_rule_result** | [List[ComplianceRuleResult]](ComplianceRuleResult.md) | Required | The Rule Results for a particular compliance run |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ComplianceBreachedOrderInfo import ComplianceBreachedOrderInfo

instance = ComplianceBreachedOrderInfo(
    order_id=ResourceId(...),  # required
    list_rule_result=[]  # required — The Rule Results for a particular compliance run
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ComplianceRuleResult](ComplianceRuleResult.md) — used in `list_rule_result`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

