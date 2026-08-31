# CreateTransferRequest

A request to create a transfer: the paired transaction legs that move a position, and the Transfer entity  recording them.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **transfer_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **portfolio_id_out** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **portfolio_id_in** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **instrument_identifier_out** | **str** | Required | *No description available.* |
| **instrument_identifier_in** | **str** | Required | *No description available.* |
| **pricing_method** | **str** | Required | Available values: AtCost, AtPrice. |
| **tax_lot_structure** | **str** | Optional | Available values: Consolidate, Preserve. |
| **units_out** | **float** | Required | *No description available.* |
| **units_in** | **float** | Required | *No description available.* |
| **amount_out** | **float** | Optional | *No description available.* |
| **weight_out** | **float** | Optional | *No description available.* |
| **trade_date_out** | **datetime** | Required | *No description available.* |
| **trade_date_in** | **datetime** | Required | *No description available.* |
| **settlement_date_out** | **datetime** | Required | *No description available.* |
| **settlement_date_in** | **datetime** | Optional | *No description available.* |
| **exchange_rate_out** | **float** | Optional | *No description available.* |
| **exchange_rate_in** | **float** | Optional | *No description available.* |
| **transaction_price_out** | **float** | Optional | *No description available.* |
| **transaction_price_in** | **float** | Optional | *No description available.* |
| **counterparty_id_out** | **str** | Optional | *No description available.* |
| **counterparty_id_in** | **str** | Optional | *No description available.* |
| **custodian_account_id_out** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **custodian_account_id_in** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **source** | **str** | Required | *No description available.* |
| **accounting_method** | **str** | Optional | Available values: AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst, ProRateByUnits, ProRateByCost, ProRateByCostPortfolioCurrency, IntraDayThenFirstInFirstOut, LongTermHighestCostFirst, LongTermHighestCostFirstPortfolioCurrency, HighestCostFirstPortfolioCurrency, LowestCostFirstPortfolioCurrency, MaximumLossMinimumGain, MaximumLossMinimumGainPortfolioCurrency. |
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | *No description available.* |
| **properties_in** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CreateTransferRequest import CreateTransferRequest

instance = CreateTransferRequest(
    transfer_id=ResourceId(...),  # required
    portfolio_id_out=ResourceId(...),  # required
    portfolio_id_in=ResourceId(...),  # required
    instrument_identifier_out="...",  # required
    instrument_identifier_in="...",  # required
    pricing_method="...",  # required — Available values: AtCost, AtPrice.
    tax_lot_structure="...",  # optional — Available values: Consolidate, Preserve.
    units_out=0.0,  # required
    units_in=0.0,  # required
    amount_out=0.0,  # optional
    weight_out=0.0,  # optional
    trade_date_out=datetime.now(),  # required
    trade_date_in=datetime.now(),  # required
    settlement_date_out=datetime.now(),  # required
    settlement_date_in=datetime.now(),  # optional
    exchange_rate_out=0.0,  # optional
    exchange_rate_in=0.0,  # optional
    transaction_price_out=0.0,  # optional
    transaction_price_in=0.0,  # optional
    counterparty_id_out="...",  # optional
    counterparty_id_in="...",  # optional
    custodian_account_id_out=ResourceId(...),  # optional
    custodian_account_id_in=ResourceId(...),  # optional
    source="...",  # required
    accounting_method="...",  # optional — Available values: AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst, ProRateByUnits, ProRateByCost, ProRateByCostPortfolioCurrency, IntraDayThenFirstInFirstOut, LongTermHighestCostFirst, LongTermHighestCostFirstPortfolioCurrency, HighestCostFirstPortfolioCurrency, LowestCostFirstPortfolioCurrency, MaximumLossMinimumGain, MaximumLossMinimumGainPortfolioCurrency.
    properties=PerpetualProperty(...),  # optional
    properties_in=PerpetualProperty(...)  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [PerpetualProperty](PerpetualProperty.md)
- [PerpetualProperty](PerpetualProperty.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

