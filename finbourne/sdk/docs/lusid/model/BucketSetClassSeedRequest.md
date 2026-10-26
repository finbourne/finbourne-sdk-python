# BucketSetClassSeedRequest

One share class's bucket values to seed.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **share_class_short_code** | **str** | Required | The short code of the seeded share class. |
| **buckets** | [List[BucketSeedValueRequest]](BucketSeedValueRequest.md) | Required | The seeded buckets of the share class. Only the bucket set&#39;s flow buckets (dealing, P&amp;L and fees) accumulate, so only they can be seeded. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BucketSetClassSeedRequest import BucketSetClassSeedRequest

instance = BucketSetClassSeedRequest(
    share_class_short_code="...",  # required — The short code of the seeded share class.
    buckets=[]  # required — The seeded buckets of the share class. Only the bucket set&#39;s flow buckets (dealing, P&amp;L and fees) accumulate, so only they can be seeded.
)
```

- [BucketSeedValueRequest](BucketSeedValueRequest.md) — used in `buckets`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

