# Economics

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instrument_scope** | **str** | Optional | The scope in which the instrument lies. |
| **lusid_instrument_id** | **str** | Required | The unique Lusid Instrument Id (LUID) of the instrument that economics are for. |
| **sub_holding_keys** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | The sub-holding properties which identify the Economic. Each property will be from the &#39;Transaction&#39; domain. These are configured on a transaction portfolio. |
| **buckets** | [List[Bucket]](Bucket.md) | Optional | Set of economic data related with each of the side impact of the transaction. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.Economics import Economics

instance = Economics(
    instrument_scope="...",  # optional — The scope in which the instrument lies.
    lusid_instrument_id="...",  # required — The unique Lusid Instrument Id (LUID) of the instrument that economics are for.
    sub_holding_keys=PerpetualProperty(...),  # optional — The sub-holding properties which identify the Economic. Each property will be from the &#39;Transaction&#39; domain. These are configured on a transaction portfolio.
    buckets=[]  # optional — Set of economic data related with each of the side impact of the transaction.
)
```

- [PerpetualProperty](PerpetualProperty.md) — used in `sub_holding_keys`
- [Bucket](Bucket.md) — used in `buckets`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

