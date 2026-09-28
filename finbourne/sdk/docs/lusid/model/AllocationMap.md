# AllocationMap

The rules that say which investor records share in the economics of a member of a Fund Structure, and on what basis.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **name** | **str** | Required | The display name of the Allocation Map. |
| **description** | **str** | Optional | An optional description for the Allocation Map. |
| **structure_member_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **inherits_from** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **participants** | [AllocationMapParticipants](AllocationMapParticipants.md) | Required | *No description available.* |
| **basis_by_event_type** | [List[AllocationMapEventBasis]](AllocationMapEventBasis.md) | Required | The basis on which each kind of allocation event is shared between the participants. At most one entry per event type. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationMap import AllocationMap

instance = AllocationMap(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    id=ResourceId(...),  # required
    name="...",  # required — The display name of the Allocation Map.
    description="...",  # optional — An optional description for the Allocation Map.
    structure_member_id=ResourceId(...),  # required
    inherits_from=ResourceId(...),  # optional
    participants=AllocationMapParticipants(...),  # required
    basis_by_event_type=[],  # required — The basis on which each kind of allocation event is shared between the participants. At most one entry per event type.
    version=Version(...),  # optional
    links=[]  # optional
)
```

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [AllocationMapParticipants](AllocationMapParticipants.md)
- [AllocationMapEventBasis](AllocationMapEventBasis.md) — used in `basis_by_event_type`
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

