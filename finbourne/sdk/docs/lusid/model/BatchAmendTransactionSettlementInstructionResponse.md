# BatchAmendTransactionSettlementInstructionResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **href** | **str** | Optional | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. |
| **values** | [Dict[str, TransactionSettlementInstruction]](TransactionSettlementInstruction.md) | Optional | The settlement instructions which have been successfully upserted. |
| **failed** | [Dict[str, ErrorDetail]](ErrorDetail.md) | Optional | The request ids of the settlement instructions which could not be upserted, along with a reason for their failure. |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.BatchAmendTransactionSettlementInstructionResponse import BatchAmendTransactionSettlementInstructionResponse

instance = BatchAmendTransactionSettlementInstructionResponse(
    href="...",  # optional — The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
    values=TransactionSettlementInstruction(...),  # optional — The settlement instructions which have been successfully upserted.
    failed=ErrorDetail(...),  # optional — The request ids of the settlement instructions which could not be upserted, along with a reason for their failure.
    links=[]  # optional
)
```

- [TransactionSettlementInstruction](TransactionSettlementInstruction.md) — used in `values`
- [ErrorDetail](ErrorDetail.md) — used in `failed`
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

