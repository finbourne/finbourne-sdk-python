# AdjustmentEntryResponse

A single adjustments entry on a virtual transaction override record: the fields it changes and its status.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **adjustment** | [AdjustmentDefinitionResponse](AdjustmentDefinitionResponse.md) | Optional | *No description available.* |
| **status** | **str** | Optional | Whether this entry&#39;s target virtual transaction id still matches one the event currently generates. Available values: Applied, Orphaned, Superseded. |
| **virtual_transaction_id** | **str** | Optional | The id of the virtual transaction this entry targets, as it appears in the requested portfolio. Null when the entry targets no virtual transaction the requested portfolio currently generates. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AdjustmentEntryResponse import AdjustmentEntryResponse

instance = AdjustmentEntryResponse(
    adjustment=AdjustmentDefinitionResponse(...),  # optional
    status="...",  # optional — Whether this entry&#39;s target virtual transaction id still matches one the event currently generates. Available values: Applied, Orphaned, Superseded.
    virtual_transaction_id="..."  # optional — The id of the virtual transaction this entry targets, as it appears in the requested portfolio. Null when the entry targets no virtual transaction the requested portfolio currently generates.
)
```


## Related Models

- [AdjustmentDefinitionResponse](AdjustmentDefinitionResponse.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

