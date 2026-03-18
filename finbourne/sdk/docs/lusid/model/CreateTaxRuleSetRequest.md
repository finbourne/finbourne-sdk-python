# CreateTaxRuleSetRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **display_name** | **str** | Required |  |
| **description** | **str** | Required |  |
| **output_property_key** | **str** | Required |  |
| **rules** | [List[TaxRule]](TaxRule.md) | Required |  |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.CreateTaxRuleSetRequest import CreateTaxRuleSetRequest

instance = CreateTaxRuleSetRequest(
    id=ResourceId(...),  # required
    display_name="...",  # required — 
    description="...",  # required — 
    output_property_key="...",  # required — 
    rules=[]  # required — 
)
```


## Related Models

- [ResourceId](ResourceId.md)
- [TaxRule](TaxRule.md) — used in `rules`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

