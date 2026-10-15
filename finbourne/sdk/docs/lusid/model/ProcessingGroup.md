# ProcessingGroup

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **display_name** | **str** | Optional | The name of the Processing Group. |
| **description** | **str** | Optional | A description for the Processing Group. |
| **schedule** | [ProcessingGroupSchedule](ProcessingGroupSchedule.md) | Optional | *No description available.* |
| **reference_list_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **workflow_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **resolved_reference_list** | [ReferenceList](ReferenceList.md) | Optional | *No description available.* |
| **list_exception_filter** | **str** | Optional | A filter selecting reference list items to exclude whenever this Processing Group resolves its reference list. Optional. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ProcessingGroup import ProcessingGroup

instance = ProcessingGroup(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    id=ResourceId(...),  # required
    display_name="...",  # optional — The name of the Processing Group.
    description="...",  # optional — A description for the Processing Group.
    schedule=ProcessingGroupSchedule(...),  # optional
    reference_list_id=ResourceId(...),  # optional
    workflow_id=ResourceId(...),  # optional
    resolved_reference_list=ReferenceList(...),  # optional
    list_exception_filter="...",  # optional — A filter selecting reference list items to exclude whenever this Processing Group resolves its reference list. Optional.
    version=Version(...),  # optional
    links=[]  # optional
)
```

- [ResourceId](ResourceId.md)
- [ProcessingGroupSchedule](ProcessingGroupSchedule.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ReferenceList](ReferenceList.md)
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

