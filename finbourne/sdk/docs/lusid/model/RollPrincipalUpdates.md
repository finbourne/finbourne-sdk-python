# RollPrincipalUpdates

Describes changes to the principal on a FlexibleDeposit instrument as the result of a DepositRollEvent.  Either the principal to be withdrawn or the principal increase must be specified (either as an amount or a percentage).
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **withdraw_principal_amount** | **float** | Optional | The amount of principal that should be withdrawn from the FlexibleDeposit. |
| **withdraw_principal_percentage** | **float** | Optional | The percentage of principal that should be withdrawn from the FlexibleDeposit. |
| **increase_principal_amount** | **float** | Optional | The amount of principal that should be added to the FlexibleDeposit. |
| **increase_principal_percentage** | **float** | Optional | The percentage of principal that should be added to the FlexibleDeposit. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RollPrincipalUpdates import RollPrincipalUpdates

instance = RollPrincipalUpdates(
    withdraw_principal_amount=0.0,  # optional — The amount of principal that should be withdrawn from the FlexibleDeposit.
    withdraw_principal_percentage=0.0,  # optional — The percentage of principal that should be withdrawn from the FlexibleDeposit.
    increase_principal_amount=0.0,  # optional — The amount of principal that should be added to the FlexibleDeposit.
    increase_principal_percentage=0.0  # optional — The percentage of principal that should be added to the FlexibleDeposit.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

