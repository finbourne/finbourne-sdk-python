# Placement

A street order for a quantity of a single instrument placed with a single market entity.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **parent_placement_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **block_ids** | [List[ResourceId]](ResourceId.md) | Required | The IDs of the Blocks associated with this placement. |
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | Client-defined properties associated with this placement. |
| **instrument_identifiers** | **Dict[str, Optional[str]]** | Required | The instrument ordered. |
| **lusid_instrument_id** | **str** | Required | The LUSID instrument id for the instrument placement. |
| **quantity** | **float** | Required | The quantity of given instrument ordered. |
| **state** | **str** | Required | The state of this placement (typically a FIX state; Open, Filled, etc). |
| **side** | **str** | Required | The side (Buy, Sell, ...) of this placement. |
| **time_in_force** | **str** | Required | The time in force applicable to this placement (GTC, FOK, Day, etc) |
| **type** | **str** | Required | The type of this placement (Market, Limit, etc). |
| **created_date** | **datetime** | Required | The active date of this placement. |
| **limit_price** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **stop_price** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **counterparty** | **str** | Optional | Optionally specifies the market entity this placement is placed with. |
| **execution_system** | **str** | Optional | Optionally specifies the execution system in use. |
| **entry_type** | **str** | Optional | Optionally specifies the entry type of this placement. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **data_model_membership** | [DataModelMembership](DataModelMembership.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.Placement import Placement

instance = Placement(
    id=ResourceId(...),  # required
    parent_placement_id=ResourceId(...),  # optional
    block_ids=[],  # required — The IDs of the Blocks associated with this placement.
    properties=PerpetualProperty(...),  # optional — Client-defined properties associated with this placement.
    instrument_identifiers=,  # required — The instrument ordered.
    lusid_instrument_id="...",  # required — The LUSID instrument id for the instrument placement.
    quantity=0.0,  # required — The quantity of given instrument ordered.
    state="...",  # required — The state of this placement (typically a FIX state; Open, Filled, etc).
    side="...",  # required — The side (Buy, Sell, ...) of this placement.
    time_in_force="...",  # required — The time in force applicable to this placement (GTC, FOK, Day, etc)
    type="...",  # required — The type of this placement (Market, Limit, etc).
    created_date=datetime.now(),  # required — The active date of this placement.
    limit_price=CurrencyAndAmount(...),  # optional
    stop_price=CurrencyAndAmount(...),  # optional
    counterparty="...",  # optional — Optionally specifies the market entity this placement is placed with.
    execution_system="...",  # optional — Optionally specifies the execution system in use.
    entry_type="...",  # optional — Optionally specifies the entry type of this placement.
    version=Version(...),  # optional
    data_model_membership=DataModelMembership(...),  # optional
    links=[]  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md) — used in `block_ids`
- [PerpetualProperty](PerpetualProperty.md) — used in `properties`
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [Version](Version.md)
- [DataModelMembership](DataModelMembership.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

