# TaxLedgerReconciliationResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **fund_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **period** | [TaxAccountingPeriod](TaxAccountingPeriod.md) | Optional | *No description available.* |
| **ledger_capital_gain_loss** | **float** | Optional | The realised and unrealised capital gain or loss recorded in the ledger for the period. |
| **comparable_tax_figure** | **float** | Optional | The tax figure on the same basis as the ledger, before the return adjustments. |
| **differences** | [List[TaxReconciliationDifferenceRow]](TaxReconciliationDifferenceRow.md) | Optional | The explained differences between the two sides, by holding. |
| **unexplained** | **float** | Optional | The part of the difference not explained by any category. Nil when the reconciliation is complete. |
| **bridge** | [List[TaxReconciliationBridgeRow]](TaxReconciliationBridgeRow.md) | Optional | The bridge from the ledger figure to the return total. |
| **return_total** | **float** | Optional | The total of lines A, D and LR. |
| **bridge_unexplained** | **float** | Optional | The part of the bridge not explained. Nil when the bridge is complete. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TaxLedgerReconciliationResponse import TaxLedgerReconciliationResponse

instance = TaxLedgerReconciliationResponse(
    fund_id=ResourceId(...),  # optional
    period=TaxAccountingPeriod(...),  # optional
    ledger_capital_gain_loss=0.0,  # optional — The realised and unrealised capital gain or loss recorded in the ledger for the period.
    comparable_tax_figure=0.0,  # optional — The tax figure on the same basis as the ledger, before the return adjustments.
    differences=[],  # optional — The explained differences between the two sides, by holding.
    unexplained=0.0,  # optional — The part of the difference not explained by any category. Nil when the reconciliation is complete.
    bridge=[],  # optional — The bridge from the ledger figure to the return total.
    return_total=0.0,  # optional — The total of lines A, D and LR.
    bridge_unexplained=0.0  # optional — The part of the bridge not explained. Nil when the bridge is complete.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [TaxAccountingPeriod](TaxAccountingPeriod.md)
- [TaxReconciliationDifferenceRow](TaxReconciliationDifferenceRow.md) — used in `differences`
- [TaxReconciliationBridgeRow](TaxReconciliationBridgeRow.md) — used in `bridge`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

