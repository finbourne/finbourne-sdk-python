# Calendar

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | *No description available.* |
| **id** | [../model/ResourceId](ResourceId.md) | Required | *No description available.* |
| **type** | **str** | Required | *No description available.* |
| **weekend_mask** | [../model/WeekendMask](WeekendMask.md) | Required | *No description available.* |
| **source_provider** | **str** | Required | *No description available.* |
| **properties** | [../model/List[ModelProperty]](ModelProperty.md) | Required | *No description available.* |
| **version** | [../model/Version](Version.md) | Optional | *No description available.* |
| **links** | [../model/List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.Calendar import Calendar

instance = Calendar(
    href="...",  # optional
    id=ResourceId(...),  # required
    type="...",  # required
    weekend_mask=WeekendMask(...),  # required
    source_provider="...",  # required
    properties=[],  # required
    version=Version(...),  # optional
    links=[]  # optional
)
```

- [ResourceId](ResourceId.md)
- [WeekendMask](WeekendMask.md)
- [ModelProperty](ModelProperty.md)
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

