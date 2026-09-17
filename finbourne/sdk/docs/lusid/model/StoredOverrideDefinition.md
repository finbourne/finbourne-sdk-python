# StoredOverrideDefinition

A single replacement transaction definition as it was persisted against a virtual transaction.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **transaction_id** | **str** | Optional | The unique identifier of the replacement transaction. |
| **type** | **str** | Optional | The type of the replacement transaction, for example &#39;Buy&#39; or &#39;Sell&#39;. |
| **instrument_identifiers** | **Dict[str, Optional[str]]** | Optional | A set of instrument identifiers that resolve the replacement transaction to a unique instrument. |
| **trade_date** | **str** | Optional | The trade date of the replacement transaction. |
| **settlement_date** | **str** | Optional | The settlement date of the replacement transaction. |
| **units** | **float** | Optional | The number of units of the transacted instrument. |
| **trade_price** | [TransactionPrice](TransactionPrice.md) | Optional | *No description available.* |
| **total_consideration** | [CurrencyAndAmount](CurrencyAndAmount.md) | Optional | *No description available.* |
| **exchange_rate** | **float** | Optional | The exchange rate between the trade and settlement currency. |
| **trade_currency** | **str** | Optional | The trade currency of the replacement transaction. |
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | The transaction properties stored for the replacement transaction. |
| **counterparty_id** | **str** | Optional | The identifier for the counterparty of the replacement transaction. |
| **source** | **str** | Optional | The source of the replacement transaction. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.StoredOverrideDefinition import StoredOverrideDefinition

instance = StoredOverrideDefinition(
    transaction_id="...",  # optional — The unique identifier of the replacement transaction.
    type="...",  # optional — The type of the replacement transaction, for example &#39;Buy&#39; or &#39;Sell&#39;.
    instrument_identifiers=,  # optional — A set of instrument identifiers that resolve the replacement transaction to a unique instrument.
    trade_date="...",  # optional — The trade date of the replacement transaction.
    settlement_date="...",  # optional — The settlement date of the replacement transaction.
    units=0.0,  # optional — The number of units of the transacted instrument.
    trade_price=TransactionPrice(...),  # optional
    total_consideration=CurrencyAndAmount(...),  # optional
    exchange_rate=0.0,  # optional — The exchange rate between the trade and settlement currency.
    trade_currency="...",  # optional — The trade currency of the replacement transaction.
    properties=PerpetualProperty(...),  # optional — The transaction properties stored for the replacement transaction.
    counterparty_id="...",  # optional — The identifier for the counterparty of the replacement transaction.
    source="..."  # optional — The source of the replacement transaction.
)
```

- [TransactionPrice](TransactionPrice.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [PerpetualProperty](PerpetualProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

