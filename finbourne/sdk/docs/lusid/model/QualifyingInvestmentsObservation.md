# QualifyingInvestmentsObservation

The qualifying-investments test result for one scheme on one day.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **var_date** | **datetime** | Required | The date the test was evaluated for. |
| **non_equity_percent** | **float** | Required | The percentage of the scheme&#39;s assets that were qualifying (non-equity) investments on the date. |
| **is_bond_fund** | **bool** | Required | Whether more than the threshold percentage of the scheme&#39;s assets were qualifying investments on the date, making it a bond fund. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.QualifyingInvestmentsObservation import QualifyingInvestmentsObservation

instance = QualifyingInvestmentsObservation(
    var_date=datetime.now(),  # required — The date the test was evaluated for.
    non_equity_percent=0.0,  # required — The percentage of the scheme&#39;s assets that were qualifying (non-equity) investments on the date.
    is_bond_fund=True  # required — Whether more than the threshold percentage of the scheme&#39;s assets were qualifying investments on the date, making it a bond fund.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

