# TransactionTypeCalculation

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **type** | **str** | Required | The type of calculation to perform |
| **side** | **str** | Optional | The side to which the calculation is applied |
| **formula** | **str** | Optional | The formula used to derive the total consideration amount when it is not provided on the transaction |
| **transaction_fee_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **transaction_fee_capitalisation** | [TransactionFeeCapitalisation](TransactionFeeCapitalisation.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransactionTypeCalculation import TransactionTypeCalculation

instance = TransactionTypeCalculation(
    type="...",  # required — The type of calculation to perform
    side="...",  # optional — The side to which the calculation is applied
    formula="...",  # optional — The formula used to derive the total consideration amount when it is not provided on the transaction
    transaction_fee_id=ResourceId(...),  # optional
    transaction_fee_capitalisation=TransactionFeeCapitalisation(...)  # optional
)
```

- [ResourceId](ResourceId.md)
- [TransactionFeeCapitalisation](TransactionFeeCapitalisation.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

