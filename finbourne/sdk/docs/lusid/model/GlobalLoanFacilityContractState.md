# GlobalLoanFacilityContractState

The desired global state of a single FlexibleLoan contract. Balances are global - across all investors -  rather than investor specific.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **contract_details** | [ContractDetails](ContractDetails.md) | Required | *No description available.* |
| **balance** | **float** | Required | The desired global balance for this contract, in the contract&#39;s own currency. Must be non-negative. |
| **balance_in_facility_ccy** | **float** | Optional | The desired global balance expressed in the facility currency. Required when the contract currency  differs from the facility currency, and defaults to Balance otherwise. |
| **agency_fx_rate** | **float** | Optional | The agency FX rate converting contract currency to facility currency. Required when the contract  currency differs from the facility currency. When omitted it is derived from the two balances where  possible, and otherwise defaults to 1. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.GlobalLoanFacilityContractState import GlobalLoanFacilityContractState

instance = GlobalLoanFacilityContractState(
    contract_details=ContractDetails(...),  # required
    balance=0.0,  # required — The desired global balance for this contract, in the contract&#39;s own currency. Must be non-negative.
    balance_in_facility_ccy=0.0,  # optional — The desired global balance expressed in the facility currency. Required when the contract currency  differs from the facility currency, and defaults to Balance otherwise.
    agency_fx_rate=0.0  # optional — The agency FX rate converting contract currency to facility currency. Required when the contract  currency differs from the facility currency. When omitted it is derived from the two balances where  possible, and otherwise defaults to 1.
)
```


## Related Models

- [ContractDetails](ContractDetails.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

