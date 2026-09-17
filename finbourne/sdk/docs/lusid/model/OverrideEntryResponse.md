# OverrideEntryResponse

A single overrides entry on a virtual transaction override record: the replacement transaction(s) that  stand in for the overridden virtual transaction, plus its status and diagnostics.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **replacements** | [List[OverrideDefinitionResponse]](OverrideDefinitionResponse.md) | Optional | The replacement transactions that stand in for the overridden virtual transaction. |
| **status** | **str** | Optional | Whether this entry&#39;s target virtual transaction id still matches one the event currently generates. Available values: Applied, Orphaned, Superseded. |
| **virtual_transaction_id** | **str** | Optional | The id of the virtual transaction this entry targets, as it appears in the requested portfolio. Null when the entry targets no virtual transaction the requested portfolio currently generates. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.OverrideEntryResponse import OverrideEntryResponse

instance = OverrideEntryResponse(
    replacements=[],  # optional — The replacement transactions that stand in for the overridden virtual transaction.
    status="...",  # optional — Whether this entry&#39;s target virtual transaction id still matches one the event currently generates. Available values: Applied, Orphaned, Superseded.
    virtual_transaction_id="..."  # optional — The id of the virtual transaction this entry targets, as it appears in the requested portfolio. Null when the entry targets no virtual transaction the requested portfolio currently generates.
)
```


## Related Models

- [OverrideDefinitionResponse](OverrideDefinitionResponse.md) — used in `replacements`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

