# ReferenceListResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **name** | **str** | Required | The name of the reference list. |
| **description** | **str** | Optional | The description of the reference list. |
| **tags** | **List[str]** | Optional | The tags associated with the reference list. |
| **reference_list** | [ReferenceList](ReferenceList.md) | Required | *No description available.* |
| **version** | [Version](Version.md) | Required | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ReferenceListResponse import ReferenceListResponse

instance = ReferenceListResponse(
    id=ResourceId(...),  # required
    name="...",  # required — The name of the reference list.
    description="...",  # optional — The description of the reference list.
    tags=,  # optional — The tags associated with the reference list.
    reference_list=ReferenceList(...),  # required
    version=Version(...),  # required
    links=[]  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ReferenceList](ReferenceList.md)
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

