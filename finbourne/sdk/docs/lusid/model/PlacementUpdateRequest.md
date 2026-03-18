# PlacementUpdateRequest

A request to create or update a Placement.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **quantity** | **float** | Optional | The quantity of given instrument ordered. |
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | Client-defined properties associated with this placement. |
| **type** | **str** | Optional | The type of this placement (Market, Limit, etc). |
| **limit_price** | **float** | Optional | The optional price, as currency and amount, associated with this placement. |
| **stop_price** | **float** | Optional | The optional price, as currency and amount, associated with this placement. |
| **counterparty** | **str** | Optional | Optionally specifies the market entity this placement is placed with. |
| **execution_system** | **str** | Optional | Optionally specifies the execution system in use. |
| **entry_type** | **str** | Optional | Optionally specifies the entry type of this placement. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PlacementUpdateRequest import PlacementUpdateRequest

instance = PlacementUpdateRequest(
    id=ResourceId(...),  # required
    quantity=0.0,  # optional — The quantity of given instrument ordered.
    properties=PerpetualProperty(...),  # optional — Client-defined properties associated with this placement.
    type="...",  # optional — The type of this placement (Market, Limit, etc).
    limit_price=0.0,  # optional — The optional price, as currency and amount, associated with this placement.
    stop_price=0.0,  # optional — The optional price, as currency and amount, associated with this placement.
    counterparty="...",  # optional — Optionally specifies the market entity this placement is placed with.
    execution_system="...",  # optional — Optionally specifies the execution system in use.
    entry_type="..."  # optional — Optionally specifies the entry type of this placement.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [PerpetualProperty](PerpetualProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

