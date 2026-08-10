# PaymentInstructionRequest

A request to create or update a Payment Instruction. Status is not accepted here —  status transitions are managed exclusively via the dedicated Payment Instruction status API.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [../model/ResourceId](ResourceId.md) | Required | *No description available.* |
| **payment_record_ids** | [../model/List[PaymentRecordReference]](PaymentRecordReference.md) | Required | One or more Payment Records batched into this instruction block. All referenced Payment Records must share the same currency as the top-level currency field. |
| **currency** | **str** | Required | ISO 4217 currency code. All referenced Payment Records must share this currency value. |
| **total_payment_amount** | **float** | Required | Total payment amount across all referenced Payment Records. |
| **payment_date** | **datetime** | Required | The value date on which settlement is due. ISO 8601 date. |
| **payor_payment_details_reference** | [../model/PaymentDetailsReference](PaymentDetailsReference.md) | Required | *No description available.* |
| **payee_payment_details_reference** | [../model/PaymentDetailsReference](PaymentDetailsReference.md) | Required | *No description available.* |
| **properties** | [../model/Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | Client-defined properties associated with this Payment Instruction. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PaymentInstructionRequest import PaymentInstructionRequest

instance = PaymentInstructionRequest(
    id=ResourceId(...),  # required
    payment_record_ids=[],  # required — One or more Payment Records batched into this instruction block. All referenced Payment Records must share the same currency as the top-level currency field.
    currency="...",  # required — ISO 4217 currency code. All referenced Payment Records must share this currency value.
    total_payment_amount=0.0,  # required — Total payment amount across all referenced Payment Records.
    payment_date=datetime.now(),  # required — The value date on which settlement is due. ISO 8601 date.
    payor_payment_details_reference=PaymentDetailsReference(...),  # required
    payee_payment_details_reference=PaymentDetailsReference(...),  # required
    properties=PerpetualProperty(...)  # optional — Client-defined properties associated with this Payment Instruction.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [PaymentRecordReference](PaymentRecordReference.md) — used in `payment_record_ids`
- [PaymentDetailsReference](PaymentDetailsReference.md)
- [PaymentDetailsReference](PaymentDetailsReference.md)
- [PerpetualProperty](PerpetualProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

