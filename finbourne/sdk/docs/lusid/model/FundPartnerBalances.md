# FundPartnerBalances

The capital balances of one register line, in the commitment currency.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **committed** | **float** | Required | The committed capital. |
| **uncalled_commitment** | **float** | Required | The commitment not yet called. |
| **paid_in** | **float** | Required | The capital paid in. |
| **returned** | **float** | Required | The capital returned. |
| **recallable** | **float** | Required | The returned capital that may be recalled. |
| **unfunded** | **float** | Required | The unfunded capital. |
| **funded** | **float** | Required | The funded capital. |
| **outstanding_calls** | **float** | Optional | Capital called but not yet paid in. Omitted on a register line that has had returned capital marked recallable, since recalled capital is not yet tracked as a balance and the figure would exclude it. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundPartnerBalances import FundPartnerBalances

instance = FundPartnerBalances(
    committed=0.0,  # required — The committed capital.
    uncalled_commitment=0.0,  # required — The commitment not yet called.
    paid_in=0.0,  # required — The capital paid in.
    returned=0.0,  # required — The capital returned.
    recallable=0.0,  # required — The returned capital that may be recalled.
    unfunded=0.0,  # required — The unfunded capital.
    funded=0.0,  # required — The funded capital.
    outstanding_calls=0.0  # optional — Capital called but not yet paid in. Omitted on a register line that has had returned capital marked recallable, since recalled capital is not yet tracked as a balance and the figure would exclude it.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

