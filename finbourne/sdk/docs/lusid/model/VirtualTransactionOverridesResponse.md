# VirtualTransactionOverridesResponse

The overrides and suppressions affecting a single instrument event in the requested portfolio. A derived  portfolio is affected by its own record and by every record held by an ancestor, so one record per  holding portfolio is returned, nearest first.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **version** | [Version](Version.md) | Required | *No description available.* |
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **instrument_event_id** | **str** | Required | The identifier of the instrument event whose overrides and suppressions are returned. |
| **records** | [List[VirtualTransactionOverrideRecord]](VirtualTransactionOverrideRecord.md) | Optional | The override and suppression records affecting the requested portfolio for this instrument event, nearest first. A derived portfolio is affected by its own record and by every record held by an ancestor. |
| **live** | **List[str]** | Optional | The virtual transaction ids the event currently generates in the requested portfolio that no returned record targets, and so keep generating unmodified. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.VirtualTransactionOverridesResponse import VirtualTransactionOverridesResponse

instance = VirtualTransactionOverridesResponse(
    version=Version(...),  # required
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    instrument_event_id="...",  # required — The identifier of the instrument event whose overrides and suppressions are returned.
    records=[],  # optional — The override and suppression records affecting the requested portfolio for this instrument event, nearest first. A derived portfolio is affected by its own record and by every record held by an ancestor.
    live=,  # optional — The virtual transaction ids the event currently generates in the requested portfolio that no returned record targets, and so keep generating unmodified.
    links=[]  # optional
)
```


## Related Models

- [Version](Version.md)
- [VirtualTransactionOverrideRecord](VirtualTransactionOverrideRecord.md) — used in `records`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

