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
| **basis_by_event_type** | [List[AllocationMapEventBasis]](AllocationMapEventBasis.md) | Required | The basis on which each kind of allocation event is shared between the participants. At most one entry per event type and component; an entry without a component is the default for the event type. |
| **rounding_partner_line** | **str** | Optional | The investor record that takes every minor unit left over when the shares of an event are rounded. Absent means the leftover is spread one minor unit at a time over the largest remainders. |
| **ilpa_transaction_types** | [List[AllocationMapIlpaTransactionType]](AllocationMapIlpaTransactionType.md) | Optional | The ILPA transaction types the map reports particular kinds of allocation event under, where they differ from the default for the event type and component. At most one entry per event type and component; an entry without a component is the default for the event type. Every value must be one the system IlpaTransactionType data type lists. |
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
    basis_by_event_type=[],  # required — The basis on which each kind of allocation event is shared between the participants. At most one entry per event type and component; an entry without a component is the default for the event type.
    rounding_partner_line="...",  # optional — The investor record that takes every minor unit left over when the shares of an event are rounded. Absent means the leftover is spread one minor unit at a time over the largest remainders.
    ilpa_transaction_types=[],  # optional — The ILPA transaction types the map reports particular kinds of allocation event under, where they differ from the default for the event type and component. At most one entry per event type and component; an entry without a component is the default for the event type. Every value must be one the system IlpaTransactionType data type lists.
    version=Version(...),  # optional
    links=[]  # optional
)
```

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [AllocationMapParticipants](AllocationMapParticipants.md)
- [AllocationMapEventBasis](AllocationMapEventBasis.md) — used in `basis_by_event_type`
- [AllocationMapIlpaTransactionType](AllocationMapIlpaTransactionType.md) — used in `ilpa_transaction_types`
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

