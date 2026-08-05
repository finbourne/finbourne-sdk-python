# PriceShiftDefinition

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instrument** | **str** | Optional | A single instrument identifier this shift applies to. Exactly one of Instrument and Filter  must be supplied. |
| **filter** | **str** | Optional | A LUSID filter expression over the instrument entity - fields and properties - selecting which  instruments&#39; quotes the shift applies to, e.g.  \&quot;assetClass eq &#39;Bond&#39; and properties[Instrument/Issuer/Name] eq &#39;X&#39;\&quot;.  Exactly one of Instrument and Filter must be supplied. |
| **amount** | **float** | Required | *No description available.* |
| **shift_type** | **str** | Required | Available values: Absolute, Relative, Percentage. |
| **quote_type** | **str** | Optional | Available values: Price, Spread, Rate, LogNormalVol, NormalVol, ParSpread, IsdaSpread, Upfront, Index, Ratio, Delta, PoolFactor, InflationAssumption, DirtyPrice, PrincipalWriteOff, InterestDeferred, InterestShortfall, ConstituentWeightFactor. |
| **scenario_shift_type** | **str** | Required | Available values: RateCurveShiftDefinition, FxShiftDefinition, PriceShiftDefinition, VolSurfaceShiftDefinition, MdkrGroupShiftDefinition. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PriceShiftDefinition import PriceShiftDefinition

instance = PriceShiftDefinition(
    instrument="...",  # optional — A single instrument identifier this shift applies to. Exactly one of Instrument and Filter  must be supplied.
    filter="...",  # optional — A LUSID filter expression over the instrument entity - fields and properties - selecting which  instruments&#39; quotes the shift applies to, e.g.  \&quot;assetClass eq &#39;Bond&#39; and properties[Instrument/Issuer/Name] eq &#39;X&#39;\&quot;.  Exactly one of Instrument and Filter must be supplied.
    amount=0.0,  # required
    shift_type="...",  # required — Available values: Absolute, Relative, Percentage.
    quote_type="...",  # optional — Available values: Price, Spread, Rate, LogNormalVol, NormalVol, ParSpread, IsdaSpread, Upfront, Index, Ratio, Delta, PoolFactor, InflationAssumption, DirtyPrice, PrincipalWriteOff, InterestDeferred, InterestShortfall, ConstituentWeightFactor.
    scenario_shift_type="..."  # required — Available values: RateCurveShiftDefinition, FxShiftDefinition, PriceShiftDefinition, VolSurfaceShiftDefinition, MdkrGroupShiftDefinition.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

