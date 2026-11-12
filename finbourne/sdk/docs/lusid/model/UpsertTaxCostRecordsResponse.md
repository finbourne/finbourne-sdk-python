# UpsertTaxCostRecordsResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **successes** | [Dict[str, TaxCostRecord]](TaxCostRecord.md) | Optional | The Tax Cost Records that were successfully upserted, keyed by the code supplied in the request. |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | The Tax Cost Records that failed to upsert, keyed by the code supplied in the request, with the reason for each failure. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertTaxCostRecordsResponse import UpsertTaxCostRecordsResponse

instance = UpsertTaxCostRecordsResponse(
    successes=TaxCostRecord(...),  # optional — The Tax Cost Records that were successfully upserted, keyed by the code supplied in the request.
    failed=ErrorDetail(...),  # optional — The Tax Cost Records that failed to upsert, keyed by the code supplied in the request, with the reason for each failure.
    links=[]  # optional
)
```


## Related Models

- [TaxCostRecord](TaxCostRecord.md) — used in `successes`
- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

