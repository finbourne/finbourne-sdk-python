# SuppressionEntryResponse

A single suppressions entry on a virtual transaction override record: the status of the suppression.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **status** | **str** | Optional | Whether this entry&#39;s target virtual transaction id still matches one the event currently generates. Available values: Applied, Orphaned, Superseded. |
| **virtual_transaction_id** | **str** | Optional | The id of the virtual transaction this entry targets, as it appears in the requested portfolio. Null when the entry targets no virtual transaction the requested portfolio currently generates. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.SuppressionEntryResponse import SuppressionEntryResponse

instance = SuppressionEntryResponse(
    status="...",  # optional — Whether this entry&#39;s target virtual transaction id still matches one the event currently generates. Available values: Applied, Orphaned, Superseded.
    virtual_transaction_id="..."  # optional — The id of the virtual transaction this entry targets, as it appears in the requested portfolio. Null when the entry targets no virtual transaction the requested portfolio currently generates.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

