# A2BDataRecord

A2B Record - shows values on, and changes between two dates: A and B
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **portfolio_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **holding_type** | **str** | Optional | The code for the type of the holding e.g. P, B, C, R, F etc. |
| **instrument_scope** | **str** | Optional | The unique Lusid Instrument Id (LUID) of the instrument that the holding is in. |
| **instrument_uid** | **str** | Optional | The unique Lusid Instrument Id (LUID) of the instrument that the holding is in. |
| **sub_holding_keys** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | The sub-holding properties which identify the holding. Each property will be from the &#39;Transaction&#39; domain. These are configured on a transaction portfolio. |
| **currency** | **str** | Optional | The holding currency. |
| **transaction_id** | **str** | Optional | The unique identifier for the transaction. |
| **start** | [A2BCategory](A2BCategory.md) | Optional | *No description available.* |
| **flows** | [A2BCategory](A2BCategory.md) | Optional | *No description available.* |
| **gains** | [A2BCategory](A2BCategory.md) | Optional | *No description available.* |
| **carry** | [A2BCategory](A2BCategory.md) | Optional | *No description available.* |
| **end** | [A2BCategory](A2BCategory.md) | Optional | *No description available.* |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | The properties which have been requested to be decorated onto the holding. These will be from the &#39;Instrument&#39; domain. |
| **group_id** | **str** | Optional | Arbitrary string that can be used to cross reference an entry in the A2B report with activity in the A2B-Movements. This should be used purely as a token. The content should not be relied upon. |
| **errors** | [List[ResponseMetaData]](ResponseMetaData.md) | Optional | Any errors with the record are reported here. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.A2BDataRecord import A2BDataRecord

instance = A2BDataRecord(
    portfolio_id=ResourceId(...),  # optional
    holding_type="...",  # optional — The code for the type of the holding e.g. P, B, C, R, F etc.
    instrument_scope="...",  # optional — The unique Lusid Instrument Id (LUID) of the instrument that the holding is in.
    instrument_uid="...",  # optional — The unique Lusid Instrument Id (LUID) of the instrument that the holding is in.
    sub_holding_keys=PerpetualProperty(...),  # optional — The sub-holding properties which identify the holding. Each property will be from the &#39;Transaction&#39; domain. These are configured on a transaction portfolio.
    currency="...",  # optional — The holding currency.
    transaction_id="...",  # optional — The unique identifier for the transaction.
    start=A2BCategory(...),  # optional
    flows=A2BCategory(...),  # optional
    gains=A2BCategory(...),  # optional
    carry=A2BCategory(...),  # optional
    end=A2BCategory(...),  # optional
    properties=ModelProperty(...),  # optional — The properties which have been requested to be decorated onto the holding. These will be from the &#39;Instrument&#39; domain.
    group_id="...",  # optional — Arbitrary string that can be used to cross reference an entry in the A2B report with activity in the A2B-Movements. This should be used purely as a token. The content should not be relied upon.
    errors=[]  # optional — Any errors with the record are reported here.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [PerpetualProperty](PerpetualProperty.md) — used in `sub_holding_keys`
- [A2BCategory](A2BCategory.md)
- [A2BCategory](A2BCategory.md)
- [A2BCategory](A2BCategory.md)
- [A2BCategory](A2BCategory.md)
- [A2BCategory](A2BCategory.md)
- [ModelProperty](ModelProperty.md) — used in `properties`
- [ResponseMetaData](ResponseMetaData.md) — used in `errors`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

