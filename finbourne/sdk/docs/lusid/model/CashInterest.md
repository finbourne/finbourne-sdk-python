# CashInterest

Interest accrued on posted cash.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **index** | **str** | Required | The name of the rate index. |
| **spread_bps** | **int** | Required | The spread over the index, in basis points. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CashInterest import CashInterest

instance = CashInterest(
    index="...",  # required — The name of the rate index.
    spread_bps=0  # required — The spread over the index, in basis points.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

