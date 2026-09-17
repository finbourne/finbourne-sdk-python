# VirtualTransactionOverrideRecord

The overrides and suppressions stored against a single instrument event in a single portfolio, together  with their statuses as resolved against the requested portfolio's currently generated virtual  transactions.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **instrument_event_id** | **str** | Optional | The identifier of the instrument event this record is stored against. |
| **source_portfolio_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **overrides** | [Dict[str, OverrideEntryResponse]](OverrideEntryResponse.md) | Optional | The overrides stored in this record, keyed by the virtual transaction id being overridden as it appears in the portfolio holding the record. |
| **suppressions** | [Dict[str, SuppressionEntryResponse]](SuppressionEntryResponse.md) | Optional | The suppressions stored in this record, keyed by the virtual transaction id being suppressed as it appears in the portfolio holding the record. |
| **override_match_status** | **str** | Optional | Whether every override and suppression entry in this record still matches a virtual transaction the event currently generates. Available values: Matched, Orphaned. |
| **override_application_status** | **str** | Optional | Whether all, some, or none of this record&#39;s override and suppression entries are currently applied. Available values: Full, Partial, Orphaned. |
| **cancel_active** | **bool** | Optional | True when an active event-level Cancel instruction also exists for this instrument event, taking precedence over the entries in this record. |
| **version** | [Version](Version.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.VirtualTransactionOverrideRecord import VirtualTransactionOverrideRecord

instance = VirtualTransactionOverrideRecord(
    instrument_event_id="...",  # optional — The identifier of the instrument event this record is stored against.
    source_portfolio_id=ResourceId(...),  # optional
    overrides=OverrideEntryResponse(...),  # optional — The overrides stored in this record, keyed by the virtual transaction id being overridden as it appears in the portfolio holding the record.
    suppressions=SuppressionEntryResponse(...),  # optional — The suppressions stored in this record, keyed by the virtual transaction id being suppressed as it appears in the portfolio holding the record.
    override_match_status="...",  # optional — Whether every override and suppression entry in this record still matches a virtual transaction the event currently generates. Available values: Matched, Orphaned.
    override_application_status="...",  # optional — Whether all, some, or none of this record&#39;s override and suppression entries are currently applied. Available values: Full, Partial, Orphaned.
    cancel_active=True,  # optional — True when an active event-level Cancel instruction also exists for this instrument event, taking precedence over the entries in this record.
    version=Version(...)  # optional
)
```

- [ResourceId](ResourceId.md)
- [OverrideEntryResponse](OverrideEntryResponse.md) — used in `overrides`
- [SuppressionEntryResponse](SuppressionEntryResponse.md) — used in `suppressions`
- [Version](Version.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

