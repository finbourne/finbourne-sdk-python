# InstrumentResolutionDetail

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instrument_identifiers** | **Dict[str, Optional[str]]** | Required | Unique instrument identifiers |
| **lusid_instrument_id** | **str** | Optional | LUSID&#39;s internal unique instrument identifier, resolved from the instrument identifiers *(read-only)* |
| **instrument_scope** | **str** | Optional | The scope in which the instrument lies. *(read-only)* |
| **launch_price** | **float** | Optional | The launch price set when a shareclass is added to the fund. Defaults to 1. |
| **launch_date** | **datetime** | Optional | The launch date set when a shareclass is added to the fund. Defaults to Fund Inception Date. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.InstrumentResolutionDetail import InstrumentResolutionDetail

instance = InstrumentResolutionDetail(
    instrument_identifiers=,  # required — Unique instrument identifiers
    lusid_instrument_id="...",  # optional — LUSID&#39;s internal unique instrument identifier, resolved from the instrument identifiers
    instrument_scope="...",  # optional — The scope in which the instrument lies.
    launch_price=0.0,  # optional — The launch price set when a shareclass is added to the fund. Defaults to 1.
    launch_date=datetime.now()  # optional — The launch date set when a shareclass is added to the fund. Defaults to Fund Inception Date.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

