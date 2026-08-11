# CustodianAccount

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **custodian_account_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **status** | **str** | Required | The Account status. Available values: Active, Inactive, Deleted. |
| **account_number** | **str** | Required | The Custodian Account Number |
| **account_name** | **str** | Required | The identifiable name given to the Custodian Account |
| **accounting_method** | **str** | Required | The Accounting method to be used. Available values: Default, AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst, ProRateByUnits, ProRateByCost, ProRateByCostPortfolioCurrency, IntraDayThenFirstInFirstOut, LongTermHighestCostFirst, LongTermHighestCostFirstPortfolioCurrency, HighestCostFirstPortfolioCurrency, LowestCostFirstPortfolioCurrency, MaximumLossMinimumGain, MaximumLossMinimumGainPortfolioCurrency. |
| **currency** | **str** | Required | The Currency for the Account |
| **properties** | [Dict[str, ModelProperty]](ModelProperty.md) | Optional | Set of unique Custodian Account properties and associated values to store with the Custodian Account. Each property must be from the &#39;CustodianAccount&#39; domain. |
| **custodian** | [LegalEntity](LegalEntity.md) | Required | *No description available.* |
| **account_type** | **str** | Optional | The type of the Custodian Account. This is a free-text field that accepts any value. Optional, with no default. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CustodianAccount import CustodianAccount

instance = CustodianAccount(
    custodian_account_id=ResourceId(...),  # required
    status="...",  # required — The Account status. Available values: Active, Inactive, Deleted.
    account_number="...",  # required — The Custodian Account Number
    account_name="...",  # required — The identifiable name given to the Custodian Account
    accounting_method="...",  # required — The Accounting method to be used. Available values: Default, AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst, ProRateByUnits, ProRateByCost, ProRateByCostPortfolioCurrency, IntraDayThenFirstInFirstOut, LongTermHighestCostFirst, LongTermHighestCostFirstPortfolioCurrency, HighestCostFirstPortfolioCurrency, LowestCostFirstPortfolioCurrency, MaximumLossMinimumGain, MaximumLossMinimumGainPortfolioCurrency.
    currency="...",  # required — The Currency for the Account
    properties=ModelProperty(...),  # optional — Set of unique Custodian Account properties and associated values to store with the Custodian Account. Each property must be from the &#39;CustodianAccount&#39; domain.
    custodian=LegalEntity(...),  # required
    account_type="..."  # optional — The type of the Custodian Account. This is a free-text field that accepts any value. Optional, with no default.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ModelProperty](ModelProperty.md) — used in `properties`
- [LegalEntity](LegalEntity.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

