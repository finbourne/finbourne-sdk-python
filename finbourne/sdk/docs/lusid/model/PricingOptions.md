# PricingOptions

Options for controlling the default aspects and behaviour of the pricing engine.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **model_selection** | [ModelSelection](ModelSelection.md) | Optional | *No description available.* |
| **use_instrument_type_to_determine_pricer** | **bool** | Optional | If true then use the instrument type to set the default instrument pricer  This applies where no more specific set of overrides are provided on a per-vendor and instrument basis. |
| **allow_any_instruments_with_sec_uid_to_price_off_lookup** | **bool** | Optional | By default, one would not expect to price and exotic instrument, i.e. an instrument with a complicated  instrument definition simply through looking up a price as there should be a better way of evaluating it.  To override that behaviour and allow lookup for a price from the instrument identifier(s), set this to true. |
| **allow_partially_successful_evaluation** | **bool** | Optional | If true then a failure in task evaluation doesn&#39;t cause overall failure.  results will be returned where they succeeded and annotation elsewhere |
| **produce_separate_result_for_linear_otc_legs** | **bool** | Optional | If true (default), when pricing an Fx-Forward or Interest Rate Swap, Future and other linearly separable products, product two results, one for each leg  rather than a single line result with the amalgamated/summed pv from both legs. |
| **enable_use_of_cached_unit_results** | **bool** | Optional | If true, when pricing using a model or for an instrument that supports use of intermediate cached-results, use them.  Default is that this caching is turned off. |
| **window_valuation_on_instrument_start_end** | **bool** | Optional | If true, when valuing an instrument outside the period where it is &#39;alive&#39; (the start-maturity window) it will return a valuation of zero |
| **remove_contingent_cashflows_in_payment_diary** | **bool** | Optional | When creating a payment diary, should contingent cash payments (e.g. from exercise of a swaption into a swap) be included or not.  i.e. Is exercise or default being assumed to happen or not. |
| **use_child_sub_holding_keys_for_portfolio_expansion** | **bool** | Optional | Should fund constituents inherit subholding keys from the parent subholding keyb |
| **validate_domestic_and_quote_currencies_are_consistent** | **bool** | Optional | Do we validate that the instrument domestic currency matches the quote currency (unless unknown/zzz) when using lookup pricing. |
| **mbs_valuation_using_holding_current_face** | **bool** | Optional | *No description available.* |
| **convert_srs_cash_flows_to_portfolio_currency** | **bool** | Optional | In the case upserted structured result store (SRS) cashflows are not   in the portfolio currency, set this parameter to True to convert said  cashflows into the portfolio currency. By default, this flag is set   to False and Lusid will not do any FX conversion.    Please note that FX conversion is dependent on the data available in  the quote store - ensure that all relevant FX quotes have been loaded  for cashflow currency conversion. |
| **conserved_quantity_for_lookthrough_expansion** | **str** | Optional | When performing lookthrough portfolio expansion with ScalingMethodology set to \&quot;Sum\&quot; or \&quot;AbsoluteSum\&quot;,  the quantity specified here will be conserved and apportioned to lookthrough constituents.  For example, an equal-weighting index with 100 constituents can be modelled as a reference portfolio with 1% weights on each equity.  When expanding a $9000 holding of that index into its constituents while conserving PV, we end up with $90 of each equity.  The number of units of each equity held is then implied.  Note that conservation of one quantity may imply non-conservation of others, especially when some constituents are OTCs.                Allowed values are: \&quot;PV\&quot; (default), \&quot;Exposure\&quot;. |
| **return_zero_pv** | [ReturnZeroPvOptions](ReturnZeroPvOptions.md) | Optional | *No description available.* |
| **enable_leg_level_inference_for_custom_srs_columns** | **bool** | Optional | When enabled, allows inference between leg-level and  instrument-level data during portfolio valuation. If  data is missing at one level, it may be inferred from  the other level. For example, missing leg-level data   may be inferred from existing leg-level and instrument-  level data when ProduceSeparateResultForLinearOtcLegs  is enabled, and vice versa. Explicitly provided data  always takes precedence. |
| **use_instrument_scale_factor_as_default** | **bool** | Optional | When enabled, priceScaleFactor defined at the instrument level will  be used in the absence of quote scaleFactor when resolving quotes. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PricingOptions import PricingOptions

