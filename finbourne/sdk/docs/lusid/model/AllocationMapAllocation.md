# AllocationMapAllocation

One investor record's share of a resolved allocation event.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **investor_record_id** | **str** | Optional | The investor record that receives the share. |
| **basis_value** | **float** | Optional | The basis value the pro rata share was weighted by. Absent for a fixed or excluded investor record. |
| **weight** | **float** | Optional | The fraction of the remainder the investor record receives, or the fixed fraction of the whole amount for a FixedPercentage exception. |
| **amount** | **float** | Optional | The amount allocated to the investor record. |
| **treatment** | **str** | Optional | How the share was found. Derived means pro rata from the basis; FixedPercentage means off the top from an exception; Excluded means an exception removed the investor record and it receives nothing. Available values: Derived, FixedPercentage, Excluded. |
| **commitment_line_id** | **str** | Optional | For a Commitment event, the commitment line the share is recorded against. Absent for other event types. |
| **portfolio_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **component** | **str** | Optional | The component of the event the share belongs to. Absent when the event was resolved whole. |
| **origin_member_short_code** | **str** | Optional | The deal the share is for, when a capital call&#39;s use of proceeds split one component across deals. Absent when the component&#39;s own origin applies. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationMapAllocation import AllocationMapAllocation

instance = AllocationMapAllocation(
    investor_record_id="...",  # optional — The investor record that receives the share.
    basis_value=0.0,  # optional — The basis value the pro rata share was weighted by. Absent for a fixed or excluded investor record.
    weight=0.0,  # optional — The fraction of the remainder the investor record receives, or the fixed fraction of the whole amount for a FixedPercentage exception.
    amount=0.0,  # optional — The amount allocated to the investor record.
    treatment="...",  # optional — How the share was found. Derived means pro rata from the basis; FixedPercentage means off the top from an exception; Excluded means an exception removed the investor record and it receives nothing. Available values: Derived, FixedPercentage, Excluded.
    commitment_line_id="...",  # optional — For a Commitment event, the commitment line the share is recorded against. Absent for other event types.
    portfolio_id=ResourceId(...),  # optional
    component="...",  # optional — The component of the event the share belongs to. Absent when the event was resolved whole.
    origin_member_short_code="..."  # optional — The deal the share is for, when a capital call&#39;s use of proceeds split one component across deals. Absent when the component&#39;s own origin applies.
)
```

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

