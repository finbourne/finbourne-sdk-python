# CollateralOptimisationTerms

When a cheaper arrangement for the agreement's trades is worth recommending.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **novation_cost** | **float** | Required | The one-off cost of novating trades away from the counterparty, in the agreement&#39;s base currency. At least 0. |
| **min_saving_per_day** | **float** | Required | A change saving no more than this a day is not recommended. At least 0. |
| **max_payback_days** | **int** | Required | A change whose one-off cost takes longer than this many days to earn back is not recommended. At least 0. |
| **max_per_agreement** | **int** | Required | The most recommendations kept for the agreement, best first. Zero means no cap. At least 0. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CollateralOptimisationTerms import CollateralOptimisationTerms

instance = CollateralOptimisationTerms(
    novation_cost=0.0,  # required — The one-off cost of novating trades away from the counterparty, in the agreement&#39;s base currency. At least 0.
    min_saving_per_day=0.0,  # required — A change saving no more than this a day is not recommended. At least 0.
    max_payback_days=0,  # required — A change whose one-off cost takes longer than this many days to earn back is not recommended. At least 0.
    max_per_agreement=0  # required — The most recommendations kept for the agreement, best first. Zero means no cap. At least 0.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

