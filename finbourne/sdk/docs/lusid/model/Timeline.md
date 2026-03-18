# Timeline

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **display_name** | **str** | Optional | The name of the Timeline. |
| **description** | **str** | Optional | A description for the Timeline. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | The Timelines properties. These will be from the &#39;Timeline&#39; domain. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested asAt datetime. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.Timeline import Timeline

instance = Timeline(
    id=ResourceId(...),  # optional
    display_name="...",  # optional — The name of the Timeline.
    description="...",  # optional — A description for the Timeline.
    properties=ModelProperty(...),  # optional — The Timelines properties. These will be from the &#39;Timeline&#39; domain.
    version=Version(...),  # optional
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested asAt datetime.
    links=[]  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ModelProperty](ModelProperty.md) — used in `properties`
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

