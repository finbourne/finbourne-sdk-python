# CollateralAllocationOverride

An asset and the units of it a user chooses to move for a margin call, validated against the agreement's  constraints as the allocation is.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instrument_id** | **str** | Required | The LUSID instrument identifier of the asset to move, or CCY_ and the currency code for cash. |
| **portfolio_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **units** | **float** | Required | The units to move. |
| **custodian_account** | [ResourceId](ResourceId.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CollateralAllocationOverride import CollateralAllocationOverride

instance = CollateralAllocationOverride(
    instrument_id="...",  # required — The LUSID instrument identifier of the asset to move, or CCY_ and the currency code for cash.
    portfolio_id=ResourceId(...),  # required
    units=0.0,  # required — The units to move.
    custodian_account=ResourceId(...)  # optional
)
```

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

