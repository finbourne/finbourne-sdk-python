# BatchUpdateUserReviewForComparisonResultResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **values** | [Dict[str, GroupReconciliationComparisonResult]](GroupReconciliationComparisonResult.md) | Optional | The collection of comparison results that have been successfully updated. |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | The collection of comparison results that could not be updated with the provided user input along with a reason for their failure. |
| **metadata** | **Dict[str, Optional[List[ResponseMetaData]]]** | Optional | Contains warnings related to the updated comparison result user input |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BatchUpdateUserReviewForComparisonResultResponse import BatchUpdateUserReviewForComparisonResultResponse

instance = BatchUpdateUserReviewForComparisonResultResponse(
    values=GroupReconciliationComparisonResult(...),  # optional — The collection of comparison results that have been successfully updated.
    failed=ErrorDetail(...),  # optional — The collection of comparison results that could not be updated with the provided user input along with a reason for their failure.
    metadata=,  # optional — Contains warnings related to the updated comparison result user input
    links=[]  # optional
)
```


## Related Models

- [GroupReconciliationComparisonResult](GroupReconciliationComparisonResult.md) — used in `values`
- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

