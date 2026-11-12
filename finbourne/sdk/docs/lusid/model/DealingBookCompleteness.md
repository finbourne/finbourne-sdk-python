# DealingBookCompleteness

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **complete** | **bool** | Required | Whether every share class&#39;s dealing cut-off had passed at the strike&#39;s as-at. True when no cut-off is configured. |
| **cut_off** | **datetime** | Optional | The latest dealing cut-off among the share classes that configure one. Absent when none does. |
| **late_not_counted** | **int** | Optional | How many orders at the valuation point were written to the book after their class&#39;s cut-off and so were reported but not counted. Absent when a cut-off is configured but lateness could not be judged because an order at the valuation point carries no version. |
| **note** | **str** | Optional | Why the book was judged complete or incomplete: the cut-off that had or had not passed, or that none is configured and completeness was assumed. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.DealingBookCompleteness import DealingBookCompleteness

instance = DealingBookCompleteness(
    complete=True,  # required — Whether every share class&#39;s dealing cut-off had passed at the strike&#39;s as-at. True when no cut-off is configured.
    cut_off=datetime.now(),  # optional — The latest dealing cut-off among the share classes that configure one. Absent when none does.
    late_not_counted=0,  # optional — How many orders at the valuation point were written to the book after their class&#39;s cut-off and so were reported but not counted. Absent when a cut-off is configured but lateness could not be judged because an order at the valuation point carries no version.
    note="..."  # optional — Why the book was judged complete or incomplete: the cut-off that had or had not passed, or that none is configured and completeness was assumed.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

