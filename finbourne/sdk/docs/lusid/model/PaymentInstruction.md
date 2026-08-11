# PaymentInstruction

A Payment Instruction groups one or more Payment Records into a single block  for transmission to a downstream treasury management system via the Horizon integration.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **payment_record_ids** | [List[PaymentRecordReference]](PaymentRecordReference.md) | Required | One or more Payment Records batched into this instruction block. All referenced Payment Records must share the same currency as the top-level currency field. |
| **currency** | **str** | Required | ISO 4217 currency code. All referenced Payment Records must share this currency value. |
| **total_payment_amount** | **float** | Required | Total payment amount across all referenced Payment Records. |
| **payment_date** | **datetime** | Required | The value date on which settlement is due. ISO 8601 date. |
| **payor_payment_details_reference** | [PaymentDetailsReferenceResponse](PaymentDetailsReferenceResponse.md) | Required | *No description available.* |
| **payee_payment_details_reference** | [PaymentDetailsReferenceResponse](PaymentDetailsReferenceResponse.md) | Required | *No description available.* |
| **properties** | [Dict[str, PerpetualProperty]](PerpetualProperty.md) | Optional | Client-defined properties associated with this Payment Instruction. |
| **status** | [PaymentInstructionStatus](PaymentInstructionStatus.md) | Required | *No description available.* |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PaymentInstruction import PaymentInstruction

instance = PaymentInstruction(
    id=ResourceId(...),  # required
    payment_record_ids=[],  # required — One or more Payment Records batched into this instruction block. All referenced Payment Records must share the same currency as the top-level currency field.
    currency="...",  # required — ISO 4217 currency code. All referenced Payment Records must share this currency value.
    total_payment_amount=0.0,  # required — Total payment amount across all referenced Payment Records.
    payment_date=datetime.now(),  # required — The value date on which settlement is due. ISO 8601 date.
    payor_payment_details_reference=PaymentDetailsReferenceResponse(...),  # required
    payee_payment_details_reference=PaymentDetailsReferenceResponse(...),  # required
    properties=PerpetualProperty(...),  # optional — Client-defined properties associated with this Payment Instruction.
    status=PaymentInstructionStatus(...),  # required
    version=Version(...),  # optional
    links=[]  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [PaymentRecordReference](PaymentRecordReference.md) — used in `payment_record_ids`
- [PaymentDetailsReferenceResponse](PaymentDetailsReferenceResponse.md)
- [PaymentDetailsReferenceResponse](PaymentDetailsReferenceResponse.md)
- [PerpetualProperty](PerpetualProperty.md) — used in `properties`
- [PaymentInstructionStatus](PaymentInstructionStatus.md)
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

