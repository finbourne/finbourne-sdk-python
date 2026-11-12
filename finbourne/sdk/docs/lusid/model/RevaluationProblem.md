# RevaluationProblem

A reason why a revaluation amount could not be populated.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Optional | A machine-readable code identifying the type of problem (e.g. MissingFxRate, MissingBookedFxRate). |
| **message** | **str** | Optional | A human-readable description of why the revaluation amount could not be populated. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RevaluationProblem import RevaluationProblem

instance = RevaluationProblem(
    code="...",  # optional — A machine-readable code identifying the type of problem (e.g. MissingFxRate, MissingBookedFxRate).
    message="..."  # optional — A human-readable description of why the revaluation amount could not be populated.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

