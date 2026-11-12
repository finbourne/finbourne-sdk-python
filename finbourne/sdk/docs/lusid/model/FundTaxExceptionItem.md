# FundTaxExceptionItem

A tax exception row seen across funds, so the fund and the owning life-company entity travel with it.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **client** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **fund** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **id** | **str** | Required | An identifier stable within a response, built from the category, portfolio and instrument. |
| **category** | **str** | Required | The kind of exception: UnmatchedDisposal, NegativePool, MissingValuation or UnclassifiedInstrument. |
| **severity** | **str** | Required | Error when the exception blocks the tax computation, Warning when it casts doubt on it. |
| **portfolio** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **instrument** | **str** | Optional | The LUSID unique identifier of the instrument the exception was raised against. |
| **message** | **str** | Required | A description of the exception. |
| **raised_at** | **datetime** | Required | The asAt the exception was observed at. |
| **tax_at_stake** | **float** | Optional | The tax effect, in the Fund&#39;s base currency, of the position or gain the exception blocks, at the Fund&#39;s configured rate. Absent when the rate or the exposure is not known. |
| **root_cause** | [TaxExceptionRootCause](TaxExceptionRootCause.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundTaxExceptionItem import FundTaxExceptionItem

instance = FundTaxExceptionItem(
    client=ResourceId(...),  # optional
    fund=ResourceId(...),  # required
    id="...",  # required — An identifier stable within a response, built from the category, portfolio and instrument.
    category="...",  # required — The kind of exception: UnmatchedDisposal, NegativePool, MissingValuation or UnclassifiedInstrument.
    severity="...",  # required — Error when the exception blocks the tax computation, Warning when it casts doubt on it.
    portfolio=ResourceId(...),  # required
    instrument="...",  # optional — The LUSID unique identifier of the instrument the exception was raised against.
    message="...",  # required — A description of the exception.
    raised_at=datetime.now(),  # required — The asAt the exception was observed at.
    tax_at_stake=0.0,  # optional — The tax effect, in the Fund&#39;s base currency, of the position or gain the exception blocks, at the Fund&#39;s configured rate. Absent when the rate or the exposure is not known.
    root_cause=TaxExceptionRootCause(...)  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [TaxExceptionRootCause](TaxExceptionRootCause.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

