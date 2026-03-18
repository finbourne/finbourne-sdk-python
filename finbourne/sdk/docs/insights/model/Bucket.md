# Bucket

A single histogram bucket.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **start_time** | **datetime** | Optional | The bucket&#39;s start time as a DateTimeOffset. |
| **item_count** | **int** | Optional | The number of items in the bucket. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.insights.models.Bucket import Bucket

instance = Bucket(
    start_time=datetime.now(),  # optional — The bucket&#39;s start time as a DateTimeOffset.
    item_count=0  # optional — The number of items in the bucket.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

