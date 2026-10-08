# CreateTransferRequest

A request to create a transfer: the paired transaction legs that move a position, and the Transfer entity  recording them.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **transfer_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **portfolio_id_out** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **portfolio_id_in** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **instrument_identifier_out** | **str** | Required | The LUSID instrument id of the instrument moving out. A position in this instrument must exist in the outgoing portfolio on the outgoing trade date. |
| **instrument_identifier_in** | **str** | Required | The LUSID instrument id of the instrument moving in. Equal to InstrumentIdentifierOut for a transfer between portfolios. |
| **pricing_method** | **str** | Required | How the legs are priced. &#39;AtCost&#39; uses the cost per unit of the outgoing holding; &#39;AtPrice&#39; uses the supplied TransactionPriceOut, which is then required. Available values: AtCost, AtPrice. |
| **tax_lot_structure** | **str** | Optional | What happens to the tax lots of the outgoing position. Only &#39;Consolidate&#39; is currently supported; &#39;Preserve&#39; is rejected. Defaults to &#39;Consolidate&#39;. Available values: Consolidate, Preserve. |
| **units_out** | **float** | Required | The number of units to move out. Must be greater than zero. |
| **units_in** | **float** | Required | The number of units to move in. Must be greater than zero. |
| **amount_out** | **float** | Optional | The total consideration of the outgoing leg. Recorded, not applied. |
| **weight_out** | **float** | Optional | The weighting factor of the outgoing leg. Recorded, not applied. |
| **trade_date_out** | **datetime** | Required | The trade date of the outgoing leg. Must not be later than TradeDateIn. |
| **trade_date_in** | **datetime** | Required | The trade date of the incoming leg. |
| **settlement_date_out** | **datetime** | Required | The settlement date of the outgoing leg. Must not be later than SettlementDateIn. |
| **settlement_date_in** | **datetime** | Optional | The settlement date of the incoming leg. Defaults to SettlementDateOut when not supplied. |
| **exchange_rate_out** | **float** | Optional | The FX rate to apply to the outgoing leg. |
| **exchange_rate_in** | **float** | Optional | The FX rate to apply to the incoming leg. |
| **transaction_price_out** | **float** | Optional | The unit price of the outgoing leg. Required when PricingMethod is &#39;AtPrice&#39;, and ignored when it is &#39;AtCost&#39;. |
| **transaction_price_in** | **float** | Optional | The unit price of the incoming leg. Ignored for a transfer, which carries the outgoing price across; defaults to the outgoing price for a switch. |
| **counterparty_id_out** | **str** | Optional | The counterparty identifier of the outgoing leg. |
| **counterparty_id_in** | **str** | Optional | The counterparty identifier of the incoming leg. Defaults to CounterpartyIdOut. |
| **custodian_account_id_out** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **custodian_account_id_in** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **source** | **str** | Required | The transaction source the generated legs are booked against. |
| **accounting_method** | **str** | Optional | An accounting method to record against the transfer. Available values: AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst, ProRateByUnits, ProRateByCost, ProRateByCostPortfolioCurrency, IntraDayThenFirstInFirstOut, LongTermHighestCostFirst, LongTermHighestCostFirstPortfolioCurrency, HighestCostFirstPortfolioCurrency, LowestCostFirstPortfolioCurrency, MaximumLossMinimumGain, MaximumLossMinimumGainPortfolioCurrency. |
| **properties_out** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | Transaction Properties to set on the outgoing transaction leg, and on the incoming transaction leg when PropertiesIn is absent. Supplying an empty collection for PropertiesIn leaves the incoming leg with no properties. |
| **properties_in** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | Transaction Properties to set on the incoming transaction leg, replacing rather than adding to PropertiesOut. |
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | Properties to set on the transfer itself, in the Transfer domain. These are separate from PropertiesOut and PropertiesIn, which are Transaction domain and land on the legs. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CreateTransferRequest import CreateTransferRequest

