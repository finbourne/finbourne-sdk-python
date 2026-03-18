# AmortisationRule

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **name** | **str** | Required | The name of the rule. |
| **description** | **str** | Optional | A description of the rule. |
| **filter** | **str** | Required | The filter for this rule. |
| **amortisation_method** | **str** | Required | The filter for this rule. |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.AmortisationRule import AmortisationRule

instance = AmortisationRule(
    name="...",  # required — The name of the rule.
    description="...",  # optional — A description of the rule.
    filter="...",  # required — The filter for this rule.
    amortisation_method="..."  # required — The filter for this rule.
)
```



[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

