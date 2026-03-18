# PortfolioHolding

A list of holdings.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instrument_scope** | **str** | Optional | The scope in which the holding&#39;s instrument is in. |
| **instrument_uid** | **str** | Required | The unique Lusid Instrument Id (LUID) of the instrument that the holding is in. |
| **sub_holding_keys** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | The sub-holding properties which identify the holding. Each property will be from the &#39;Transaction&#39; domain. These are configured on a transaction portfolio. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | The properties which have been requested to be decorated onto the holding. These will be from the &#39;Instrument&#39; or &#39;Holding&#39; domain. |
| **holding_type** | **str** | Required | The code for the type of the holding e.g. P, B, C, R, F etc. |
| **units** | **float** | Required | The total number of units of the holding. |
| **settled_units** | **float** | Required | The total number of settled units of the holding. |
| **cost** | [CurrencyAndAmount](CurrencyAndAmount.md) | Required | *No description available.* |
| **cost_portfolio_ccy** | [CurrencyAndAmount](CurrencyAndAmount.md) | Required | *No description available.* |
| **transaction** | [Transaction](Transaction.md) | Optional | *No description available.* |
| **currency** | **str** | Optional | The holding currency. |
| **holding_type_name** | **str** | Optional | The decoded type of the holding e.g. Position, Balance, CashCommitment, Receivable, ForwardFX etc. |
| **holding_id** | **int** | Optional | A single identifier for the holding within the portfolio. The holdingId is constructed from the LusidInstrumentId, sub-holding keys and currrency and is unique within the portfolio. |
| **notional_cost** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **amortised_cost** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **amortised_cost_portfolio_ccy** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **variation_margin** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **variation_margin_portfolio_ccy** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **settlement_schedule** | [List[SettlementSchedule]](SettlementSchedule.md) | Optional | Where no. of days ahead has been specified, future dated settlements will be captured here. |
| **current_face** | **float** | Optional | Current face value of the holding. |
| **custodian_account_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **unsettled_units** | **float** | Optional | The number of unsettled units for the holding. |
| **overdue_units** | **float** | Optional | The number of unsettled units for the holding that are beyond their contractual settlement date. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PortfolioHolding import PortfolioHolding

instance = PortfolioHolding(
    instrument_scope="...",  # optional — The scope in which the holding&#39;s instrument is in.
    instrument_uid="...",  # required — The unique Lusid Instrument Id (LUID) of the instrument that the holding is in.
    sub_holding_keys=PerpetualProperty(...),  # optional — The sub-holding properties which identify the holding. Each property will be from the &#39;Transaction&#39; domain. These are configured on a transaction portfolio.
    properties=ModelProperty(...),  # optional — The properties which have been requested to be decorated onto the holding. These will be from the &#39;Instrument&#39; or &#39;Holding&#39; domain.
    holding_type="...",  # required — The code for the type of the holding e.g. P, B, C, R, F etc.
    units=0.0,  # required — The total number of units of the holding.
    settled_units=0.0,  # required — The total number of settled units of the holding.
    cost=CurrencyAndAmount(...),  # required
    cost_portfolio_ccy=CurrencyAndAmount(...),  # required
    transaction=Transaction(...),  # optional
    currency="...",  # optional — The holding currency.
    holding_type_name="...",  # optional — The decoded type of the holding e.g. Position, Balance, CashCommitment, Receivable, ForwardFX etc.
    holding_id=0,  # optional — A single identifier for the holding within the portfolio. The holdingId is constructed from the LusidInstrumentId, sub-holding keys and currrency and is unique within the portfolio.
    notional_cost=CurrencyAndAmount(...),  # optional
    amortised_cost=CurrencyAndAmount(...),  # optional
    amortised_cost_portfolio_ccy=CurrencyAndAmount(...),  # optional
    variation_margin=CurrencyAndAmount(...),  # optional
    variation_margin_portfolio_ccy=CurrencyAndAmount(...),  # optional
    settlement_schedule=[],  # optional — Where no. of days ahead has been specified, future dated settlements will be captured here.
    current_face=0.0,  # optional — Current face value of the holding.
    custodian_account_id=ResourceId(...),  # optional
    unsettled_units=0.0,  # optional — The number of unsettled units for the holding.
    overdue_units=0.0  # optional — The number of unsettled units for the holding that are beyond their contractual settlement date.
)
```

- [PerpetualProperty](PerpetualProperty.md) — used in `sub_holding_keys`
- [ModelProperty](ModelProperty.md) — used in `properties`
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [Transaction](Transaction.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [SettlementSchedule](SettlementSchedule.md) — used in `settlement_schedule`
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

