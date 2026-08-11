# Histogram

A histogram showing an item's count in buckets of equal timespans.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **buckets** | [List[Bucket]](Bucket.md) | Optional | An ordered list of the histogram buckets. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.insights.models.Histogram import Histogram

instance = Histogram(
    buckets=[]  # optional — An ordered list of the histogram buckets.
)
```


## Related Models

- [Bucket](Bucket.md) — used in `buckets`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

