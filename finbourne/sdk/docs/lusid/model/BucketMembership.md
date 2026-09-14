# BucketMembership

The bucket a Journal Entry Line was assigned to within one of a Fund Configuration's bucket sets.  Computed when the lines are read, from the bucket set definitions in force at that point.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **bucket_set_code** | **str** | Optional | The code of the bucket set that produced this classification. |
| **bucket_id** | **str** | Optional | The id of the bucket within that bucket set the line was assigned to, following the same first-match-wins waterfall used at valuation. One of the reserved &#39;_unmatched_dealing&#39;, &#39;_unmatched_fees&#39; or &#39;_unmatched_pnl&#39; ids when the line matched no bucket&#39;s filter in the set. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BucketMembership import BucketMembership

instance = BucketMembership(
    bucket_set_code="...",  # optional — The code of the bucket set that produced this classification.
    bucket_id="..."  # optional — The id of the bucket within that bucket set the line was assigned to, following the same first-match-wins waterfall used at valuation. One of the reserved &#39;_unmatched_dealing&#39;, &#39;_unmatched_fees&#39; or &#39;_unmatched_pnl&#39; ids when the line matched no bucket&#39;s filter in the set.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

