# PartnerCapitalAccountMemo

The memo block of a capital account statement: commitment balances from the register at the period end.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **commitment** | **float** | Required | The partner&#39;s total commitment. |
| **uncalled_commitment** | **float** | Required | The commitment not yet called. |
| **recallable** | **float** | Required | Distributions that the fund may recall. |
| **available_commitment** | **float** | Required | The commitment available to call, being uncalled plus recallable. |
| **contributions_receivable** | **float** | Optional | Called contributions not yet received from the partner. Omitted when a register line of the partner has had returned capital marked recallable, since recalled capital is not yet tracked as a balance and the figure would exclude it. |
| **distributions_declared_not_paid** | **float** | Required | Distributions declared to the partner but not yet paid. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.PartnerCapitalAccountMemo import PartnerCapitalAccountMemo

instance = PartnerCapitalAccountMemo(
    commitment=0.0,  # required — The partner&#39;s total commitment.
    uncalled_commitment=0.0,  # required — The commitment not yet called.
    recallable=0.0,  # required — Distributions that the fund may recall.
    available_commitment=0.0,  # required — The commitment available to call, being uncalled plus recallable.
    contributions_receivable=0.0,  # optional — Called contributions not yet received from the partner. Omitted when a register line of the partner has had returned capital marked recallable, since recalled capital is not yet tracked as a balance and the figure would exclude it.
    distributions_declared_not_paid=0.0  # required — Distributions declared to the partner but not yet paid.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

