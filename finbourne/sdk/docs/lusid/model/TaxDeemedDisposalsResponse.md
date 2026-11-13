# TaxDeemedDisposalsResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **fund_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **period** | [TaxAccountingPeriod](TaxAccountingPeriod.md) | Optional | *No description available.* |
| **disposals** | [List[TaxDeemedDisposalResponse]](TaxDeemedDisposalResponse.md) | Optional | The deemed disposals at the end of the period. |
| **vintages** | [List[TaxReturnVintage]](TaxReturnVintage.md) | Optional | The deemed-disposal vintages, one per period, that feed line D. |
| **matrix** | [List[TaxReturnSpreadInstalment]](TaxReturnSpreadInstalment.md) | Optional | The seven-period spreading matrix for the vintages. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TaxDeemedDisposalsResponse import TaxDeemedDisposalsResponse

instance = TaxDeemedDisposalsResponse(
    fund_id=ResourceId(...),  # optional
    period=TaxAccountingPeriod(...),  # optional
    disposals=[],  # optional — The deemed disposals at the end of the period.
    vintages=[],  # optional — The deemed-disposal vintages, one per period, that feed line D.
    matrix=[]  # optional — The seven-period spreading matrix for the vintages.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [TaxAccountingPeriod](TaxAccountingPeriod.md)
- [TaxDeemedDisposalResponse](TaxDeemedDisposalResponse.md) — used in `disposals`
- [TaxReturnVintage](TaxReturnVintage.md) — used in `vintages`
- [TaxReturnSpreadInstalment](TaxReturnSpreadInstalment.md) — used in `matrix`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

