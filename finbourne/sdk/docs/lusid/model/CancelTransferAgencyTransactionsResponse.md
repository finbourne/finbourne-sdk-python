# CancelTransferAgencyTransactionsResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **successes** | [Dict[str, TransferAgencyTransactionCancellationResult]](TransferAgencyTransactionCancellationResult.md) | Optional | A dictionary of successfully un-priced orders, keyed by the request key. |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | A dictionary of failed un-pricing attempts, keyed by the request key, containing error details. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CancelTransferAgencyTransactionsResponse import CancelTransferAgencyTransactionsResponse

instance = CancelTransferAgencyTransactionsResponse(
    successes=TransferAgencyTransactionCancellationResult(...),  # optional — A dictionary of successfully un-priced orders, keyed by the request key.
    failed=ErrorDetail(...),  # optional — A dictionary of failed un-pricing attempts, keyed by the request key, containing error details.
    links=[]  # optional
)
```


## Related Models

- [TransferAgencyTransactionCancellationResult](TransferAgencyTransactionCancellationResult.md) — used in `successes`
- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

