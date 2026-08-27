# GetScenarioResponse

The response to a singular scenario read. There is deliberately no failure block on this  type: every route returning it is a singular (or list-of-singular) read, never a batch keyed  lookup, so there is no per-key error to report - an invalid entity is rejected at upsert and  a failed read fails the whole request. The IGetResponse batch members below throw for the  same reason; do not reintroduce a Failed property when copying this shape.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | *No description available.* |
| **value** | [ScenarioDefinition](ScenarioDefinition.md) | Optional | *No description available.* |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.GetScenarioResponse import GetScenarioResponse

instance = GetScenarioResponse(
    href="...",  # optional
    value=ScenarioDefinition(...),  # optional
    version=Version(...),  # optional
    links=[]  # optional
)
```

- [ScenarioDefinition](ScenarioDefinition.md)
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