instance = PricingOptions(
    model_selection=ModelSelection(...),  # optional
    use_instrument_type_to_determine_pricer=True,  # optional — If true then use the instrument type to set the default instrument pricer  This applies where no more specific set of overrides are provided on a per-vendor and instrument basis.
    allow_any_instruments_with_sec_uid_to_price_off_lookup=True,  # optional — By default, one would not expect to price and exotic instrument, i.e. an instrument with a complicated  instrument definition simply through looking up a price as there should be a better way of evaluating it.  To override that behaviour and allow lookup for a price from the instrument identifier(s), set this to true.
    allow_partially_successful_evaluation=True,  # optional — If true then a failure in task evaluation doesn&#39;t cause overall failure.  results will be returned where they succeeded and annotation elsewhere
    produce_separate_result_for_linear_otc_legs=True,  # optional — If true (default), when pricing an Fx-Forward or Interest Rate Swap, Future and other linearly separable products, product two results, one for each leg  rather than a single line result with the amalgamated/summed pv from both legs.
    enable_use_of_cached_unit_results=True,  # optional — If true, when pricing using a model or for an instrument that supports use of intermediate cached-results, use them.  Default is that this caching is turned off.
    window_valuation_on_instrument_start_end=True,  # optional — If true, when valuing an instrument outside the period where it is &#39;alive&#39; (the start-maturity window) it will return a valuation of zero
    remove_contingent_cashflows_in_payment_diary=True,  # optional — When creating a payment diary, should contingent cash payments (e.g. from exercise of a swaption into a swap) be included or not.  i.e. Is exercise or default being assumed to happen or not.
    use_child_sub_holding_keys_for_portfolio_expansion=True,  # optional — Should fund constituents inherit subholding keys from the parent subholding keyb
    validate_domestic_and_quote_currencies_are_consistent=True,  # optional — Do we validate that the instrument domestic currency matches the quote currency (unless unknown/zzz) when using lookup pricing.
    mbs_valuation_using_holding_current_face=True,  # optional
    convert_srs_cash_flows_to_portfolio_currency=True,  # optional — In the case upserted structured result store (SRS) cashflows are not   in the portfolio currency, set this parameter to True to convert said  cashflows into the portfolio currency. By default, this flag is set   to False and Lusid will not do any FX conversion.    Please note that FX conversion is dependent on the data available in  the quote store - ensure that all relevant FX quotes have been loaded  for cashflow currency conversion.
    conserved_quantity_for_lookthrough_expansion="...",  # optional — When performing lookthrough portfolio expansion with ScalingMethodology set to \&quot;Sum\&quot; or \&quot;AbsoluteSum\&quot;,  the quantity specified here will be conserved and apportioned to lookthrough constituents.  For example, an equal-weighting index with 100 constituents can be modelled as a reference portfolio with 1% weights on each equity.  When expanding a $9000 holding of that index into its constituents while conserving PV, we end up with $90 of each equity.  The number of units of each equity held is then implied.  Note that conservation of one quantity may imply non-conservation of others, especially when some constituents are OTCs.                Allowed values are: \&quot;PV\&quot; (default), \&quot;Exposure\&quot;.
    return_zero_pv=ReturnZeroPvOptions(...),  # optional
    enable_leg_level_inference_for_custom_srs_columns=True,  # optional — When enabled, allows inference between leg-level and  instrument-level data during portfolio valuation. If  data is missing at one level, it may be inferred from  the other level. For example, missing leg-level data   may be inferred from existing leg-level and instrument-  level data when ProduceSeparateResultForLinearOtcLegs  is enabled, and vice versa. Explicitly provided data  always takes precedence.
    use_instrument_scale_factor_as_default=True  # optional — When enabled, priceScaleFactor defined at the instrument level will  be used in the absence of quote scaleFactor when resolving quotes.
)
```


## Related Models

- [ModelSelection](ModelSelection.md)
- [ReturnZeroPvOptions](ReturnZeroPvOptions.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

