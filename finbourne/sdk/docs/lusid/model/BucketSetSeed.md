# BucketSetSeed

The closing balances seeded for a bucket set on a valuation point.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **bucket_set_code** | **str** | Required | The code of the seeded bucket set on the fund configuration. |
| **class_seeds** | [List[BucketSetClassSeed]](BucketSetClassSeed.md) | Required | The bucket set&#39;s seeded closing balances at the valuation point, per share class. They replace everything the bucket set holds up to and including the valuation point. A share class or bucket not listed is zero. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BucketSetSeed import BucketSetSeed

instance = BucketSetSeed(
    bucket_set_code="...",  # required — The code of the seeded bucket set on the fund configuration.
    class_seeds=[]  # required — The bucket set&#39;s seeded closing balances at the valuation point, per share class. They replace everything the bucket set holds up to and including the valuation point. A share class or bucket not listed is zero.
)
```

- [BucketSetClassSeed](BucketSetClassSeed.md) — used in `class_seeds`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

