# BucketSeedValueRequest

One bucket's cumulative value to seed.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **bucket_id** | **str** | Required | The identifier of the seeded bucket. |
| **absolute_value** | **float** | Required | The bucket&#39;s cumulative value at the valuation point, in the fund currency. It is trusted input: nothing reconciles it to the share class NAV. |
| **per_unit_value** | **float** | Optional | The bucket&#39;s cumulative value per unit in issue. It is stored rounded to the share class&#39;s price precision. When omitted on a unitised bucket it is the absolute value over the share class&#39;s units in issue at the valuation point. Must be omitted on a bucket that is not unitised. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BucketSeedValueRequest import BucketSeedValueRequest

instance = BucketSeedValueRequest(
    bucket_id="...",  # required — The identifier of the seeded bucket.
    absolute_value=0.0,  # required — The bucket&#39;s cumulative value at the valuation point, in the fund currency. It is trusted input: nothing reconciles it to the share class NAV.
    per_unit_value=0.0  # optional — The bucket&#39;s cumulative value per unit in issue. It is stored rounded to the share class&#39;s price precision. When omitted on a unitised bucket it is the absolute value over the share class&#39;s units in issue at the valuation point. Must be omitted on a bucket that is not unitised.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

