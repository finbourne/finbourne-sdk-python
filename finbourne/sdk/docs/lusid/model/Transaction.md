# Transaction

A list of transactions.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **transaction_id** | **str** | Required | The unique identifier for the transaction. |
| **type** | **str** | Required | The type of the transaction e.g. &#39;Buy&#39;, &#39;Sell&#39;. The transaction type should have been pre-configured via the System Configuration API endpoint. |
| **instrument_identifiers** | **Dict[str, Optional[str]]** | Optional | A set of instrument identifiers that can resolve the transaction to a unique instrument. |
| **instrument_scope** | **str** | Optional | The scope in which the transaction&#39;s instrument lies. |
| **instrument_uid** | **str** | Required | The unique Lusid Instrument Id (LUID) of the instrument that the transaction is in. |
| **transaction_date** | **datetime** | Required | The date of the transaction. |
| **settlement_date** | **datetime** | Required | The settlement date of the transaction. |
| **units** | **float** | Required | The number of units transacted in the associated instrument. |
| **transaction_price** | [TransactionPrice](TransactionPrice.md) | Optional | *No description available.* |
| **total_consideration** | [CurrencyAndAmount](CurrencyAndAmount.md) | Required | *No description available.* |
| **exchange_rate** | **float** | Optional | The exchange rate between the transaction and settlement currency (settlement currency being represented by the TotalConsideration.Currency). For example if the transaction currency is in USD and the settlement currency is in GBP this this the USD/GBP rate. |
| **transaction_currency** | **str** | Optional | The transaction currency. |
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | Set of unique transaction properties and associated values to stored with the transaction. Each property will be from the &#39;Transaction&#39; domain. |
| **counterparty_id** | **str** | Optional | The identifier for the counterparty of the transaction. |
| **source** | **str** | Optional | The source of the transaction. This is used to look up the appropriate transaction group set in the transaction type configuration. |
| **entry_date_time** | **datetime** | Optional | The asAt datetime that the transaction was added to LUSID. |
| **otc_confirmation** | [OtcConfirmation](OtcConfirmation.md) | Optional | *No description available.* |
| **transaction_status** | **str** | Optional | The status of the transaction. The available values are: Active, Amended, Cancelled, ActiveReversal, ActiveTrueUp, CancelledTrueUp |
| **cancel_date_time** | **datetime** | Optional | If the transaction has been cancelled, the asAt datetime that the transaction was cancelled. |
| **order_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **allocation_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **custodian_account** | [CustodianAccount](CustodianAccount.md) | Optional | *No description available.* |
| **transaction_group_id** | **str** | Optional | The identifier for grouping economic events across multiple transactions |
| **strategy_tag** | [List[Strategy]](Strategy.md) | Optional | A list of strategies representing the allocation of units across multiple sub-holding keys |
| **resolved_transaction_type_details** | [TransactionTypeDetails](TransactionTypeDetails.md) | Optional | *No description available.* |
| **data_model_membership** | [DataModelMembership](DataModelMembership.md) | Optional | *No description available.* |
| **version** | [Version](Version.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.Transaction import Transaction

instance = Transaction(
    transaction_id="...",  # required — The unique identifier for the transaction.
    type="...",  # required — The type of the transaction e.g. &#39;Buy&#39;, &#39;Sell&#39;. The transaction type should have been pre-configured via the System Configuration API endpoint.
    instrument_identifiers=,  # optional — A set of instrument identifiers that can resolve the transaction to a unique instrument.
    instrument_scope="...",  # optional — The scope in which the transaction&#39;s instrument lies.
    instrument_uid="...",  # required — The unique Lusid Instrument Id (LUID) of the instrument that the transaction is in.
    transaction_date=datetime.now(),  # required — The date of the transaction.
    settlement_date=datetime.now(),  # required — The settlement date of the transaction.
    units=0.0,  # required — The number of units transacted in the associated instrument.
    transaction_price=TransactionPrice(...),  # optional
    total_consideration=CurrencyAndAmount(...),  # required
    exchange_rate=0.0,  # optional — The exchange rate between the transaction and settlement currency (settlement currency being represented by the TotalConsideration.Currency). For example if the transaction currency is in USD and the settlement currency is in GBP this this the USD/GBP rate.
    transaction_currency="...",  # optional — The transaction currency.
    properties=PerpetualProperty(...),  # optional — Set of unique transaction properties and associated values to stored with the transaction. Each property will be from the &#39;Transaction&#39; domain.
    counterparty_id="...",  # optional — The identifier for the counterparty of the transaction.
    source="...",  # optional — The source of the transaction. This is used to look up the appropriate transaction group set in the transaction type configuration.
    entry_date_time=datetime.now(),  # optional — The asAt datetime that the transaction was added to LUSID.
    otc_confirmation=OtcConfirmation(...),  # optional
    transaction_status="...",  # optional — The status of the transaction. The available values are: Active, Amended, Cancelled, ActiveReversal, ActiveTrueUp, CancelledTrueUp
    cancel_date_time=datetime.now(),  # optional — If the transaction has been cancelled, the asAt datetime that the transaction was cancelled.
    order_id=ResourceId(...),  # optional
    allocation_id=ResourceId(...),  # optional
    custodian_account=CustodianAccount(...),  # optional
    transaction_group_id="...",  # optional — The identifier for grouping economic events across multiple transactions
    strategy_tag=[],  # optional — A list of strategies representing the allocation of units across multiple sub-holding keys
    resolved_transaction_type_details=TransactionTypeDetails(...),  # optional
    data_model_membership=DataModelMembership(...),  # optional
    version=Version(...)  # optional
)
```

- [TransactionPrice](TransactionPrice.md)
- [CurrencyAndAmount](CurrencyAndAmount.md)
- [PerpetualProperty](PerpetualProperty.md) — used in `properties`
- [OtcConfirmation](OtcConfirmation.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [CustodianAccount](CustodianAccount.md)
- [Strategy](Strategy.md) — used in `strategy_tag`
- [TransactionTypeDetails](TransactionTypeDetails.md)
- [DataModelMembership](DataModelMembership.md)
- [Version](Version.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

