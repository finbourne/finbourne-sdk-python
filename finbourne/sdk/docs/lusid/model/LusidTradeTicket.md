# LusidTradeTicket

A LUSID Trade Ticket comprising an instrument, a transaction, and a counterparty.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **transaction_id** | **str** | Required | Transaction ID. Must be unique. |
| **transaction_type** | **str** | Required | Type of transaction for processing. Referenced by Transaction Configuration. |
| **source** | **str** | Optional | Transaction Source. Referenced by Transaction Configuration. |
| **transaction_date** | **str** | Required | Transaction Date. Date at which transaction is known. |
| **settlement_date** | **str** | Required | Transaction settlement. Date at which transaction is finalised and realised into the system. |
| **total_consideration** | [CurrencyAndAmount](CurrencyAndAmount.md) | Required | *No description available.* |
| **units** | **float** | Required | Number of units in the transaction. For an OTC this is somewhat interchangeable with the quantity booked in the  instrument. As M x N or N x M are equivalent it is advised a client chooses one approach and sticks to it.  Arguably either the unit or holding is best unitised. |
| **instrument_identifiers** | **Dict[str, Optional[str]]** | Required | Identifiers for the instrument. |
| **instrument_scope** | **str** | Optional | Scope of instrument |
| **instrument_name** | **str** | Optional | Name of instrument |
| **instrument_definition** | [LusidInstrument](LusidInstrument.md) | Optional | *No description available.* |
| **counterparty_agreement_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **counterparty** | **str** | Optional | Counterparty |
| **instrument_properties** | [List[ModelProperty]](ModelProperty.md) | Optional | Set of instrument properties (as defined by client/user). |
| **transaction_properties** | [List[ModelProperty]](ModelProperty.md) | Optional | Set of transaction properties (as defined by client/user). |
| **trade_ticket_type** | **str** | Required | The available values are: LusidTradeTicket, ExternalTradeTicket |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.LusidTradeTicket import LusidTradeTicket

instance = LusidTradeTicket(
    transaction_id="...",  # required — Transaction ID. Must be unique.
    transaction_type="...",  # required — Type of transaction for processing. Referenced by Transaction Configuration.
    source="...",  # optional — Transaction Source. Referenced by Transaction Configuration.
    transaction_date="...",  # required — Transaction Date. Date at which transaction is known.
    settlement_date="...",  # required — Transaction settlement. Date at which transaction is finalised and realised into the system.
    total_consideration=CurrencyAndAmount(...),  # required
    units=0.0,  # required — Number of units in the transaction. For an OTC this is somewhat interchangeable with the quantity booked in the  instrument. As M x N or N x M are equivalent it is advised a client chooses one approach and sticks to it.  Arguably either the unit or holding is best unitised.
    instrument_identifiers=,  # required — Identifiers for the instrument.
    instrument_scope="...",  # optional — Scope of instrument
    instrument_name="...",  # optional — Name of instrument
    instrument_definition=LusidInstrument(...),  # optional
    counterparty_agreement_id=ResourceId(...),  # optional
    counterparty="...",  # optional — Counterparty
    instrument_properties=[],  # optional — Set of instrument properties (as defined by client/user).
    transaction_properties=[],  # optional — Set of transaction properties (as defined by client/user).
    trade_ticket_type="..."  # required — The available values are: LusidTradeTicket, ExternalTradeTicket
)
```

- [CurrencyAndAmount](CurrencyAndAmount.md)
- [LusidInstrument](LusidInstrument.md)
- [ResourceId](ResourceId.md)
- [ModelProperty](ModelProperty.md) — used in `instrument_properties`
- [ModelProperty](ModelProperty.md) — used in `transaction_properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

