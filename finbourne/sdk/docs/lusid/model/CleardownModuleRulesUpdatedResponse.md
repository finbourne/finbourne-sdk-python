# CleardownModuleRulesUpdatedResponse

A Cleardown Module rules update response
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **rules** | [List[CleardownModuleRule]](CleardownModuleRule.md) | Optional | The Cleardown Rules that apply for the Cleardown Module. Rules are evaluated in the order they occur in this collection. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CleardownModuleRulesUpdatedResponse import CleardownModuleRulesUpdatedResponse

instance = CleardownModuleRulesUpdatedResponse(
    rules=[],  # optional — The Cleardown Rules that apply for the Cleardown Module. Rules are evaluated in the order they occur in this collection.
    version=Version(...),  # optional
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    links=[]  # optional
)
```


## Related Models

- [CleardownModuleRule](CleardownModuleRule.md) — used in `rules`
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

