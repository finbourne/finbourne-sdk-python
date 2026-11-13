# TaxLedgerReconciliationHoldingResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **fund_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **period** | [TaxAccountingPeriod](TaxAccountingPeriod.md) | Optional | *No description available.* |
| **holding_id** | **str** | Optional | The identifier of the holding. For a company this is the pooled LUSID instrument identifier, for a fund the portfolio code and instrument identifier. |
| **instrument_id** | **str** | Optional | The LUSID unique identifier of the instrument. |
| **instrument_name** | **str** | Optional | The name of the instrument. |
| **portfolio_code** | **str** | Optional | The code of the portfolio the holding sits in, or the pooled marker for a company. |
| **ledger_realised** | **float** | Optional | The realised gain or loss recorded in the ledger for the holding. |
| **ledger_unrealised_movement** | **float** | Optional | The movement in unrealised gain or loss recorded in the ledger for the holding. |
| **tax_realised_unindexed** | **float** | Optional | The realised gain or loss for tax before indexation. |
| **tax_unrealised_movement_unindexed** | **float** | Optional | The movement in the unrealised gain or loss for tax before indexation. |
| **deemed_disposal_net** | **float** | Optional | The net deemed-disposal amount for the holding. |
| **loan_relationship_net** | **float** | Optional | The net loan relationship credit or debit for the holding. |
| **category** | **str** | Optional | The reconciliation category of the difference, when there is one. Available values: ExcludedHoldings, TaxCostAdjustments, OutOfSync, Scope, PoolAveraging, Matching, Indexation, KinkTest. |
| **difference** | **float** | Optional | The difference between the two sides. |
| **explanation** | **str** | Optional | The explanation of the difference. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TaxLedgerReconciliationHoldingResponse import TaxLedgerReconciliationHoldingResponse

instance = TaxLedgerReconciliationHoldingResponse(
    fund_id=ResourceId(...),  # optional
    period=TaxAccountingPeriod(...),  # optional
    holding_id="...",  # optional — The identifier of the holding. For a company this is the pooled LUSID instrument identifier, for a fund the portfolio code and instrument identifier.
    instrument_id="...",  # optional — The LUSID unique identifier of the instrument.
    instrument_name="...",  # optional — The name of the instrument.
    portfolio_code="...",  # optional — The code of the portfolio the holding sits in, or the pooled marker for a company.
    ledger_realised=0.0,  # optional — The realised gain or loss recorded in the ledger for the holding.
    ledger_unrealised_movement=0.0,  # optional — The movement in unrealised gain or loss recorded in the ledger for the holding.
    tax_realised_unindexed=0.0,  # optional — The realised gain or loss for tax before indexation.
    tax_unrealised_movement_unindexed=0.0,  # optional — The movement in the unrealised gain or loss for tax before indexation.
    deemed_disposal_net=0.0,  # optional — The net deemed-disposal amount for the holding.
    loan_relationship_net=0.0,  # optional — The net loan relationship credit or debit for the holding.
    category="...",  # optional — The reconciliation category of the difference, when there is one. Available values: ExcludedHoldings, TaxCostAdjustments, OutOfSync, Scope, PoolAveraging, Matching, Indexation, KinkTest.
    difference=0.0,  # optional — The difference between the two sides.
    explanation="..."  # optional — The explanation of the difference.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [TaxAccountingPeriod](TaxAccountingPeriod.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

