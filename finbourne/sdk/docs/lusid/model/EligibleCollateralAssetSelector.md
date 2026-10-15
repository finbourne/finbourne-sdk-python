# EligibleCollateralAssetSelector

The assets an eligible collateral row applies to, as stored on a schedule.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **kind** | **str** | Required | What the selector matches. One of BaseCurrencyCash, Cash or Instrument. Available values: BaseCurrencyCash, Cash, Instrument. |
| **currency** | **str** | Optional | The currency of the cash. Required for a Cash selector and not allowed otherwise. |
| **instrument_filter** | **str** | Optional | A filter selecting the instruments. Required for an Instrument selector and not allowed otherwise. Checked for structure only when the schedule is stored. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.EligibleCollateralAssetSelector import EligibleCollateralAssetSelector

instance = EligibleCollateralAssetSelector(
    kind="...",  # required — What the selector matches. One of BaseCurrencyCash, Cash or Instrument. Available values: BaseCurrencyCash, Cash, Instrument.
    currency="...",  # optional — The currency of the cash. Required for a Cash selector and not allowed otherwise.
    instrument_filter="..."  # optional — A filter selecting the instruments. Required for an Instrument selector and not allowed otherwise. Checked for structure only when the schedule is stored.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

