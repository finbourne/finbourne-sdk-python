# BatchReviewRecResultItemResult

The successful outcome of a single batch review item: every rec result affected by the item (which  may exceed the results named in the request, e.g. group members re-opened by a nullify).
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **rec_results** | [List[RecResult]](RecResult.md) | Required | The full set of rec results affected by the batch item (may exceed the results named in the request). |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BatchReviewRecResultItemResult import BatchReviewRecResultItemResult

instance = BatchReviewRecResultItemResult(
    rec_results=[]  # required — The full set of rec results affected by the batch item (may exceed the results named in the request).
)
```


## Related Models

- [RecResult](RecResult.md) — used in `rec_results`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

