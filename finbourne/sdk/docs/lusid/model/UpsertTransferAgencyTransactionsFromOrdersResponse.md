# UpsertTransferAgencyTransactionsFromOrdersResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **successes** | [Dict[str, TransferAgencyTransactionFromOrderResult]](TransferAgencyTransactionFromOrderResult.md) | Optional | A dictionary of successfully priced orders, keyed by the request key. |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | A dictionary of failed order pricing attempts, keyed by the request key, containing error details. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertTransferAgencyTransactionsFromOrdersResponse import UpsertTransferAgencyTransactionsFromOrdersResponse

instance = UpsertTransferAgencyTransactionsFromOrdersResponse(
    successes=TransferAgencyTransactionFromOrderResult(...),  # optional — A dictionary of successfully priced orders, keyed by the request key.
    failed=ErrorDetail(...),  # optional — A dictionary of failed order pricing attempts, keyed by the request key, containing error details.
    links=[]  # optional
)
```


## Related Models

- [TransferAgencyTransactionFromOrderResult](TransferAgencyTransactionFromOrderResult.md) — used in `successes`
- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

