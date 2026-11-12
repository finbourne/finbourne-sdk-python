# TaxClassificationDecisionStep

One question the decision tree asked on the way to the leaf.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **order** | **int** | Required | The position of the step in the decision trace, starting at 1. |
| **rule** | **str** | Required | The decision-tree rule the step evaluated. |
| **question** | **str** | Required | The question the rule asked of the inputs. |
| **answer** | **str** | Required | The answer the rule took. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TaxClassificationDecisionStep import TaxClassificationDecisionStep

instance = TaxClassificationDecisionStep(
    order=0,  # required — The position of the step in the decision trace, starting at 1.
    rule="...",  # required — The decision-tree rule the step evaluated.
    question="...",  # required — The question the rule asked of the inputs.
    answer="..."  # required — The answer the rule took.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

