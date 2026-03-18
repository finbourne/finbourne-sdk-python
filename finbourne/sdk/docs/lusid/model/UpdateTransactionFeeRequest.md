# UpdateTransactionFeeRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **description** | **str** | Optional | A description of the transaction fee. |
| **calculation** | [FeeCalculationRequest](FeeCalculationRequest.md) | Optional | *No description available.* |
| **condition** | **str** | Optional | The condition that the transaction must meet in order for the fee to be applied. |
| **capitalisation_condition** | **str** | Optional | If the fee Capitalisation is Conditional, this condition determines whether the fee is capitalised, when applied to the transaction. |
| **txn_property_key** | **str** | Optional | The property key to which the fee value will be applied and decorated onto the transaction. Must be in the &#39;Transaction&#39; property domain. |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | A set of properties for the transaction fee. |
| **is_active** | **bool** | Optional | Indicates whether the transaction fee is currently active and should be applied to transactions. Optional when creating a transaction fee, defaults to true, if a value is not provided. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpdateTransactionFeeRequest import UpdateTransactionFeeRequest

instance = UpdateTransactionFeeRequest(
    description="...",  # optional — A description of the transaction fee.
    calculation=FeeCalculationRequest(...),  # optional
    condition="...",  # optional — The condition that the transaction must meet in order for the fee to be applied.
    capitalisation_condition="...",  # optional — If the fee Capitalisation is Conditional, this condition determines whether the fee is capitalised, when applied to the transaction.
    txn_property_key="...",  # optional — The property key to which the fee value will be applied and decorated onto the transaction. Must be in the &#39;Transaction&#39; property domain.
    properties=ModelProperty(...),  # optional — A set of properties for the transaction fee.
    is_active=True  # optional — Indicates whether the transaction fee is currently active and should be applied to transactions. Optional when creating a transaction fee, defaults to true, if a value is not provided.
)
```

- [FeeCalculationRequest](FeeCalculationRequest.md)
- [ModelProperty](ModelProperty.md) — used in `properties`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

