# DependencySourceFilter

Encapsulates parts of a market data rule relating not to the nature of the market data requested, but rather the nature of the thing (instrument/model) that is requesting it.  In the first instance, this includes the instrument type, asset class, and the currency of the underlying instrument.  This can be used to differentiate requests for market data according to the source of the request. See MarketDataSpecificRule.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instrument_type** | **str** | Optional | Specify that a rule should only apply if the market data is requested by an instrument of a given instrument type.  If null, then no filtering on instrument type is applied. |
| **asset_class** | **str** | Optional | Specify that a rule should only apply if the market data is requested by an instrument of a given asset class.  If null, then no filtering on asset class is applied. |
| **dom_ccy** | **str** | Optional | Specify that a rule should only apply if the market data is requested by an instrument with a given domestic currency.  If null, then no filtering on currency is applied. |
| **long_or_short_indicator** | **str** | Optional | Specify that a rule should apply if the market data is requested by a model with a given long or short indicator.  If none, then no filtering on LongOrShortIndicator is applied. |
| **address_key_filters** | [List[AddressKeyFilter]](AddressKeyFilter.md) | Optional | Specify that a rule should apply if the market data is requested by an instrument with features or properties  satisfying all the given address key filters. If an empty list is given, no additional filtering is done. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.DependencySourceFilter import DependencySourceFilter

instance = DependencySourceFilter(
    instrument_type="...",  # optional — Specify that a rule should only apply if the market data is requested by an instrument of a given instrument type.  If null, then no filtering on instrument type is applied.
    asset_class="...",  # optional — Specify that a rule should only apply if the market data is requested by an instrument of a given asset class.  If null, then no filtering on asset class is applied.
    dom_ccy="...",  # optional — Specify that a rule should only apply if the market data is requested by an instrument with a given domestic currency.  If null, then no filtering on currency is applied.
    long_or_short_indicator="...",  # optional — Specify that a rule should apply if the market data is requested by a model with a given long or short indicator.  If none, then no filtering on LongOrShortIndicator is applied.
    address_key_filters=[]  # optional — Specify that a rule should apply if the market data is requested by an instrument with features or properties  satisfying all the given address key filters. If an empty list is given, no additional filtering is done.
)
```

- [AddressKeyFilter](AddressKeyFilter.md) — used in `address_key_filters`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

