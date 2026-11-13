# TaxReturnLoanRelationshipRow

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **holding_id** | **str** | Optional | The identifier of the holding. For a company this is the pooled LUSID instrument identifier, for a fund the portfolio code and instrument identifier. |
| **instrument_id** | **str** | Optional | The LUSID unique identifier of the instrument. |
| **instrument_name** | **str** | Optional | The name of the instrument. |
| **portfolio_code** | **str** | Optional | The code of the portfolio the holding sits in, or the pooled marker for a company. |
| **ledger_amount** | **float** | Optional | The loan relationship credit or debit recorded in the ledger. |
| **uplift_excluded** | **float** | Optional | The uplift excluded from the loan relationship figure. |
| **net_credit_debit** | **float** | Optional | The net loan relationship credit or debit, after the uplift is excluded. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TaxReturnLoanRelationshipRow import TaxReturnLoanRelationshipRow

instance = TaxReturnLoanRelationshipRow(
    holding_id="...",  # optional — The identifier of the holding. For a company this is the pooled LUSID instrument identifier, for a fund the portfolio code and instrument identifier.
    instrument_id="...",  # optional — The LUSID unique identifier of the instrument.
    instrument_name="...",  # optional — The name of the instrument.
    portfolio_code="...",  # optional — The code of the portfolio the holding sits in, or the pooled marker for a company.
    ledger_amount=0.0,  # optional — The loan relationship credit or debit recorded in the ledger.
    uplift_excluded=0.0,  # optional — The uplift excluded from the loan relationship figure.
    net_credit_debit=0.0  # optional — The net loan relationship credit or debit, after the uplift is excluded.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

