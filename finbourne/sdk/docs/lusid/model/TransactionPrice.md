# TransactionPrice

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **price** | **float** | Optional | *No description available.* |
| **type** | **str** | Optional | The available values are: Price, Yield, Spread, CashFlowPerUnit, CleanPrice, DirtyPrice |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TransactionPrice import TransactionPrice

instance = TransactionPrice(
    price=0.0,  # optional
    type="..."  # optional — The available values are: Price, Yield, Spread, CashFlowPerUnit, CleanPrice, DirtyPrice
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

