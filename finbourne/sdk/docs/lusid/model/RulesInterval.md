# RulesInterval

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **effective_range** | [DateRange](DateRange.md) | Required | *No description available.* |
| **rules** | [List[AmortisationRule]](AmortisationRule.md) | Required | The rules of this rule set. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.RulesInterval import RulesInterval

instance = RulesInterval(
    effective_range=DateRange(...),  # required
    rules=[]  # required — The rules of this rule set.
)
```


## Related Models

- [DateRange](DateRange.md)
- [AmortisationRule](AmortisationRule.md) — used in `rules`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

