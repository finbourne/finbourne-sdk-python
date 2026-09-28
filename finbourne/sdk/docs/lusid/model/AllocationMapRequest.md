# AllocationMapRequest

The request used to create or update an Allocation Map.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Required | The code of the Allocation Map. |
| **name** | **str** | Required | The display name of the Allocation Map. |
| **description** | **str** | Optional | An optional description for the Allocation Map. |
| **structure_member_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **inherits_from** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **participants** | [AllocationMapParticipants](AllocationMapParticipants.md) | Optional | *No description available.* |
| **basis_by_event_type** | [List[AllocationMapEventBasis]](AllocationMapEventBasis.md) | Optional | The basis on which each kind of allocation event is shared between the participants. At most one entry per event type. |
| **effective_at** | **datetime** | Optional | The effective datetime from which the Allocation Map applies. Defaults to the beginning of time if not specified, so that the map is visible at every effective datetime. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationMapRequest import AllocationMapRequest

instance = AllocationMapRequest(
    code="...",  # required — The code of the Allocation Map.
    name="...",  # required — The display name of the Allocation Map.
    description="...",  # optional — An optional description for the Allocation Map.
    structure_member_id=ResourceId(...),  # required
    inherits_from=ResourceId(...),  # optional
    participants=AllocationMapParticipants(...),  # optional
    basis_by_event_type=[],  # optional — The basis on which each kind of allocation event is shared between the participants. At most one entry per event type.
    effective_at=datetime.now()  # optional — The effective datetime from which the Allocation Map applies. Defaults to the beginning of time if not specified, so that the map is visible at every effective datetime.
)
```

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [AllocationMapParticipants](AllocationMapParticipants.md)
- [AllocationMapEventBasis](AllocationMapEventBasis.md) — used in `basis_by_event_type`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

