# UpsertVirtualTransactionOverrideResponse

The result of upserting overrides and suppressions of virtual transactions for a single instrument event.  Returns the record as it was persisted and the new version of the record. Whether each entry currently  applies, and which virtual transactions the event still generates unmodified.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **version** | [Version](Version.md) | Required | *No description available.* |
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **metadata** | **Dict[str, Optional[List[ResponseMetaData]]]** | Optional | Contains warnings related to unresolved instruments, non-existent transaction types, sub-holding key mismatches, or closed accounting periods for the override transactions. |
| **instrument_event_id** | **str** | Required | The identifier of the instrument event that was overridden. |
| **overrides** | **Dict[str, Optional[List[StoredOverrideDefinition]]]** | Optional | The replacement transactions persisted for the instrument event, keyed by the virtual transaction id being overridden. |
| **suppressions** | **List[str]** | Optional | The virtual transaction ids suppressed for the instrument event. |
| **cancel_active** | **bool** | Optional | True when an active event-level Cancel instruction also exists for this instrument event, taking precedence over the entries in this record. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertVirtualTransactionOverrideResponse import UpsertVirtualTransactionOverrideResponse

instance = UpsertVirtualTransactionOverrideResponse(
    version=Version(...),  # required
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    metadata=,  # optional — Contains warnings related to unresolved instruments, non-existent transaction types, sub-holding key mismatches, or closed accounting periods for the override transactions.
    instrument_event_id="...",  # required — The identifier of the instrument event that was overridden.
    overrides=,  # optional — The replacement transactions persisted for the instrument event, keyed by the virtual transaction id being overridden.
    suppressions=,  # optional — The virtual transaction ids suppressed for the instrument event.
    cancel_active=True,  # optional — True when an active event-level Cancel instruction also exists for this instrument event, taking precedence over the entries in this record.
    links=[]  # optional
)
```


## Related Models

- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

