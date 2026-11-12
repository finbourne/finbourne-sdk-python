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
| **tax_lot_structure** | **str** | Optional | What happens to the tax lots of the outgoing position. Defaults to &#39;Consolidate&#39;. &#39;Preserve&#39; carries each outgoing lot onto the incoming position; it is not supported when the incoming portfolio uses the AverageCost or Default accounting method, or across share classes in different currencies. Available values: Consolidate, Preserve. |
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
| **transaction_price_in** | **float** | Optional | The unit price of the incoming leg. Not accepted for a transfer of one instrument between portfolios, which carries the outgoing price across. For a switch, required when PricingMethod is &#39;AtPrice&#39; and defaults to the outgoing price otherwise. |
| **counterparty_id_out** | **str** | Optional | The counterparty identifier of the outgoing leg. |
| **counterparty_id_in** | **str** | Optional | The counterparty identifier of the incoming leg. Defaults to CounterpartyIdOut. |
| **custodian_account_id_out** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **custodian_account_id_in** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **source_out** | **str** | Optional | The transaction source the outgoing leg is booked against, and the incoming leg too when SourceIn is not supplied. Defaults to &#39;default&#39;. |
| **accounting_method** | **str** | Optional | An accounting method to record against the transfer. Available values: AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst, ProRateByUnits, ProRateByCost, ProRateByCostPortfolioCurrency, IntraDayThenFirstInFirstOut, LongTermHighestCostFirst, LongTermHighestCostFirstPortfolioCurrency, HighestCostFirstPortfolioCurrency, LowestCostFirstPortfolioCurrency, MaximumLossMinimumGain, MaximumLossMinimumGainPortfolioCurrency. |
| **properties_out** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | Transaction Properties to set on the outgoing transaction leg, and on the incoming transaction leg when PropertiesIn is absent. Supplying an empty collection for PropertiesIn leaves the incoming leg with no properties. |
| **properties_in** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | Transaction Properties to set on the incoming transaction leg, replacing rather than adding to PropertiesOut. |
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | Properties to set on the transfer itself, in the Transfer domain. These are separate from PropertiesOut and PropertiesIn, which are Transaction domain and land on the legs. |
| **transaction_to_portfolio_rate_out** | **float** | Optional | The rate from the outgoing leg&#39;s trade currency to the outgoing portfolio&#39;s base currency, applied whenever supplied. |
| **transaction_to_portfolio_rate_in** | **float** | Optional | The rate from the incoming leg&#39;s trade currency to the incoming portfolio&#39;s base currency. Required when the two portfolios have different base currencies, and applied whenever supplied. |
| **source_in** | **str** | Optional | The transaction source the incoming leg is booked against. Defaults to SourceOut. |
| **transaction_type_out** | **str** | Optional | The transaction type to book the outgoing leg as. Supply it together with TransactionTypeIn, or supply neither. If not supplied, it will be derived from the transfer type. It must be a different type from TransactionTypeIn, must be configured under SourceOut in the transaction type scope of PortfolioIdOut, and must reduce a position. |
| **transaction_type_in** | **str** | Optional | The transaction type to book the incoming leg as. Supply it together with TransactionTypeOut, or supply neither. If not supplied, it will be derived from the transfer type. It must be configured under SourceIn in the transaction type scope of PortfolioIdIn, and must increase a position. |


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
    tax_lot_structure="...",  # optional — What happens to the tax lots of the outgoing position. Defaults to &#39;Consolidate&#39;. &#39;Preserve&#39; carries each outgoing lot onto the incoming position; it is not supported when the incoming portfolio uses the AverageCost or Default accounting method, or across share classes in different currencies. Available values: Consolidate, Preserve.
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
    transaction_price_in=0.0,  # optional — The unit price of the incoming leg. Not accepted for a transfer of one instrument between portfolios, which carries the outgoing price across. For a switch, required when PricingMethod is &#39;AtPrice&#39; and defaults to the outgoing price otherwise.
    counterparty_id_out="...",  # optional — The counterparty identifier of the outgoing leg.
    counterparty_id_in="...",  # optional — The counterparty identifier of the incoming leg. Defaults to CounterpartyIdOut.
    custodian_account_id_out=ResourceId(...),  # optional
    custodian_account_id_in=ResourceId(...),  # optional
    source_out="...",  # optional — The transaction source the outgoing leg is booked against, and the incoming leg too when SourceIn is not supplied. Defaults to &#39;default&#39;.
    accounting_method="...",  # optional — An accounting method to record against the transfer. Available values: AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst, ProRateByUnits, ProRateByCost, ProRateByCostPortfolioCurrency, IntraDayThenFirstInFirstOut, LongTermHighestCostFirst, LongTermHighestCostFirstPortfolioCurrency, HighestCostFirstPortfolioCurrency, LowestCostFirstPortfolioCurrency, MaximumLossMinimumGain, MaximumLossMinimumGainPortfolioCurrency.
    properties_out=PerpetualProperty(...),  # optional — Transaction Properties to set on the outgoing transaction leg, and on the incoming transaction leg when PropertiesIn is absent. Supplying an empty collection for PropertiesIn leaves the incoming leg with no properties.
    properties_in=PerpetualProperty(...),  # optional — Transaction Properties to set on the incoming transaction leg, replacing rather than adding to PropertiesOut.
    properties=PerpetualProperty(...),  # optional — Properties to set on the transfer itself, in the Transfer domain. These are separate from PropertiesOut and PropertiesIn, which are Transaction domain and land on the legs.
    transaction_to_portfolio_rate_out=0.0,  # optional — The rate from the outgoing leg&#39;s trade currency to the outgoing portfolio&#39;s base currency, applied whenever supplied.
    transaction_to_portfolio_rate_in=0.0,  # optional — The rate from the incoming leg&#39;s trade currency to the incoming portfolio&#39;s base currency. Required when the two portfolios have different base currencies, and applied whenever supplied.
    source_in="...",  # optional — The transaction source the incoming leg is booked against. Defaults to SourceOut.
    transaction_type_out="...",  # optional — The transaction type to book the outgoing leg as. Supply it together with TransactionTypeIn, or supply neither. If not supplied, it will be derived from the transfer type. It must be a different type from TransactionTypeIn, must be configured under SourceOut in the transaction type scope of PortfolioIdOut, and must reduce a position.
    transaction_type_in="..."  # optional — The transaction type to book the incoming leg as. Supply it together with TransactionTypeOut, or supply neither. If not supplied, it will be derived from the transfer type. It must be configured under SourceIn in the transaction type scope of PortfolioIdIn, and must increase a position.
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

