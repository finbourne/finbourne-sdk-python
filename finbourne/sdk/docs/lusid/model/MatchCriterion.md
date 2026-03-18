# MatchCriterion

A condition to be evaluated.  Each supported CriterionType has a corresponding schema.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **criterion_type** | **str** | Required | The available values are: PropertyValueEquals, PropertyValueIn, SubHoldingKeyValueEquals |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.MatchCriterion import MatchCriterion

instance = MatchCriterion(
    criterion_type="..."  # required — The available values are: PropertyValueEquals, PropertyValueIn, SubHoldingKeyValueEquals
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

