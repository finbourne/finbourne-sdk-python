# ResultKeyRule

Base class for representing result key rules in LUSID, which describe how to resolve (unit) result data.  This base class should not be directly instantiated; each supported ResultKeyRuleType has a corresponding inherited class.
## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **result_key_rule_type** | **str** | Required | The available values are: Invalid, ResultDataKeyRule, PortfolioResultDataKeyRule |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.ResultKeyRule import ResultKeyRule

instance = ResultKeyRule(
    result_key_rule_type="..."  # required — The available values are: Invalid, ResultDataKeyRule, PortfolioResultDataKeyRule
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

