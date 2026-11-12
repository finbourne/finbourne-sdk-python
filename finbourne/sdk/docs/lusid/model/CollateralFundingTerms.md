# CollateralFundingTerms

What margin posted under the agreement costs us: the annual rate it is funded at, the basis it accrues on and the  lending fee assumed forgone on a security with no fee quote of its own when collateral is ranked.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **rate** | **float** | Required | The annual rate posted margin is funded at, as a fraction, for example 0.053 for 5.3%. Between -1 and 1. |
| **day_count_basis** | **int** | Required | The number of days in the year the funding rate accrues over. Either 360 or 365. |
| **default_lending_fee** | **float** | Optional | The annual lending fee, as a fraction, assumed forgone on a security with no fee quote of its own when collateral is ranked. Between 0 and 1. A security with no fee at all cannot be ranked. Optional. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CollateralFundingTerms import CollateralFundingTerms

instance = CollateralFundingTerms(
    rate=0.0,  # required — The annual rate posted margin is funded at, as a fraction, for example 0.053 for 5.3%. Between -1 and 1.
    day_count_basis=0,  # required — The number of days in the year the funding rate accrues over. Either 360 or 365.
    default_lending_fee=0.0  # optional — The annual lending fee, as a fraction, assumed forgone on a security with no fee quote of its own when collateral is ranked. Between 0 and 1. A security with no fee at all cannot be ranked. Optional.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

