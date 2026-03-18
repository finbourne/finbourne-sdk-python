# UpsertComplianceRuleRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **name** | **str** | Optional | *No description available.* |
| **description** | **str** | Optional | *No description available.* |
| **active** | **bool** | Required | *No description available.* |
| **template_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **variation** | **str** | Required | *No description available.* |
| **portfolio_group_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **parameters** | [Dict[str, ComplianceParameter]](ComplianceParameter.md) | Required | *No description available.* |
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Required | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertComplianceRuleRequest import UpsertComplianceRuleRequest

instance = UpsertComplianceRuleRequest(
    id=ResourceId(...),  # required
    name="...",  # optional
    description="...",  # optional
    active=True,  # required
    template_id=ResourceId(...),  # required
    variation="...",  # required
    portfolio_group_id=ResourceId(...),  # required
    parameters=ComplianceParameter(...),  # required
    properties=PerpetualProperty(...)  # required
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ComplianceParameter](ComplianceParameter.md)
- [PerpetualProperty](PerpetualProperty.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

