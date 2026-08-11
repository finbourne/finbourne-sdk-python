# BucketSetResult

A valuation point's results for one bucket set: whether the set is the apportionment set, and its per-node  (fund and share class) buckets and NAV. Allocation-group nodes are not included here - they are surfaced via  the apportionment results.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **is_apportionment** | **bool** | Required | Whether this bucket set is the apportionment set (apportioning non-class-specific P&amp;L across share classes). |
| **nodes** | [List[BucketSetNode]](BucketSetNode.md) | Required | The nodes making up the bucket set: the fund aggregate and one per share class. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BucketSetResult import BucketSetResult

instance = BucketSetResult(
    is_apportionment=True,  # required — Whether this bucket set is the apportionment set (apportioning non-class-specific P&amp;L across share classes).
    nodes=[]  # required — The nodes making up the bucket set: the fund aggregate and one per share class.
)
```

- [BucketSetNode](BucketSetNode.md) — used in `nodes`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

