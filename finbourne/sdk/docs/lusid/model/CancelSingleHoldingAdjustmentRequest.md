# CancelSingleHoldingAdjustmentRequest

This request specifies single target holding. i.e. holding data that the  system should match. And deletes previous adjustment made to that holding
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instrument_identifiers** | **Dict[str, Optional[str]]** | Required | A set of instrument identifiers that can resolve the holding adjustment to a unique instrument. |
| **sub_holding_keys** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | The sub-holding properties which identify the holding. Each property must be from the &#39;Transaction&#39; domain. |
| **currency** | **str** | Optional | The Holding currency. |
| **custodian_account_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CancelSingleHoldingAdjustmentRequest import CancelSingleHoldingAdjustmentRequest

instance = CancelSingleHoldingAdjustmentRequest(
    instrument_identifiers=,  # required — A set of instrument identifiers that can resolve the holding adjustment to a unique instrument.
    sub_holding_keys=PerpetualProperty(...),  # optional — The sub-holding properties which identify the holding. Each property must be from the &#39;Transaction&#39; domain.
    currency="...",  # optional — The Holding currency.
    custodian_account_id=ResourceId(...)  # optional
)
```

- [PerpetualProperty](PerpetualProperty.md) — used in `sub_holding_keys`
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

