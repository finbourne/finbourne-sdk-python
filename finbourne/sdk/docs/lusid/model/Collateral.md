# Collateral

Representation of the collateral of a repurchase agreement, along with related details of the agreement.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **buyer_receives_cashflows** | **bool** | Required | Does the buyer of the FlexibleRepo receive the cashflows from any collateral instruments, or do they get paid to the seller. |
| **buyer_receives_corporate_action_payments** | **bool** | Required | Does the buyer of the FlexibleRepo receive any dividend or cash payments as the result of a corporate action  on any of the collateral instruments, or are these amounts paid to the seller.  Referred to as \&quot;manufactured payments\&quot; in the UK, and valid only under a repo with GMRA in Europe |
| **collateral_instruments** | [List[CollateralInstrument]](CollateralInstrument.md) | Optional | List of any collateral instruments. |
| **collateral_value** | **float** | Optional | Total value of the collateral before any margin or haircut applied.  Can be provided instead of PurchasePrice, so that PurchasePrice can be inferred from the CollateralValue and one of  Haircut or Margin. |
| **defer_manufactured_payments** | **bool** | Optional | Indicates whether manufactured collateral payments are capitalised (i.e. deferred). Capitalised payments will  be deferred to the maturity date of the repo and if applicable interest will be accrued at the repo rate.  Defaults to false. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.Collateral import Collateral

instance = Collateral(
    buyer_receives_cashflows=True,  # required — Does the buyer of the FlexibleRepo receive the cashflows from any collateral instruments, or do they get paid to the seller.
    buyer_receives_corporate_action_payments=True,  # required — Does the buyer of the FlexibleRepo receive any dividend or cash payments as the result of a corporate action  on any of the collateral instruments, or are these amounts paid to the seller.  Referred to as \&quot;manufactured payments\&quot; in the UK, and valid only under a repo with GMRA in Europe
    collateral_instruments=[],  # optional — List of any collateral instruments.
    collateral_value=0.0,  # optional — Total value of the collateral before any margin or haircut applied.  Can be provided instead of PurchasePrice, so that PurchasePrice can be inferred from the CollateralValue and one of  Haircut or Margin.
    defer_manufactured_payments=True  # optional — Indicates whether manufactured collateral payments are capitalised (i.e. deferred). Capitalised payments will  be deferred to the maturity date of the repo and if applicable interest will be accrued at the repo rate.  Defaults to false.
)
```

- [CollateralInstrument](CollateralInstrument.md) — used in `collateral_instruments`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

