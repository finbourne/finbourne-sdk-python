# ComplianceRuleResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **name** | **str** | Optional | *No description available.* |
| **description** | **str** | Optional | *No description available.* |
| **active** | **bool** | Optional | *No description available.* |
| **template_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **variation** | **str** | Optional | *No description available.* |
| **portfolio_group_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **parameters** | [Dict[str, ComplianceParameter]](ComplianceParameter.md) | Optional | *No description available.* |
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | *No description available.* |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ComplianceRuleResponse import ComplianceRuleResponse

instance = ComplianceRuleResponse(
    id=ResourceId(...),  # optional
    name="...",  # optional
    description="...",  # optional
    active=True,  # optional
    template_id=ResourceId(...),  # optional
    variation="...",  # optional
    portfolio_group_id=ResourceId(...),  # optional
    parameters=ComplianceParameter(...),  # optional
    properties=PerpetualProperty(...),  # optional
    version=Version(...),  # optional
    links=[]  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ComplianceParameter](ComplianceParameter.md)
- [PerpetualProperty](PerpetualProperty.md)
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

