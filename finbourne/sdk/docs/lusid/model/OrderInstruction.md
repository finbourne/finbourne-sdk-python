# OrderInstruction

Record of an order instruction
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **created_date** | **datetime** | Required | The active date of this order instruction. |
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | Client-defined properties associated with this execution. |
| **portfolio_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **instrument_identifiers** | **Dict[str, Optional[str]]** | Required | The instrument ordered. |
| **quantity** | **float** | Optional | The quantity of given instrument ordered. |
| **weight** | **float** | Optional | The proportion of the total portfolio value ordered for the given instrument ordered. |
| **price** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **instrument_scope** | **str** | Optional | The scope in which the instrument lies |
| **lusid_instrument_id** | **str** | Optional | The LUSID instrument id for the instrument ordered. |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **data_model_membership** | [DataModelMembership](DataModelMembership.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.OrderInstruction import OrderInstruction

instance = OrderInstruction(
    id=ResourceId(...),  # required
    created_date=datetime.now(),  # required — The active date of this order instruction.
    properties=PerpetualProperty(...),  # optional — Client-defined properties associated with this execution.
    portfolio_id=ResourceId(...),  # optional
    instrument_identifiers=,  # required — The instrument ordered.
    quantity=0.0,  # optional — The quantity of given instrument ordered.
    weight=0.0,  # optional — The proportion of the total portfolio value ordered for the given instrument ordered.
    price=CurrencyAndAmount(...),  # optional
    instrument_scope="...",  # optional — The scope in which the instrument lies
    lusid_instrument_id="...",  # optional — The LUSID instrument id for the instrument ordered.
    version=Version(...),  # optional
    data_model_membership=DataModelMembership(...),  # optional
    links=[]  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [PerpetualProperty](PerpetualProperty.md) — used in `properties`
- [ResourceId](ResourceId.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [Version](Version.md)
- [DataModelMembership](DataModelMembership.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

