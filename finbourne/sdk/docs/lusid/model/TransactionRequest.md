# TransactionRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **transaction_id** | **str** | Required | The unique identifier of the transaction. |
| **type** | **str** | Required | The type of the transaction, for example &#39;Buy&#39; or &#39;Sell&#39;. The transaction type must have been pre-configured using the System Configuration API. If not, this operation will succeed but you are not able to calculate holdings for the portfolio that include this transaction. |
| **instrument_identifiers** | **Dict[str, Optional[str]]** | Required | A set of instrument identifiers that can resolve the transaction to a unique instrument. |
| **transaction_date** | **str** | Required | The date of the transaction. |
| **settlement_date** | **str** | Required | The settlement date of the transaction. |
| **units** | **float** | Required | The number of units of the transacted instrument. |
| **transaction_price** | [TransactionPrice](TransactionPrice.md) | Optional | *No description available.* |
| **total_consideration** | [CurrencyAndAmount](CurrencyAndAmount.md) | Required | *No description available.* |
| **exchange_rate** | **float** | Optional | The exchange rate between the transaction and settlement currency (settlement currency being represented by TotalConsideration.Currency). For example, if the transaction currency is USD and the settlement currency is GBP, this would be the appropriate USD/GBP rate. |
| **transaction_currency** | **str** | Optional | The transaction currency. |
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | A list of unique transaction properties and associated values to store for the transaction. Each property must be from the &#39;Transaction&#39; domain. |
| **counterparty_id** | **str** | Optional | The identifier for the counterparty of the transaction. |
| **source** | **str** | Optional | The source of the transaction. This is used to look up the appropriate transaction group set in the transaction type configuration. |
| **otc_confirmation** | [OtcConfirmation](OtcConfirmation.md) | Optional | *No description available.* |
| **order_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **allocation_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **custodian_account_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **transaction_group_id** | **str** | Optional | The identifier for grouping economic events across multiple transactions |
| **strategy_tag** | [List[Strategy]](Strategy.md) | Optional | A list of strategies representing the allocation of units across multiple sub-holding keys |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransactionRequest import TransactionRequest

instance = TransactionRequest(
    transaction_id="...",  # required — The unique identifier of the transaction.
    type="...",  # required — The type of the transaction, for example &#39;Buy&#39; or &#39;Sell&#39;. The transaction type must have been pre-configured using the System Configuration API. If not, this operation will succeed but you are not able to calculate holdings for the portfolio that include this transaction.
    instrument_identifiers=,  # required — A set of instrument identifiers that can resolve the transaction to a unique instrument.
    transaction_date="...",  # required — The date of the transaction.
    settlement_date="...",  # required — The settlement date of the transaction.
    units=0.0,  # required — The number of units of the transacted instrument.
    transaction_price=TransactionPrice(...),  # optional
    total_consideration=CurrencyAndAmount(...),  # required
    exchange_rate=0.0,  # optional — The exchange rate between the transaction and settlement currency (settlement currency being represented by TotalConsideration.Currency). For example, if the transaction currency is USD and the settlement currency is GBP, this would be the appropriate USD/GBP rate.
    transaction_currency="...",  # optional — The transaction currency.
    properties=PerpetualProperty(...),  # optional — A list of unique transaction properties and associated values to store for the transaction. Each property must be from the &#39;Transaction&#39; domain.
    counterparty_id="...",  # optional — The identifier for the counterparty of the transaction.
    source="...",  # optional — The source of the transaction. This is used to look up the appropriate transaction group set in the transaction type configuration.
    otc_confirmation=OtcConfirmation(...),  # optional
    order_id=ResourceId(...),  # optional
    allocation_id=ResourceId(...),  # optional
    custodian_account_id=ResourceId(...),  # optional
    transaction_group_id="...",  # optional — The identifier for grouping economic events across multiple transactions
    strategy_tag=[]  # optional — A list of strategies representing the allocation of units across multiple sub-holding keys
)
```

- [TransactionPrice](TransactionPrice.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [PerpetualProperty](PerpetualProperty.md) — used in `properties`
- [OtcConfirmation](OtcConfirmation.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [Strategy](Strategy.md) — used in `strategy_tag`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

