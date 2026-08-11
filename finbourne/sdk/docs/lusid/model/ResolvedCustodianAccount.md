# ResolvedCustodianAccount

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **account_selector** | **str** | Optional | Available values: From, To. |
| **custodian_account** | [CustodianAccount](CustodianAccount.md) | Required | *No description available.* |
| **resolution_type** | **str** | Required | Available values: BookingEntry, ContextCustodian, RelatedAccount, PortfolioDefault. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ResolvedCustodianAccount import ResolvedCustodianAccount

instance = ResolvedCustodianAccount(
    account_selector="...",  # optional — Available values: From, To.
    custodian_account=CustodianAccount(...),  # required
    resolution_type="..."  # required — Available values: BookingEntry, ContextCustodian, RelatedAccount, PortfolioDefault.
)
```

- [CustodianAccount](CustodianAccount.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

