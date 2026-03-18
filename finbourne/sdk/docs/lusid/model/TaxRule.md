# TaxRule

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Required | A user-friendly name |
| **description** | **str** | Required | A description for this rule |
| **rate** | **float** | Required | The rate to be applied if all criteria are met |
| **match_criteria** | [List[MatchCriterion]](MatchCriterion.md) | Required | A set of criteria to be met for this rule to be applied |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TaxRule import TaxRule

instance = TaxRule(
    name="...",  # required — A user-friendly name
    description="...",  # required — A description for this rule
    rate=0.0,  # required — The rate to be applied if all criteria are met
    match_criteria=[]  # required — A set of criteria to be met for this rule to be applied
)
```

- [MatchCriterion](MatchCriterion.md) — used in `match_criteria`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

