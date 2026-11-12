# FundPartnerUnfundedReconciliationWarning

A soft warning on an unfunded commitment statement: the statement is still produced, with a caveat.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Required | The warning. PeriodStartsBeforeAdmission: the period opens before the partner was admitted, so the opening balances are zero and the admission commitment is counted as a commitment change. |
| **admitted_on** | **datetime** | Optional | For PeriodStartsBeforeAdmission, the date the partner was admitted to the fund. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.FundPartnerUnfundedReconciliationWarning import FundPartnerUnfundedReconciliationWarning

instance = FundPartnerUnfundedReconciliationWarning(
    code="...",  # required — The warning. PeriodStartsBeforeAdmission: the period opens before the partner was admitted, so the opening balances are zero and the admission commitment is counted as a commitment change.
    admitted_on=datetime.now()  # optional — For PeriodStartsBeforeAdmission, the date the partner was admitted to the fund.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

