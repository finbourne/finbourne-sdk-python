# MarginItem

One margin arrangement under an agreement, either variation or initial.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Required | The stable key that margin calls and custodian accounts refer to this item by. Unique across the agreement&#39;s variation and initial margin. |
| **trade_filter** | **str** | Optional | A filter selecting the trades this item covers. Required where the agreement has more than one margin item. |
| **settlement** | **str** | Optional | Whether margin is settled (Settled) or collateralised (Collateral). Optional. Available values: Collateral, Settled. |
| **legal_mechanism** | **str** | Optional | How title to posted collateral is held. One of TitleTransfer or SecurityInterest. Optional. Available values: TitleTransfer, SecurityInterest. |
| **we_post** | [PartyTerms](PartyTerms.md) | Required | *No description available.* |
| **they_post** | [PartyTerms](PartyTerms.md) | Required | *No description available.* |
| **eligible_collateral** | [EligibleCollateralReferences](EligibleCollateralReferences.md) | Optional | *No description available.* |
| **calculation** | [MarginCalculation](MarginCalculation.md) | Required | *No description available.* |
| **margin_accounts** | [MarginAccounts](MarginAccounts.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.MarginItem import MarginItem

instance = MarginItem(
    code="...",  # required — The stable key that margin calls and custodian accounts refer to this item by. Unique across the agreement&#39;s variation and initial margin.
    trade_filter="...",  # optional — A filter selecting the trades this item covers. Required where the agreement has more than one margin item.
    settlement="...",  # optional — Whether margin is settled (Settled) or collateralised (Collateral). Optional. Available values: Collateral, Settled.
    legal_mechanism="...",  # optional — How title to posted collateral is held. One of TitleTransfer or SecurityInterest. Optional. Available values: TitleTransfer, SecurityInterest.
    we_post=PartyTerms(...),  # required
    they_post=PartyTerms(...),  # required
    eligible_collateral=EligibleCollateralReferences(...),  # optional
    calculation=MarginCalculation(...),  # required
    margin_accounts=MarginAccounts(...)  # optional
)
```

- [PartyTerms](PartyTerms.md)
- [PartyTerms](PartyTerms.md)
- [EligibleCollateralReferences](EligibleCollateralReferences.md)
- [MarginCalculation](MarginCalculation.md)
- [MarginAccounts](MarginAccounts.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

