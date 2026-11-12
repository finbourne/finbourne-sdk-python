# QualifyingInvestmentsCrossing

A flip of the qualifying-investments result between two consecutive observed days.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **var_from** | **datetime** | Required | The date of the observation before the flip. |
| **to** | **datetime** | Required | The date of the observation after the flip. |
| **was_bond_fund_before** | **bool** | Required | Whether the scheme was a bond fund on the From date. |
| **is_bond_fund_after** | **bool** | Required | Whether the scheme was a bond fund on the To date. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.QualifyingInvestmentsCrossing import QualifyingInvestmentsCrossing

instance = QualifyingInvestmentsCrossing(
    var_from=datetime.now(),  # required — The date of the observation before the flip.
    to=datetime.now(),  # required — The date of the observation after the flip.
    was_bond_fund_before=True,  # required — Whether the scheme was a bond fund on the From date.
    is_bond_fund_after=True  # required — Whether the scheme was a bond fund on the To date.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

