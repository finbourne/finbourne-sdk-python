# InstrumentCapabilities

Instrument capabilities containing useful information about the instrument and the model. This includes  - features corresponding to the instrument i.e. Optionality:American, Other:InflationLinked  - supported addresses (if model provided) i.e. Valuation/Pv, Valuation/DirtyPriceKey, Valuation/Accrued  - economic dependencies (if model provided) i.e. Cash:USD, Fx:GBP.USD, Rates:GBP.GBPOIS
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instrument_id** | **str** | Optional | The Lusid instrument id for the instrument e.g. &#39;LUID_00003D4X&#39;. |
| **model** | **str** | Optional | The pricing model e.g. &#39;Discounting&#39;. |
| **features** | **Dict[str, Optional[str]]** | Optional | Features of the instrument describing its optionality, payoff type and more e.g. &#39;Instrument/Features/Exercise: American&#39;, &#39;Instrument/Features/Product: Option&#39; |
| **supported_addresses** | [List[DescribedAddressKey]](DescribedAddressKey.md) | Optional | Queryable addresses supported by the model, e.g. &#39;Valuation/Pv&#39;, &#39;Valuation/Accrued&#39;. |
| **economic_dependencies** | [List[EconomicDependency]](EconomicDependency.md) | Optional | Economic dependencies for the model, e.g. &#39;Fx:GBP.USD&#39;, &#39;Cash:GBP&#39;, &#39;Rates:GBP.GBPOIS&#39;. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.InstrumentCapabilities import InstrumentCapabilities

instance = InstrumentCapabilities(
    instrument_id="...",  # optional — The Lusid instrument id for the instrument e.g. &#39;LUID_00003D4X&#39;.
    model="...",  # optional — The pricing model e.g. &#39;Discounting&#39;.
    features=,  # optional — Features of the instrument describing its optionality, payoff type and more e.g. &#39;Instrument/Features/Exercise: American&#39;, &#39;Instrument/Features/Product: Option&#39;
    supported_addresses=[],  # optional — Queryable addresses supported by the model, e.g. &#39;Valuation/Pv&#39;, &#39;Valuation/Accrued&#39;.
    economic_dependencies=[],  # optional — Economic dependencies for the model, e.g. &#39;Fx:GBP.USD&#39;, &#39;Cash:GBP&#39;, &#39;Rates:GBP.GBPOIS&#39;.
    links=[]  # optional
)
```

- [DescribedAddressKey](DescribedAddressKey.md) — used in `supported_addresses`
- [EconomicDependency](EconomicDependency.md) — used in `economic_dependencies`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

