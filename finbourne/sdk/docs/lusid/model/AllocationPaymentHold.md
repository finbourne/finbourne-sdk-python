# AllocationPaymentHold

A hold placed on a partner's payment against an allocation event, blocking receipt until it is released  by a second user.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **allocation_event_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **investor_record_id** | **str** | Required | The investor record identifier of the partner whose payment is held. |
| **status** | **str** | Required | The hold status: Blocked, Escrow or Released. |
| **reason** | **str** | Optional | The reason for the hold. |
| **reference** | **str** | Optional | An external reference for the hold, such as a compliance case number. |
| **placed_by** | **str** | Required | The user who placed the hold. |
| **placed_at** | **datetime** | Required | When the hold was placed. |
| **released_by** | **str** | Optional | The user who released the hold, or null while it is active. |
| **released_at** | **datetime** | Optional | When the hold was released, or null while it is active. |
| **active** | **bool** | Required | Whether the hold is currently blocking receipt of the partner&#39;s payment. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AllocationPaymentHold import AllocationPaymentHold

instance = AllocationPaymentHold(
    allocation_event_id=ResourceId(...),  # required
    investor_record_id="...",  # required — The investor record identifier of the partner whose payment is held.
    status="...",  # required — The hold status: Blocked, Escrow or Released.
    reason="...",  # optional — The reason for the hold.
    reference="...",  # optional — An external reference for the hold, such as a compliance case number.
    placed_by="...",  # required — The user who placed the hold.
    placed_at=datetime.now(),  # required — When the hold was placed.
    released_by="...",  # optional — The user who released the hold, or null while it is active.
    released_at=datetime.now(),  # optional — When the hold was released, or null while it is active.
    active=True  # required — Whether the hold is currently blocking receipt of the partner&#39;s payment.
)
```


## Related Models

- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

