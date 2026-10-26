# BucketSetSeedRequest

The closing balances to seed for a bucket set on an estimate valuation point.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **bucket_set_code** | **str** | Required | The code of the bucket set on the fund configuration to seed. |
| **class_seeds** | [List[BucketSetClassSeedRequest]](BucketSetClassSeedRequest.md) | Required | The bucket set&#39;s closing balances at the valuation point, per share class. They replace everything the bucket set holds up to and including the valuation point. A share class or bucket left out is zero. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BucketSetSeedRequest import BucketSetSeedRequest

instance = BucketSetSeedRequest(
    bucket_set_code="...",  # required — The code of the bucket set on the fund configuration to seed.
    class_seeds=[]  # required — The bucket set&#39;s closing balances at the valuation point, per share class. They replace everything the bucket set holds up to and including the valuation point. A share class or bucket left out is zero.
)
```

- [BucketSetClassSeedRequest](BucketSetClassSeedRequest.md) — used in `class_seeds`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

