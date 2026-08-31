# FlexibleLoanPricerOptions

Model options for instruments of type flexibleDeposit and flexibleLoan when used on a standalone basis.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **set_clean_pvto_zero** | **bool** | Required | If set to true the CleanPV will be set to zero in valuations and PV will effectively just be the Accrual. |
| **model_options_type** | **str** | Required | Available values: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, CdsModelOptions, FlexibleLoanPricerOptions, HullWhiteModelOptions, BondLookupModelOptions. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FlexibleLoanPricerOptions import FlexibleLoanPricerOptions

instance = FlexibleLoanPricerOptions(
    set_clean_pvto_zero=True,  # required — If set to true the CleanPV will be set to zero in valuations and PV will effectively just be the Accrual.
    model_options_type="..."  # required — Available values: Invalid, OpaqueModelOptions, EmptyModelOptions, IndexModelOptions, FxForwardModelOptions, FundingLegModelOptions, EquityModelOptions, CdsModelOptions, FlexibleLoanPricerOptions, HullWhiteModelOptions, BondLookupModelOptions.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

