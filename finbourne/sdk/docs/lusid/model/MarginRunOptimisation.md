# MarginRunOptimisation

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **status** | **str** | Required | How far the pass got. One of Pending, Completed, Skipped or Failed. |
| **recommendation_count** | **int** | Required | How many recommendations the pass made. |
| **detail** | **str** | Optional | What the pass left out and why, or why it failed. Null when nothing was left out. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.MarginRunOptimisation import MarginRunOptimisation

instance = MarginRunOptimisation(
    status="...",  # required — How far the pass got. One of Pending, Completed, Skipped or Failed.
    recommendation_count=0,  # required — How many recommendations the pass made.
    detail="..."  # optional — What the pass left out and why, or why it failed. Null when nothing was left out.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

