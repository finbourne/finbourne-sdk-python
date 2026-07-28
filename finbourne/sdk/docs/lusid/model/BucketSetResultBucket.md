# BucketSetResultBucket

One bucket's values within a bucket set node: the movement in the period plus the cumulative values before  and after it (CumulativeValue = Value + PreviousCumulativeValue).
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **bucket_id** | **str** | Required | The identifier of the bucket. |
| **bucket_type** | **str** | Required | The type of the bucket (for example Dealing or PnL). |
| **value** | **float** | Required | The movement in the bucket over the valuation point&#39;s period. |
| **previous_cumulative_value** | **float** | Required | The cumulative value of the bucket up to the start of the period. |
| **cumulative_value** | **float** | Required | The cumulative value of the bucket up to the end of the period (Value + PreviousCumulativeValue). |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BucketSetResultBucket import BucketSetResultBucket

instance = BucketSetResultBucket(
    bucket_id="...",  # required — The identifier of the bucket.
    bucket_type="...",  # required — The type of the bucket (for example Dealing or PnL).
    value=0.0,  # required — The movement in the bucket over the valuation point&#39;s period.
    previous_cumulative_value=0.0,  # required — The cumulative value of the bucket up to the start of the period.
    cumulative_value=0.0  # required — The cumulative value of the bucket up to the end of the period (Value + PreviousCumulativeValue).
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

