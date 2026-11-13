# TaxReturnResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **fund_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **period** | [TaxAccountingPeriod](TaxAccountingPeriod.md) | Optional | *No description available.* |
| **status** | **str** | Optional | The workflow status of the return. Available values: Draft, Prepared, Reviewed, SignedOff, Final. Available values: Draft, Prepared, Reviewed, SignedOff, Final. |
| **steps** | [List[TaxReturnWorkflowStep]](TaxReturnWorkflowStep.md) | Optional | The workflow history of the return in the order the steps were taken. |
| **line_a** | [List[TaxReturnDisposalRow]](TaxReturnDisposalRow.md) | Optional | Chargeable gains and allowable losses on actual disposals in the period. |
| **line_a_total** | **float** | Optional | The total of line A, in whole pounds. |
| **vintages** | [List[TaxReturnVintage]](TaxReturnVintage.md) | Optional | The deemed-disposal vintages, one per period, that feed line D. |
| **instalments** | [List[TaxReturnSpreadInstalment]](TaxReturnSpreadInstalment.md) | Optional | The instalments of earlier vintages that fall into the period. |
| **line_d_total** | **float** | Optional | The total of line D, in whole pounds. |
| **loan_relationships** | [List[TaxReturnLoanRelationshipRow]](TaxReturnLoanRelationshipRow.md) | Optional | The loan relationship and derivative holdings that make up line LR. Empty for a fund. |
| **line_lr_total** | **float** | Optional | The total of line LR, in whole pounds. Zero for a fund. |
| **outside** | [List[TaxReturnExcludedRow]](TaxReturnExcludedRow.md) | Optional | The holdings excluded from the return, with the reason. |
| **summary** | [List[TaxReturnMemoRow]](TaxReturnMemoRow.md) | Optional | Memo rows such as the tax at the applicable rate and the minimum-profits trade profit. |
| **sync_break_open** | **bool** | Optional | True when the tax records are out of sync with the ledger and the return cannot advance past Reviewed. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TaxReturnResponse import TaxReturnResponse

instance = TaxReturnResponse(
    fund_id=ResourceId(...),  # optional
    period=TaxAccountingPeriod(...),  # optional
    status="...",  # optional — The workflow status of the return. Available values: Draft, Prepared, Reviewed, SignedOff, Final. Available values: Draft, Prepared, Reviewed, SignedOff, Final.
    steps=[],  # optional — The workflow history of the return in the order the steps were taken.
    line_a=[],  # optional — Chargeable gains and allowable losses on actual disposals in the period.
    line_a_total=0.0,  # optional — The total of line A, in whole pounds.
    vintages=[],  # optional — The deemed-disposal vintages, one per period, that feed line D.
    instalments=[],  # optional — The instalments of earlier vintages that fall into the period.
    line_d_total=0.0,  # optional — The total of line D, in whole pounds.
    loan_relationships=[],  # optional — The loan relationship and derivative holdings that make up line LR. Empty for a fund.
    line_lr_total=0.0,  # optional — The total of line LR, in whole pounds. Zero for a fund.
    outside=[],  # optional — The holdings excluded from the return, with the reason.
    summary=[],  # optional — Memo rows such as the tax at the applicable rate and the minimum-profits trade profit.
    sync_break_open=True  # optional — True when the tax records are out of sync with the ledger and the return cannot advance past Reviewed.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [TaxAccountingPeriod](TaxAccountingPeriod.md)
- [TaxReturnWorkflowStep](TaxReturnWorkflowStep.md) — used in `steps`
- [TaxReturnDisposalRow](TaxReturnDisposalRow.md) — used in `line_a`
- [TaxReturnVintage](TaxReturnVintage.md) — used in `vintages`
- [TaxReturnSpreadInstalment](TaxReturnSpreadInstalment.md) — used in `instalments`
- [TaxReturnLoanRelationshipRow](TaxReturnLoanRelationshipRow.md) — used in `loan_relationships`
- [TaxReturnExcludedRow](TaxReturnExcludedRow.md) — used in `outside`
- [TaxReturnMemoRow](TaxReturnMemoRow.md) — used in `summary`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

