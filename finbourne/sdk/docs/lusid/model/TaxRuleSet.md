# TaxRuleSet

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **display_name** | **str** | Required | A user-friendly name |
| **description** | **str** | Required | A description of what this rule set is for |
| **output_property_key** | **str** | Required | The property key that this rule set will write to |
| **rules** | [List[TaxRule]](TaxRule.md) | Required | The rules of this rule set, which stipulate what rate to apply (i.e. write to the OutputPropertyKey) under certain conditions |
| **version** | [Version](Version.md) | Optional | *No description available.* |
| **links** | [List[Link]](Link.md) | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.TaxRuleSet import TaxRuleSet

instance = TaxRuleSet(
    id=ResourceId(...),  # required
    display_name="...",  # required — A user-friendly name
    description="...",  # required — A description of what this rule set is for
    output_property_key="...",  # required — The property key that this rule set will write to
    rules=[],  # required — The rules of this rule set, which stipulate what rate to apply (i.e. write to the OutputPropertyKey) under certain conditions
    version=Version(...),  # optional
    links=[]  # optional
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [TaxRule](TaxRule.md) — used in `rules`
- [Version](Version.md)
- [Link](Link.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

