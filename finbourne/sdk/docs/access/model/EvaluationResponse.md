# EvaluationResponse

The result of an evaluation request
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **result** | [EvaluationResult](EvaluationResult.md) | Required | *No description available.* |
| **detailed_message** | **str** | Optional | In the case of the evaluation being denied a message may be returned |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.access.models.EvaluationResponse import EvaluationResponse

instance = EvaluationResponse(
    result=EvaluationResult(...),  # required
    detailed_message="..."  # optional — In the case of the evaluation being denied a message may be returned
)
```


## Related Models

- [EvaluationResult](EvaluationResult.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

