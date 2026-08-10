# GetScenarioResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | *No description available.* |
| **value** | [../model/ScenarioDefinition](ScenarioDefinition.md) | Optional | *No description available.* |
| **version** | [../model/Version](Version.md) | Optional | *No description available.* |
| **failed** | [../model/ErrorDetail](ErrorDetail.md) | Optional | *No description available.* |
| **links** | [../model/List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.GetScenarioResponse import GetScenarioResponse

instance = GetScenarioResponse(
    href="...",  # optional
    value=ScenarioDefinition(...),  # optional
    version=Version(...),  # optional
    failed=ErrorDetail(...),  # optional
    links=[]  # optional
)
```

- [ScenarioDefinition](ScenarioDefinition.md)
- [Version](Version.md)
- [ErrorDetail](ErrorDetail.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

