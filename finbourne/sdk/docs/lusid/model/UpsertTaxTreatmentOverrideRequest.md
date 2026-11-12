# UpsertTaxTreatmentOverrideRequest

Pins an instrument to a treatment leaf in place of the system-derived one.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **treatment** | **str** | Required | The treatment leaf to pin the instrument to, replacing the system-derived one. Available values: OutsideBlagab, LoanRelationship, IndexLinkedGilt, PrivateEquity, RealEstate, FinancialFuture, PooledDerivative, DerivativeProfitAndLoss, NonTransparentScheme, BondFund, TransparentScheme, StandardEquity, Exempt. |
| **effective_at** | **datetime** | Optional | The effective date the override applies from. Defaults to the start of time if not specified. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpsertTaxTreatmentOverrideRequest import UpsertTaxTreatmentOverrideRequest

instance = UpsertTaxTreatmentOverrideRequest(
    treatment="...",  # required — The treatment leaf to pin the instrument to, replacing the system-derived one. Available values: OutsideBlagab, LoanRelationship, IndexLinkedGilt, PrivateEquity, RealEstate, FinancialFuture, PooledDerivative, DerivativeProfitAndLoss, NonTransparentScheme, BondFund, TransparentScheme, StandardEquity, Exempt.
    effective_at=datetime.now()  # optional — The effective date the override applies from. Defaults to the start of time if not specified.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

