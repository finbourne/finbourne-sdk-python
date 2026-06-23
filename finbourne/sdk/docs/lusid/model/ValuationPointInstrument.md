# ValuationPointInstrument

An Instrument held at a Valuation Point, including its origin
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instrument** | [Instrument](Instrument.md) | Optional | *No description available.* |
| **valuation_point_origin** | **str** | Optional | Designates if the instrument was originally part of the Valuation Point or if it was added as part of a Complex Close action. Available values: None, Original, Added, OriginalAndAdded. |
| **added_origin_valuation_point_code** | **str** | Optional | The Valuation Point, only for an Instrument added as part of a Complex Close action. |
| **added_origin_valuation_point_variant_code** | **str** | Optional | The Valuation Point variant, only for Instruments added as part of a Complex Close action. |
| **valuation_point_origin_source** | **List[str]** | Optional | Collection of sources of Post Close Activities which added this instrument. Available values: Undefined, Manual, Auto. |
| **valuation_point_origin_type** | **List[str]** | Optional | Collection of types of Post Close Activities which added this instrument. Available values: PortfolioTransaction, PortfolioSettlementInstruction, InstrumentActivity, QuoteActivity. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | The requested instrument properties. These will be from the &#39;Instrument&#39; domain. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ValuationPointInstrument import ValuationPointInstrument

instance = ValuationPointInstrument(
    instrument=Instrument(...),  # optional
    valuation_point_origin="...",  # optional — Designates if the instrument was originally part of the Valuation Point or if it was added as part of a Complex Close action. Available values: None, Original, Added, OriginalAndAdded.
    added_origin_valuation_point_code="...",  # optional — The Valuation Point, only for an Instrument added as part of a Complex Close action.
    added_origin_valuation_point_variant_code="...",  # optional — The Valuation Point variant, only for Instruments added as part of a Complex Close action.
    valuation_point_origin_source=,  # optional — Collection of sources of Post Close Activities which added this instrument. Available values: Undefined, Manual, Auto.
    valuation_point_origin_type=,  # optional — Collection of types of Post Close Activities which added this instrument. Available values: PortfolioTransaction, PortfolioSettlementInstruction, InstrumentActivity, QuoteActivity.
    properties=ModelProperty(...)  # optional — The requested instrument properties. These will be from the &#39;Instrument&#39; domain.
)
```


## Related Models

- [Instrument](Instrument.md)
- [ModelProperty](ModelProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

