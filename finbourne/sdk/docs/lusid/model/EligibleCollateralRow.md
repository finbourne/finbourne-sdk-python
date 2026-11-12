# EligibleCollateralRow

One class of eligible collateral and how it is valued, as stored on a schedule.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Required | The stable key the row is referred to by. Unique within the schedule. |
| **description** | **str** | Optional | A description of the row. Optional. |
| **selector** | [EligibleCollateralAssetSelector](EligibleCollateralAssetSelector.md) | Required | *No description available.* |
| **valuation_percentage** | **float** | Required | The fraction of an asset&#39;s value that is accepted as collateral, for example 0.95 for 95%. Greater than 0 and at most 1. |
| **fx_haircut** | **float** | Optional | The further fraction deducted when the asset&#39;s currency is not the agreement&#39;s base currency, so that the effective valuation percentage is ValuationPercentage - FxHaircut. At least 0 and less than the valuationPercentage. Not allowed for a BaseCurrencyCash selector. Optional. |
| **min_residual_maturity_years** | **float** | Optional | The inclusive lower bound of the residual maturity in years that the row applies to. Only allowed for an Instrument selector. Optional. |
| **max_residual_maturity_years** | **float** | Optional | The exclusive upper bound of the residual maturity in years that the row applies to. Only allowed for an Instrument selector. Optional. |
| **concentration_group** | **str** | Optional | The group the row&#39;s assets count towards for a concentration limit, for example &#39;sovereign&#39; or &#39;issuer&#39;. Rows naming the same group share one limit. Required when a concentrationLimit is set. Optional. |
| **concentration_limit** | **float** | Optional | The largest fraction of the collateral held plus the call that assets of the row&#39;s concentration group may make up, for example 0.3 for 30%. Greater than 0 and at most 1. Required when a concentrationGroup is set. Optional. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.EligibleCollateralRow import EligibleCollateralRow

instance = EligibleCollateralRow(
    code="...",  # required — The stable key the row is referred to by. Unique within the schedule.
    description="...",  # optional — A description of the row. Optional.
    selector=EligibleCollateralAssetSelector(...),  # required
    valuation_percentage=0.0,  # required — The fraction of an asset&#39;s value that is accepted as collateral, for example 0.95 for 95%. Greater than 0 and at most 1.
    fx_haircut=0.0,  # optional — The further fraction deducted when the asset&#39;s currency is not the agreement&#39;s base currency, so that the effective valuation percentage is ValuationPercentage - FxHaircut. At least 0 and less than the valuationPercentage. Not allowed for a BaseCurrencyCash selector. Optional.
    min_residual_maturity_years=0.0,  # optional — The inclusive lower bound of the residual maturity in years that the row applies to. Only allowed for an Instrument selector. Optional.
    max_residual_maturity_years=0.0,  # optional — The exclusive upper bound of the residual maturity in years that the row applies to. Only allowed for an Instrument selector. Optional.
    concentration_group="...",  # optional — The group the row&#39;s assets count towards for a concentration limit, for example &#39;sovereign&#39; or &#39;issuer&#39;. Rows naming the same group share one limit. Required when a concentrationLimit is set. Optional.
    concentration_limit=0.0  # optional — The largest fraction of the collateral held plus the call that assets of the row&#39;s concentration group may make up, for example 0.3 for 30%. Greater than 0 and at most 1. Required when a concentrationGroup is set. Optional.
)
```

- [EligibleCollateralAssetSelector](EligibleCollateralAssetSelector.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

