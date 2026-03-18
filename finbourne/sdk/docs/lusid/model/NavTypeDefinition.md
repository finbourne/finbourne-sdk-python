# NavTypeDefinition

## Properties

| Name | Type | Required | Description |
|------|------|----------|-------------|
| **code** | **str** | Optional | *No description available.* |
| **display_name** | **str** | Optional | *No description available.* |
| **description** | **str** | Optional | *No description available.* |
| **chart_of_accounts_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **posting_module_codes** | **List[str]** | Optional | *No description available.* |
| **cleardown_module_codes** | **List[str]** | Optional | *No description available.* |
| **valuation_recipe_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **holding_recipe_id** | [ResourceId](ResourceId.md) | Required | *No description available.* |
| **accounting_method** | **str** | Required | *No description available.* |
| **sub_holding_keys** | **List[str]** | Optional | Set of unique holding identifiers, e.g. trader, desk, strategy. |
| **amortisation_method** | **str** | Required | *No description available.* |
| **transaction_type_scope** | **str** | Required | *No description available.* |
| **cash_gain_loss_calculation_date** | **str** | Required | *No description available.* |
| **amortisation_rule_set_id** | [ResourceId](ResourceId.md) | Optional | *No description available.* |
| **leader_nav_type_code** | **str** | Optional | *No description available.* |
| **transaction_template_scope** | **str** | Optional | *No description available.* |


## Usage

### Creating from keyword arguments

```python
from finbourne.sdk.services.lusid.models.NavTypeDefinition import NavTypeDefinition

instance = NavTypeDefinition(
    code="...",  # optional
    display_name="...",  # optional
    description="...",  # optional
    chart_of_accounts_id=ResourceId(...),  # required
    posting_module_codes=,  # optional
    cleardown_module_codes=,  # optional
    valuation_recipe_id=ResourceId(...),  # required
    holding_recipe_id=ResourceId(...),  # required
    accounting_method="...",  # required
    sub_holding_keys=,  # optional — Set of unique holding identifiers, e.g. trader, desk, strategy.
    amortisation_method="...",  # required
    transaction_type_scope="...",  # required
    cash_gain_loss_calculation_date="...",  # required
    amortisation_rule_set_id=ResourceId(...),  # optional
    leader_nav_type_code="...",  # optional
    transaction_template_scope="..."  # optional
)
```

- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)
- [ResourceId](ResourceId.md)


[Back to top](#) · [Back to API list](../../api_endpoints.md) · [Back to Model list](../../models.md) · [Back to README](../../../../../README.md)