instance = CreateTransferRequest(
    transfer_id=ResourceId(...),  # required
    portfolio_id_out=ResourceId(...),  # required
    portfolio_id_in=ResourceId(...),  # required
    instrument_identifier_out="...",  # required — The LUSID instrument id of the instrument moving out. A position in this instrument must exist in the outgoing portfolio on the outgoing trade date.
    instrument_identifier_in="...",  # required — The LUSID instrument id of the instrument moving in. Equal to InstrumentIdentifierOut for a transfer between portfolios.
    pricing_method="...",  # required — How the legs are priced. &#39;AtCost&#39; uses the cost per unit of the outgoing holding; &#39;AtPrice&#39; uses the supplied TransactionPriceOut, which is then required. Available values: AtCost, AtPrice.
    tax_lot_structure="...",  # optional — What happens to the tax lots of the outgoing position. Only &#39;Consolidate&#39; is currently supported; &#39;Preserve&#39; is rejected. Defaults to &#39;Consolidate&#39;. Available values: Consolidate, Preserve.
    units_out=0.0,  # required — The number of units to move out. Must be greater than zero.
    units_in=0.0,  # required — The number of units to move in. Must be greater than zero.
    amount_out=0.0,  # optional — The total consideration of the outgoing leg. Recorded, not applied.
    weight_out=0.0,  # optional — The weighting factor of the outgoing leg. Recorded, not applied.
    trade_date_out=datetime.now(),  # required — The trade date of the outgoing leg. Must not be later than TradeDateIn.
    trade_date_in=datetime.now(),  # required — The trade date of the incoming leg.
    settlement_date_out=datetime.now(),  # required — The settlement date of the outgoing leg. Must not be later than SettlementDateIn.
    settlement_date_in=datetime.now(),  # optional — The settlement date of the incoming leg. Defaults to SettlementDateOut when not supplied.
    exchange_rate_out=0.0,  # optional — The FX rate to apply to the outgoing leg.
    exchange_rate_in=0.0,  # optional — The FX rate to apply to the incoming leg.
    transaction_price_out=0.0,  # optional — The unit price of the outgoing leg. Required when PricingMethod is &#39;AtPrice&#39;, and ignored when it is &#39;AtCost&#39;.
    transaction_price_in=0.0,  # optional — The unit price of the incoming leg. Ignored for a transfer, which carries the outgoing price across; defaults to the outgoing price for a switch.
    counterparty_id_out="...",  # optional — The counterparty identifier of the outgoing leg.
    counterparty_id_in="...",  # optional — The counterparty identifier of the incoming leg. Defaults to CounterpartyIdOut.
    custodian_account_id_out=ResourceId(...),  # optional
    custodian_account_id_in=ResourceId(...),  # optional
    source="...",  # required — The transaction source the generated legs are booked against.
    accounting_method="...",  # optional — An accounting method to record against the transfer. Available values: AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst, ProRateByUnits, ProRateByCost, ProRateByCostPortfolioCurrency, IntraDayThenFirstInFirstOut, LongTermHighestCostFirst, LongTermHighestCostFirstPortfolioCurrency, HighestCostFirstPortfolioCurrency, LowestCostFirstPortfolioCurrency, MaximumLossMinimumGain, MaximumLossMinimumGainPortfolioCurrency.
    properties_out=PerpetualProperty(...),  # optional — Transaction Properties to set on the outgoing transaction leg, and on the incoming transaction leg when PropertiesIn is absent. Supplying an empty collection for PropertiesIn leaves the incoming leg with no properties.
    properties_in=PerpetualProperty(...),  # optional — Transaction Properties to set on the incoming transaction leg, replacing rather than adding to PropertiesOut.
    properties=PerpetualProperty(...)  # optional — Properties to set on the transfer itself, in the Transfer domain. These are separate from PropertiesOut and PropertiesIn, which are Transaction domain and land on the legs.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [PerpetualProperty](PerpetualProperty.md) — used in `properties_out`
- [PerpetualProperty](PerpetualProperty.md) — used in `properties_in`
- [PerpetualProperty](PerpetualProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

