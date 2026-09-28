# SimpleModelOptions

Model options for a minimal pricer, allowing accrued interest calculation to be disabled and  the price quote to be interpreted as an offset from par.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **assume_accrued_is_zero** | **bool** | Optional | Disable calculation for accrued interest  The simple static pricer will attempt to calculate accrued interest where an instrument is present  and the accrued is requested. This may no be what is desired. If the user is sure they just want lookup  pricing then they can disable the accrued interest calculation attempt.  If set, the override accrued will be used if given but the calculation for accrued will just return zero.  This will also disable requesting any required instrument dependencies (e.g. resets) that might be required  to calculate accrued. |
| **price_is_par_offset** | **bool** | Optional | Interpret the instrument&#39;s price quote as an offset from par rather than as a currency value for  one unit of notional. The unit value becomes (price - basis) / basis, so a quote at par gives a  unit value of zero. The basis is taken from the quote&#39;s own scale factor, or 100 when the quote carries none.  This is not the treatment a bond price receives: a bond price is a proportion of par and scales  its value, whereas here only the distance from par carries value.  Supported for an interest rate swap only; setting it for any other instrument type fails the  valuation.  Quotes provided must have a quote type of either Price or DirtyPrice. The resulting unit  value is then the clean PV for a Price quote and the dirty PV for a DirtyPrice quote,  with accrued giving the other.  The quote must describe the swap as it is defined. The legs&#39; pay and receive directions do not  sign the value taken from the quote, so a swap booked the other way round is expected to be  quoted the other side of par. |
| **model_options_type** | **str** | Required | Available values: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, CdsModelOptions, FlexibleLoanPricerOptions, HullWhiteModelOptions, BondLookupModelOptions, BondForwardModelOptions, SimpleModelOptions. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SimpleModelOptions import SimpleModelOptions

instance = SimpleModelOptions(
    assume_accrued_is_zero=True,  # optional — Disable calculation for accrued interest  The simple static pricer will attempt to calculate accrued interest where an instrument is present  and the accrued is requested. This may no be what is desired. If the user is sure they just want lookup  pricing then they can disable the accrued interest calculation attempt.  If set, the override accrued will be used if given but the calculation for accrued will just return zero.  This will also disable requesting any required instrument dependencies (e.g. resets) that might be required  to calculate accrued.
    price_is_par_offset=True,  # optional — Interpret the instrument&#39;s price quote as an offset from par rather than as a currency value for  one unit of notional. The unit value becomes (price - basis) / basis, so a quote at par gives a  unit value of zero. The basis is taken from the quote&#39;s own scale factor, or 100 when the quote carries none.  This is not the treatment a bond price receives: a bond price is a proportion of par and scales  its value, whereas here only the distance from par carries value.  Supported for an interest rate swap only; setting it for any other instrument type fails the  valuation.  Quotes provided must have a quote type of either Price or DirtyPrice. The resulting unit  value is then the clean PV for a Price quote and the dirty PV for a DirtyPrice quote,  with accrued giving the other.  The quote must describe the swap as it is defined. The legs&#39; pay and receive directions do not  sign the value taken from the quote, so a swap booked the other way round is expected to be  quoted the other side of par.
    model_options_type="..."  # required — Available values: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, CdsModelOptions, FlexibleLoanPricerOptions, HullWhiteModelOptions, BondLookupModelOptions, BondForwardModelOptions, SimpleModelOptions.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

