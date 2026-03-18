# UpdateTaxRuleSetRequest

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **display_name** | **str** | Required |  |
| **description** | **str** | Required |  |
| **rules** | [List[TaxRule]](TaxRule.md) | Required |  |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.UpdateTaxRuleSetRequest import UpdateTaxRuleSetRequest

instance = UpdateTaxRuleSetRequest(
    display_name="...",  # required — 
    description="...",  # required — 
    rules=[]  # required — 
)
```

- [TaxRule](TaxRule.md) — used in `rules`


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

