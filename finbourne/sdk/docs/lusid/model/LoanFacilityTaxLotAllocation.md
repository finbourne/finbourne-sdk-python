# LoanFacilityTaxLotAllocation

Contract-level state for a single tax lot on a single contract. These values live on the contract holding.                Each allocation names its own contract rather than being grouped under one, so the event carries a flat  list. A tax lot holding a balance on two contracts appears twice, once per contract.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **contract_details** | [ContractDetails](ContractDetails.md) | Required | *No description available.* |
| **tax_lot_id** | **str** | Required | The tax lot being set, identified by the transaction id of the trade that opened it. |
| **balance** | **float** | Required | The desired settled balance for this tax lot on this contract, in the contract&#39;s own currency. This  replaces the pro-rata balance that the opening trade derived from the global facility state, which is  how a non-pro-rata position is expressed. |
| **balance_in_facility_ccy** | **float** | Optional | The desired balance expressed in the facility currency. Required when the contract currency differs  from the facility currency, and defaults to Balance otherwise. |
| **accrued_interest** | **float** | Optional | Interest accrued on this tax lot&#39;s balance on this contract, as at the start of the event&#39;s date, in  the contract&#39;s own currency. Distinct from the facility&#39;s own accrual on its undrawn amount - the two  are summed to give the accrued interest reported against the holding.                Omit it and the lot&#39;s accrual is left as it is, so a migrated lot accrues from its own trade date. |
| **pik_accrued_interest** | **float** | Optional | Payment-in-kind interest accrued on this tax lot, as at the start of the event&#39;s date, for a contract  carrying a PIK schedule. Tracked separately from cash-settled accrual and never derived. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.LoanFacilityTaxLotAllocation import LoanFacilityTaxLotAllocation

instance = LoanFacilityTaxLotAllocation(
    contract_details=ContractDetails(...),  # required
    tax_lot_id="...",  # required — The tax lot being set, identified by the transaction id of the trade that opened it.
    balance=0.0,  # required — The desired settled balance for this tax lot on this contract, in the contract&#39;s own currency. This  replaces the pro-rata balance that the opening trade derived from the global facility state, which is  how a non-pro-rata position is expressed.
    balance_in_facility_ccy=0.0,  # optional — The desired balance expressed in the facility currency. Required when the contract currency differs  from the facility currency, and defaults to Balance otherwise.
    accrued_interest=0.0,  # optional — Interest accrued on this tax lot&#39;s balance on this contract, as at the start of the event&#39;s date, in  the contract&#39;s own currency. Distinct from the facility&#39;s own accrual on its undrawn amount - the two  are summed to give the accrued interest reported against the holding.                Omit it and the lot&#39;s accrual is left as it is, so a migrated lot accrues from its own trade date.
    pik_accrued_interest=0.0  # optional — Payment-in-kind interest accrued on this tax lot, as at the start of the event&#39;s date, for a contract  carrying a PIK schedule. Tracked separately from cash-settled accrual and never derived.
)
```


## Related Models

- [ContractDetails](ContractDetails.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

