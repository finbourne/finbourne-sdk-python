# RollInterestUpdates

Describes changes to the interest of a FlexibleDeposit instrument as the result of a DepositRollEvent.  Both the interest to be withdrawn and the interest to be reinvested must be specified (either as an amount or as a percentage).
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **withdraw_interest_amount** | **float** | Optional | The amount of interest that should be withdrawn from a FlexibleDeposit as the result of a roll event. |
| **withdraw_interest_percentage** | **float** | Optional | The percentage of interest that should be withdrawn from a FlexibleDeposit instrument as the result of a roll event. |
| **reinvest_interest_amount** | **float** | Optional | The amount of interest that should be reinvested in a FlexibleDeposit instrument as the result of a roll event. |
| **reinvest_interest_percentage** | **float** | Optional | The percentage of interest that should be reinvested in a FlexibleDeposit instrument as the result of a roll event. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RollInterestUpdates import RollInterestUpdates

instance = RollInterestUpdates(
    withdraw_interest_amount=0.0,  # optional — The amount of interest that should be withdrawn from a FlexibleDeposit as the result of a roll event.
    withdraw_interest_percentage=0.0,  # optional — The percentage of interest that should be withdrawn from a FlexibleDeposit instrument as the result of a roll event.
    reinvest_interest_amount=0.0,  # optional — The amount of interest that should be reinvested in a FlexibleDeposit instrument as the result of a roll event.
    reinvest_interest_percentage=0.0  # optional — The percentage of interest that should be reinvested in a FlexibleDeposit instrument as the result of a roll event.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

