# TaxReconciliationDifferenceRow

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **holding_id** | **str** | Optional | The identifier of the holding. For a company this is the pooled LUSID instrument identifier, for a fund the portfolio code and instrument identifier. |
| **instrument_id** | **str** | Optional | The LUSID unique identifier of the instrument. |
| **instrument_name** | **str** | Optional | The name of the instrument. |
| **category** | **str** | Optional | The reconciliation category. Available values: ExcludedHoldings, TaxCostAdjustments, OutOfSync, Scope, PoolAveraging, Matching, Indexation, KinkTest. Available values: ExcludedHoldings, TaxCostAdjustments, OutOfSync, Scope, PoolAveraging, Matching, Indexation, KinkTest. |
| **compared_amount** | **float** | Optional | The amount on the side being reconciled from. |
| **tax_amount** | **float** | Optional | The amount on the tax side. |
| **difference** | **float** | Optional | The difference between the two sides. |
| **explanation** | **str** | Optional | The explanation of the difference. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TaxReconciliationDifferenceRow import TaxReconciliationDifferenceRow

instance = TaxReconciliationDifferenceRow(
    holding_id="...",  # optional — The identifier of the holding. For a company this is the pooled LUSID instrument identifier, for a fund the portfolio code and instrument identifier.
    instrument_id="...",  # optional — The LUSID unique identifier of the instrument.
    instrument_name="...",  # optional — The name of the instrument.
    category="...",  # optional — The reconciliation category. Available values: ExcludedHoldings, TaxCostAdjustments, OutOfSync, Scope, PoolAveraging, Matching, Indexation, KinkTest. Available values: ExcludedHoldings, TaxCostAdjustments, OutOfSync, Scope, PoolAveraging, Matching, Indexation, KinkTest.
    compared_amount=0.0,  # optional — The amount on the side being reconciled from.
    tax_amount=0.0,  # optional — The amount on the tax side.
    difference=0.0,  # optional — The difference between the two sides.
    explanation="..."  # optional — The explanation of the difference.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

