# AssetLeg

The underlying instrument representing one side of the TRS and its pay-receive direction.                Note that TRS currently only supports an asset of Bond or ComplexBond, no other instruments are allowed.  Support for additional instrument types will be added in the future.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **asset** | [LusidInstrument](LusidInstrument.md) | Required | *No description available.* |
| **pay_receive** | **str** | Required | Either Pay or Receive stating direction of the asset in the swap.    Supported string (enumeration) values are: [Pay, Receive]. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AssetLeg import AssetLeg

instance = AssetLeg(
    asset=LusidInstrument(...),  # required
    pay_receive="..."  # required — Either Pay or Receive stating direction of the asset in the swap.    Supported string (enumeration) values are: [Pay, Receive].
)
```


## Related Models

- [LusidInstrument](LusidInstrument.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

