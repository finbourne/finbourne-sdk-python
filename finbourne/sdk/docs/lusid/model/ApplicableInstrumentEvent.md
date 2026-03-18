# ApplicableInstrumentEvent

Represents applicable instrument event.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **portfolio_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **holding_id** | **int** | Required | *No description available.* |
| **lusid_instrument_id** | **str** | Required | *No description available.* |
| **instrument_scope** | **str** | Required | *No description available.* |
| **instrument_type** | **str** | Required | *No description available.* |
| **instrument_event_type** | **str** | Required | *No description available.* |
| **instrument_event_id** | **str** | Required | *No description available.* |
| **generated_event** | [InstrumentEventHolder](InstrumentEventHolder.md) | Optional | *No description available.* |
| **generated_event_diagnostics** | [GeneratedEventDiagnostics](GeneratedEventDiagnostics.md) | Optional | *No description available.* |
| **loaded_event** | [InstrumentEventHolder](InstrumentEventHolder.md) | Optional | *No description available.* |
| **applied_instrument_event_instruction_id** | **str** | Optional | *No description available.* |
| **transactions** | [List[Transaction]](Transaction.md) | Optional | *No description available.* |
| **transaction_diagnostics** | [TransactionDiagnostics](TransactionDiagnostics.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ApplicableInstrumentEvent import ApplicableInstrumentEvent

instance = ApplicableInstrumentEvent(
    portfolio_id=ResourceId(...),  # required
    holding_id=0,  # required
    lusid_instrument_id="...",  # required
    instrument_scope="...",  # required
    instrument_type="...",  # required
    instrument_event_type="...",  # required
    instrument_event_id="...",  # required
    generated_event=InstrumentEventHolder(...),  # optional
    generated_event_diagnostics=GeneratedEventDiagnostics(...),  # optional
    loaded_event=InstrumentEventHolder(...),  # optional
    applied_instrument_event_instruction_id="...",  # optional
    transactions=[],  # optional
    transaction_diagnostics=TransactionDiagnostics(...)  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [InstrumentEventHolder](InstrumentEventHolder.md)
- [GeneratedEventDiagnostics](GeneratedEventDiagnostics.md)
- [InstrumentEventHolder](InstrumentEventHolder.md)
- [Transaction](Transaction.md)
- [TransactionDiagnostics](TransactionDiagnostics.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

