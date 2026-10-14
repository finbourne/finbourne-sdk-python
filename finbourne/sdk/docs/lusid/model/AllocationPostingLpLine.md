# AllocationPostingLpLine

One instrument event a booking writes on an investor's commitment line.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | **str** | Optional | The deterministic identifier of the posting: the booking reference, investor record, commitment line, component and side. |
| **instrument** | **str** | Optional | The commitment-line instrument the event is written on. |
| **portfolio** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **event** | **str** | Optional | The instrument event type written, for instance CapitalCallEvent. |
| **amount** | **float** | Optional | The amount posted, in the event currency. |
| **component** | **str** | Optional | The component of the event the posting carries. |
| **investor_record_id** | **str** | Optional | The investor record the posting is for. |
| **origin_member_short_code** | **str** | Optional | The member of the structure the component originates from, when it is not the map&#39;s own member. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationPostingLpLine import AllocationPostingLpLine

instance = AllocationPostingLpLine(
    id="...",  # optional — The deterministic identifier of the posting: the booking reference, investor record, commitment line, component and side.
    instrument="...",  # optional — The commitment-line instrument the event is written on.
    portfolio=ResourceId(...),  # optional
    event="...",  # optional — The instrument event type written, for instance CapitalCallEvent.
    amount=0.0,  # optional — The amount posted, in the event currency.
    component="...",  # optional — The component of the event the posting carries.
    investor_record_id="...",  # optional — The investor record the posting is for.
    origin_member_short_code="..."  # optional — The member of the structure the component originates from, when it is not the map&#39;s own member.
)
```

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

