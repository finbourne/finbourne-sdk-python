# TaxFundReconciliationHoldingResponse

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **fund_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **period** | [TaxAccountingPeriod](TaxAccountingPeriod.md) | Optional | *No description available.* |
| **holding_id** | **str** | Optional | The identifier of the holding. For a company this is the pooled LUSID instrument identifier, for a fund the portfolio code and instrument identifier. |
| **instrument_id** | **str** | Optional | The LUSID unique identifier of the instrument. |
| **instrument_name** | **str** | Optional | The name of the instrument. |
| **company_amount** | **float** | Optional | The company-level amount for the holding. |
| **fund_proxies** | [List[TaxFundReconciliationProxyRow]](TaxFundReconciliationProxyRow.md) | Optional | The member funds&#39; notional figures for the holding. |
| **difference** | **float** | Optional | The difference between the two sides. |
| **category** | **str** | Optional | The reconciliation category of the difference, when there is one. Available values: ExcludedHoldings, TaxCostAdjustments, OutOfSync, Scope, PoolAveraging, Matching, Indexation, KinkTest. |
| **explanation** | **str** | Optional | The explanation of the difference. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TaxFundReconciliationHoldingResponse import TaxFundReconciliationHoldingResponse

instance = TaxFundReconciliationHoldingResponse(
    fund_id=ResourceId(...),  # optional
    period=TaxAccountingPeriod(...),  # optional
    holding_id="...",  # optional — The identifier of the holding. For a company this is the pooled LUSID instrument identifier, for a fund the portfolio code and instrument identifier.
    instrument_id="...",  # optional — The LUSID unique identifier of the instrument.
    instrument_name="...",  # optional — The name of the instrument.
    company_amount=0.0,  # optional — The company-level amount for the holding.
    fund_proxies=[],  # optional — The member funds&#39; notional figures for the holding.
    difference=0.0,  # optional — The difference between the two sides.
    category="...",  # optional — The reconciliation category of the difference, when there is one. Available values: ExcludedHoldings, TaxCostAdjustments, OutOfSync, Scope, PoolAveraging, Matching, Indexation, KinkTest.
    explanation="..."  # optional — The explanation of the difference.
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [TaxAccountingPeriod](TaxAccountingPeriod.md)
- [TaxFundReconciliationProxyRow](TaxFundReconciliationProxyRow.md) — used in `fund_proxies`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

