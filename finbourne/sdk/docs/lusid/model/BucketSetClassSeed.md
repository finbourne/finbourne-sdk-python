# BucketSetClassSeed

One share class's seeded bucket values.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **share_class_short_code** | **str** | Required | The short code of the seeded share class. |
| **buckets** | [List[BucketSeedValue]](BucketSeedValue.md) | Required | The seeded buckets of the share class. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BucketSetClassSeed import BucketSetClassSeed

instance = BucketSetClassSeed(
    share_class_short_code="...",  # required — The short code of the seeded share class.
    buckets=[]  # required — The seeded buckets of the share class.
)
```

- [BucketSeedValue](BucketSeedValue.md) — used in `buckets`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

