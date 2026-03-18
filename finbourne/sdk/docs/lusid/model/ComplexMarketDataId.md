# ComplexMarketDataId

An identifier that uniquely describes an item of complex market data such as an interest rate curve or volatility surface.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **provider** | **str** | Required | The platform or vendor that provided the complex market data, e.g. &#39;DataScope&#39;, &#39;LUSID&#39;, etc. |
| **price_source** | **str** | Optional | The source or originator of the complex market data, e.g. a bank or financial institution. |
| **lineage** | **str** | Optional | This is obsolete. It is not used, it will not be stored, and has no effects.  If you wish to attach a Lineage to your ComplexMarketData,  you should provide it in the optional Lineage field in the ComplexMarketData class. |
| **effective_at** | **str** | Optional | The effectiveAt or cut label that this item of complex market data is/was updated/inserted with. |
| **market_asset** | **str** | Required | The name of the market entity that the document represents |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ComplexMarketDataId import ComplexMarketDataId

instance = ComplexMarketDataId(
    provider="...",  # required — The platform or vendor that provided the complex market data, e.g. &#39;DataScope&#39;, &#39;LUSID&#39;, etc.
    price_source="...",  # optional — The source or originator of the complex market data, e.g. a bank or financial institution.
    lineage="...",  # optional — This is obsolete. It is not used, it will not be stored, and has no effects.  If you wish to attach a Lineage to your ComplexMarketData,  you should provide it in the optional Lineage field in the ComplexMarketData class.
    effective_at="...",  # optional — The effectiveAt or cut label that this item of complex market data is/was updated/inserted with.
    market_asset="..."  # required — The name of the market entity that the document represents
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

