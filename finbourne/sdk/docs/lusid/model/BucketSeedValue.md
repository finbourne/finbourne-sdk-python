# BucketSeedValue

One bucket's seeded cumulative value, as stored.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **bucket_id** | **str** | Required | The identifier of the seeded bucket. |
| **absolute_value** | **float** | Required | The bucket&#39;s seeded cumulative value at the valuation point, in the fund currency. |
| **per_unit_value** | **float** | Optional | The per-unit value given with the seed, unrounded. Omitted where none was given, in which case the valuation point reads it off the share class&#39;s units in issue. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BucketSeedValue import BucketSeedValue

instance = BucketSeedValue(
    bucket_id="...",  # required — The identifier of the seeded bucket.
    absolute_value=0.0,  # required — The bucket&#39;s seeded cumulative value at the valuation point, in the fund currency.
    per_unit_value=0.0  # optional — The per-unit value given with the seed, unrounded. Omitted where none was given, in which case the valuation point reads it off the share class&#39;s units in issue.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

