# ShareClass

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instrument_identifiers** | **Dict[str, Optional[str]]** | Required | Unique instrument identifiers |
| **series** | [List[Series]](Series.md) | Optional | The series that belong to this Share Class. |
| **code** | **str** | Required | The unique code for the Share Class. Must be unique within the Fund. |
| **name** | **str** | Required | The display name of the Share Class. |
| **description** | **str** | Optional | An optional description for the Share Class. |
| **share_class_short_code** | **str** | Required | A short code that uniquely identifies the share class within the Fund. |
| **launch_price** | **float** | Optional | The launch price set when a shareclass is added to the fund. Defaults to 1. |
| **launch_date** | **datetime** | Optional | The launch date set when a shareclass is added to the fund. Defaults to Fund Inception Date. |
| **apportionment_factor** | **float** | Optional | The weighting factor used for apportionment across this share class. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | An optional set of properties to attach to the auto-created Instrument. Only applied when createInstrument is true. |
| **fund_share_class_type** | **str** | Required | The Type of Share Class. Supported values are: Unitised / Non-Unitised / Series / Private Equity / Partnership. |
| **distribution_type** | **str** | Required | The type of distribution the ShareClass will calculate. Supported values are: Income, Accumulation. |
| **dom_ccy** | **str** | Required | The domestic currency of the ShareClass instrument. |
| **trading_conventions** | [TradingConventions](TradingConventions.md) | Optional | *No description available.* |
| **units_precision** | **int** | Optional | Decimal places for the share class units. |
| **price_precision** | **int** | Optional | Decimal places for the share class price. |
| **rounding_conventions** | [List[SimpleRoundingConvention]](SimpleRoundingConvention.md) | Optional | Rounding conventions used for the ShareClass quotes. |
| **rounding_conventions_units** | [List[SimpleRoundingConvention]](SimpleRoundingConvention.md) | Optional | Rounding conventions used for the ShareClass units. |
| **time_zone_conventions** | [TimeZoneConventions](TimeZoneConventions.md) | Optional | *No description available.* |
| **distribution_payment_type** | **str** | Optional | The tax treatment applied to distributions. Supported values are: Gross, Net. |
| **hedging** | **str** | Required | Indicates whether the ShareClass applies currency hedging. Supported values are: Invalid, None, ApplyHedging. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ShareClass import ShareClass

instance = ShareClass(
    instrument_identifiers=,  # required — Unique instrument identifiers
    series=[],  # optional — The series that belong to this Share Class.
    code="...",  # required — The unique code for the Share Class. Must be unique within the Fund.
    name="...",  # required — The display name of the Share Class.
    description="...",  # optional — An optional description for the Share Class.
    share_class_short_code="...",  # required — A short code that uniquely identifies the share class within the Fund.
    launch_price=0.0,  # optional — The launch price set when a shareclass is added to the fund. Defaults to 1.
    launch_date=datetime.now(),  # optional — The launch date set when a shareclass is added to the fund. Defaults to Fund Inception Date.
    apportionment_factor=0.0,  # optional — The weighting factor used for apportionment across this share class.
    properties=ModelProperty(...),  # optional — An optional set of properties to attach to the auto-created Instrument. Only applied when createInstrument is true.
    fund_share_class_type="...",  # required — The Type of Share Class. Supported values are: Unitised / Non-Unitised / Series / Private Equity / Partnership.
    distribution_type="...",  # required — The type of distribution the ShareClass will calculate. Supported values are: Income, Accumulation.
    dom_ccy="...",  # required — The domestic currency of the ShareClass instrument.
    trading_conventions=TradingConventions(...),  # optional
    units_precision=0,  # optional — Decimal places for the share class units.
    price_precision=0,  # optional — Decimal places for the share class price.
    rounding_conventions=[],  # optional — Rounding conventions used for the ShareClass quotes.
    rounding_conventions_units=[],  # optional — Rounding conventions used for the ShareClass units.
    time_zone_conventions=TimeZoneConventions(...),  # optional
    distribution_payment_type="...",  # optional — The tax treatment applied to distributions. Supported values are: Gross, Net.
    hedging="..."  # required — Indicates whether the ShareClass applies currency hedging. Supported values are: Invalid, None, ApplyHedging.
)
```

- [Series](Series.md) — used in `series`
- [ModelProperty](ModelProperty.md) — used in `properties`
- [TradingConventions](TradingConventions.md)
- [SimpleRoundingConvention](SimpleRoundingConvention.md) — used in `rounding_conventions`
- [SimpleRoundingConvention](SimpleRoundingConvention.md) — used in `rounding_conventions_units`
- [TimeZoneConventions](TimeZoneConventions.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

