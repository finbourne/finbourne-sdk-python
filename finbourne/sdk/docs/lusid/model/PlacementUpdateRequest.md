# PlacementUpdateRequest

A request to update a Placement.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **quantity** | **float** | Optional | The quantity of given instrument ordered. |
| **amount** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | Client-defined properties associated with this placement. |
| **type** | **str** | Optional | Optionally changes the type of this placement (Market, Limit, Stop, StopLimit, etc). A type change is permitted only when the associated block is of type &#39;Market&#39;. Setting the type to &#39;Market&#39; clears the placement&#39;s stop and limit prices; any other type change leaves them as they are. |
| **limit_price** | **float** | Optional | Optionally updates the limit price of this placement, in the placement&#39;s limit price currency unless a currency is also specified. A price on a placement with no limit price currency is stored but not returned until a currency is supplied. |
| **stop_price** | **float** | Optional | Optionally updates the stop price of this placement, in the placement&#39;s stop price currency unless a currency is also specified. A price on a placement with no stop price currency is stored but not returned until a currency is supplied. |
| **counterparty** | **str** | Optional | Optionally specifies the market entity this placement is placed with. |
| **execution_system** | **str** | Optional | Optionally specifies the execution system in use. |
| **entry_type** | **str** | Optional | Optionally specifies the entry type of this placement. Available values: Undecided, Manual, Direct, Ems, External. |
| **currency** | **str** | Optional | Optionally sets the ISO currency code of the placement&#39;s stop and/or limit price. Not permitted for a Market placement. For a value placement it must match the currency of the amount exactly, whether that amount is on the placement or in the update. When omitted, no currency checks are applied. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PlacementUpdateRequest import PlacementUpdateRequest

instance = PlacementUpdateRequest(
    id=ResourceId(...),  # required
    quantity=0.0,  # optional — The quantity of given instrument ordered.
    amount=CurrencyAndAmount(...),  # optional
    properties=PerpetualProperty(...),  # optional — Client-defined properties associated with this placement.
    type="...",  # optional — Optionally changes the type of this placement (Market, Limit, Stop, StopLimit, etc). A type change is permitted only when the associated block is of type &#39;Market&#39;. Setting the type to &#39;Market&#39; clears the placement&#39;s stop and limit prices; any other type change leaves them as they are.
    limit_price=0.0,  # optional — Optionally updates the limit price of this placement, in the placement&#39;s limit price currency unless a currency is also specified. A price on a placement with no limit price currency is stored but not returned until a currency is supplied.
    stop_price=0.0,  # optional — Optionally updates the stop price of this placement, in the placement&#39;s stop price currency unless a currency is also specified. A price on a placement with no stop price currency is stored but not returned until a currency is supplied.
    counterparty="...",  # optional — Optionally specifies the market entity this placement is placed with.
    execution_system="...",  # optional — Optionally specifies the execution system in use.
    entry_type="...",  # optional — Optionally specifies the entry type of this placement. Available values: Undecided, Manual, Direct, Ems, External.
    currency="..."  # optional — Optionally sets the ISO currency code of the placement&#39;s stop and/or limit price. Not permitted for a Market placement. For a value placement it must match the currency of the amount exactly, whether that amount is on the placement or in the update. When omitted, no currency checks are applied.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [PerpetualProperty](PerpetualProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

